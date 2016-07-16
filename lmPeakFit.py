import numpy as np
from lmfit.models import GaussianModel, ExpressionModel, ExponentialModel, LorentzianModel, LinearModel, DampedOscillatorModel
import peak_Detect as pd
import matplotlib.pyplot as plt
from scipy import signal
import math
from lmfit import CompositeModel, Model

def find_nearestx(x, value):
    idx = (np.abs(x-value)).argmin()
    return idx, x[idx]

def DDOphase(x, w0, Q, m , b):
    y= (-np.arctan2(w0 * x/Q,w0**2-x**2))*180/np.pi+m*x+b
    return y

"""Fits a dataset with a sum of lorentzians with a linear background. Params is a list of the form [ctr1,amp1,sig1,ctr2,...]. ctr_range, amp_range, sig_range
set how much the peak parameters may vary. For this fitting function to be effective, all peaks including double peaks should be found. Including small false
peaks should be okay as long as they are filtered later. Returns a ModelResult class with fitted parameters"""
def lmDDOFit(xdata, ydata, params, ctr_range = 1.2, amp_range = 3 , sig_range= 6, weightexponential = 0):    
    
    
    x = xdata
    y = ydata
#Define a linear model and a Damped Oscillator Model    
    line_mod = LinearModel(prefix='line_')
    ddo_mod = DampedOscillatorModel(prefix='ddo_')
#Initial Pars for Linear Model
    pars =  line_mod.make_params(intercept=0, slope=0)
    pars['line_intercept'].set(0, vary=True)
    pars['line_slope'].set(0, vary=True)
#Extend param list to use multiple peaks. Currently unused.
    peaks=[]
#Add fit parameters, Center, Amplitude, and Sigma
    for i in range(0, len(params)/3):
        peaks.append(DampedOscillatorModel(prefix='ddo'+str(i)+'_'))
        pars.update(peaks[i].make_params())
        ctr=params[3*i]
        amp=params[3*i+1]
        sig=params[3*i+2]
        pars['ddo'+str(i)+'_center'].set(ctr, min=ctr/ctr_range, max=ctr*ctr_range)
        pars['ddo'+str(i)+'_amplitude'].set(amp,min=amp/amp_range, max=amp*amp_range)
        pars['ddo'+str(i)+'_sigma'].set(sig, min=sig/sig_range, max=sig*sig_range)
#Create full model. Add linear model and all peaks
    mod=line_mod
    for i in xrange(len(peaks)):
        mod=mod+peaks[i]
#Initialize fit
    init = mod.eval(pars, x=x)
#Do the fit. The weight exponential can weight the points porportional to the
#amplitude of y point. In this way, points on peak can be given more weight.     
    out=mod.fit(y, pars,x=x, weights=y**weightexponential)
#Get the fit parameters
    fittedsigma = out.params['ddo0_sigma'].value
    fittedAmp = out.params['ddo0_amplitude'].value
    fittedCenter = out.params['ddo0_center'].value
    fittedIntercept = out.params['line_intercept'].value
    fittedSlope = out.params['line_slope'].value
    fittedQ=1/(2*fittedsigma)
#Returns the output fit as well as an array of the fit parameters
    """Returns output fit as will as list of important fitting parameters"""
    return out, [fittedCenter, fittedAmp, fittedsigma, fittedQ, fittedIntercept, fittedSlope]

def jump(x, mid):
    "heaviside step function"
    o = np.zeros(len(x))
    imid = max(np.where(x<=mid)[0])
    o[imid:] = - 2*np.pi
    return o
    
def phase(x, off, m, f0, Q):
    list0=np.zeros(len(x)) 
    imid = max(np.where(x<=f0)[0])
    list0[imid:] = - 2*np.pi
    o=off + m*x- np.arctan(1/Q * 1/(f0/x - x/f0))+list0
    return o
    
def lmDDOPhaseFit(xdata, ydata, params, f0_range = 1.2, Q_range = 3):    
    f0= params[0]
    Q=1/(2*params[2])
    
    x = xdata
    y = ydata
#Define a linear model and a Damped Oscillator Model    
#    ddophase_mod = ExpressionModel('off + m*x- arctan(1/Q * 1/(f0/x - x/f0))-')
    ddophase_mod = Model(phase)
#Initial Pars for Linear Model
    pars =  ddophase_mod.make_params(off=0, m=0, f0=f0, Q=Q)

#Add fit parameters, Center, Amplitude, and Sigma
    pars['f0'].set(min=f0/f0_range, max=f0*f0_range)
    pars['Q'].set(min=Q/Q_range, max=Q*Q_range)
#Create full model. Add linear model and all peaks
#Initialize fit
    init = ddophase_mod.eval(pars, x=x)
