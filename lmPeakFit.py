import numpy as np
from lmfit.models import GaussianModel, ExponentialModel, LorentzianModel, LinearModel, DampedOscillatorModel
import peak_Detect as pd
import matplotlib.pyplot as plt
from scipy import signal
import math





"""Fits a dataset with a sum of lorentzians with a linear background. Params is a list of the form [ctr1,amp1,sig1,ctr2,...]. ctr_range, amp_range, sig_range
set how much the peak parameters may vary. For this fitting function to be effective, all peaks including double peaks should be found. Including small false
peaks should be okay as long as they are filtered later. Returns a ModelResult class with fitted parameters"""
def lmLorFit(xdata, ydata, params, ctr_range = 1.2, amp_range = 3 , sig_range= 6):
    x = xdata
    y = ydata
    line_mod = LinearModel(prefix='line_')
    lorentz_mod = DampedOscillatorModel(prefix='lor_')
    pars =  line_mod.make_params(intercept=0, slope=0)
    pars['line_intercept'].set(0, vary=True)
    pars['line_slope'].set(0, vary=True)

    peaks=[]
    for i in range(0, len(params)/3):
        peaks.append(DampedOscillatorModel(prefix='lo'+str(i)+'_'))
        pars.update(peaks[i].make_params())
        ctr=params[3*i]
        amp=params[3*i+1]
        sig=params[3*i+2]
        print sig
        pars['lo'+str(i)+'_center'].set(ctr, min=ctr/ctr_range, max=ctr*ctr_range)
        pars['lo'+str(i)+'_amplitude'].set(amp,min=amp/amp_range, max=amp*amp_range)
        pars['lo'+str(i)+'_sigma'].set(sig, min=sig/sig_range, max=sig*sig_range)

    mod=line_mod
    for i in xrange(len(peaks)):
        mod=mod+peaks[i]

    init = mod.eval(pars, x=x)
    out=mod.fit(y, pars,x=x, weights=np.sqrt(y))
    fittedsigma = out.params['lo0_sigma'].value
    fittedAmp = out.params['lo0_amplitude'].value
    fittedCenter = out.params['lo0_center'].value
    fittedQ=1/(2*fittedsigma)

    """Returns output fit as will as list of important fitting parameters"""
    return out, [fittedCenter, fittedAmp, fittedsigma, fittedQ]

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
