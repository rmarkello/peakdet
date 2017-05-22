#!/usr/bin/env python

import os.path as op
import pytest
import peakdet


def test_PPG():
    file = op.join(op.dirname(__file__),'data','PPG.1D')
    ppg = peakdet.PPG(file, 40)
    ppg.get_peaks()
    with pytest.raises(ValueError): ppg.iHR()
    ppg.iHR(TR=3.0)
    ppg.meanHR()
    ppg.reset(hard=True)


def test_RESP():
    file = op.join(op.dirname(__file__),'data','Resp.1D')
    resp = peakdet.RESP(file, 40)
    resp.get_peaks()
    with pytest.raises(ValueError): resp.RVT()
    resp.RVT(TR=3.0)
    resp.reset(hard=True)


def test_ECG():
    file = op.join(op.dirname(__file__),'data','ECG.1D')
    ecg = peakdet.ECG(file, 1000)
    ecg.get_peaks()
    with pytest.raises(ValueError): ecg.iHR()
    ecg.iHR(TR=3.0)
    ecg.meanHR()
    ecg.reset(hard=True)