#Do the fit. The weight exponential can weight the points porportional to the
#amplitude of y point. In this way, points on peak can be given more weight.     
    out=ddophase_mod.fit(y, pars,x=x)
#Get the fit parameters
    fittedf0= out.params['f0'].value
    fittedQ = out.params['Q'].value
#Returns the output fit as well as an array of the fit parameters
    """Returns output fit as will as list of important fitting parameters"""
    return out, [fittedf0, np.nan, np.nan, fittedQ]

def fitSingleLorentzian(data, expectedQ, lookahead, delta, backgroundData = None, svgWindowLength = 11, svgOrder= 5):
    """Fits a data to a single lorentzian plus a linear background. The expected Q
    must be manually measured and entered. Lookahead and delta pass to the peakdetect
    function and will determine how many peaks are found. Only the largest peak
    will be fit in this function. A background dataset may be entered and will be
    subtracted off. A Savgoy-Galow filter is applied before the peak finding (but not fitting)
    The windowlength and order can be changed. Returns a the output fit and the list of fitted paramaters as
    [Center, Amp, FWHM, Q]
    """
    f=data[:,0]
    t=data[:,3]

    if backgroundData == None:
        r=data[:,2]
    elif len(backgroundData) == len(r=data[:,2]):
        r=data[:,2]-backgroundData
    else:
        print "Length of Background Data is not equal Length of r"
        return



    #apply SVG filter to make peak detection easier
    fr=signal.savgol_filter(r,svgWindowLength,svgOrder)
    _max, _min = pd.peakdetect(fr, None, lookahead, delta)

    #create lists of locations of max/min, values of xmax/xmin and ymax/ymin
    fmi = [p[0] for p in _max]
    fni= [p[0] for p in _min]
    fm = [f[p[0]] for p in _max]
    rm = [p[1] for p in _max]
    fn = [f[p[0]] for p in _min]
    rn = [p[1] for p in _min]

    limitToBigPeak=True
    #change Q to fwhm based on first detected peak location

    fwhm=fm[0]/expectedQ
    paramList=[]

    #if limitToBigPeak is true, will only try to fit maximum peak. Good if only
    #looking at single resonance peak. Problematic if there is a larger BG peak
    #which gets fit.
    if limitToBigPeak == True:
        max_value = max(rm)
        max_index = rm.index(max_value)
        paramList=[fm[max_index], rm[max_index]*fwhm, fwhm]
    else:
        for i in xrange(len(fmi)):
            paramList+=[fm[i], rm[i]*fwhm/2*math.pi, fwhm]

    #fits data to a single lorentzian with a linear background. Parameters are limited
    #in how much they vary so initial choice is vital to a good fit

    out = lmLorFit(f, r, paramList, ctr_range = 1.2, amp_range = 2 , sig_range= 2)
    fittedfwhm = out.params['lo0_fwhm'].value
    fittedAmp = out.params['lo0_amplitude'].value
    fittedCenter = out.params['lo0_center'].value
    fittedQ=fittedCenter/fittedfwhm

    """Returns output fit as will as list of important fitting parameters"""
    return out, [fittedCenter, fittedAmp, fittedfwhm, fittedQ]

def DDOphase(x, w0, Q, m , b):
    y= (-np.arctan2(w0 * x/Q,w0**2-x**2))*180/np.pi+m*x+b
    return y
    
def fitPhaseFromAmp(theta,f, w0,Q):
    phase=theta
    phase = fixPhase(phase)
    FWHM=w0/Q
    w0idx, w0=find_nearestx(f, w0)
    maxval,wmax=find_nearestx(f, w0+3*FWHM)
    minval,wmin=find_nearestx(f, w0-3*FWHM)
    fixedphase=(phase-phase[w0idx])*180/np.pi
    gmod = Model(DDOphase)
    result = gmod.fit(fixedphase[minval:maxval], x=f[minval:maxval], w0=w0, \
                  Q=Q, m =0, b=0)
#    plt.plot(data.f[minval:maxval], result.init_fit, 'r-')
#    plt.plot(data.f[minval:maxval], result.best_fit, 'b-')
#    plt.plot(data.f[minval:maxval], fixedphase[minval:maxval], 'g')
    Q = result.params['Q'].value
    w0 = result.params['w0'].value
    m = result.params['m'].value
    b = result.params['b'].value   
    fout = f[minval:maxval]   
    pout = fixedphase[minval:maxval]       
    return result, [w0, Q, m,b], [fout, pout]
    
def fixPhase(Th):
    for i in xrange(len(Th)-1):
        if Th[i+1]-Th[i]>3:
            for ii in xrange(len(Th)):
                if ii>i:
                    Th[ii]=Th[ii]-2*np.pi
        if Th[i+1]-Th[i]<-3:
            for ii in xrange(len(Th)):
                if ii>i:
                    Th[ii]=Th[ii]+2*np.pi
    return Th