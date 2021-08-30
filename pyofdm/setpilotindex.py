# -*- coding: utf-8 -*-
"""
Create list of pilot indices for equally spaced pilots

Created on Sun Aug 29 11:45:44 2021

@author: dch2y
"""

import numpy as np

def setpilotindex(nData,mQAM,pilotspacing):
    
    kpilot = (4*nData//mQAM+pilotspacing//2)//(pilotspacing-1)
    pilotindex = np.arange(pilotspacing//2,kpilot*pilotspacing+pilotspacing//2,pilotspacing,dtype=int)
    pilotindex = np.concatenate((-1*np.flip(pilotindex),pilotindex))
    return pilotindex