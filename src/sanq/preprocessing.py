from __future__ import annotations
import numpy as np

def bandpass(signal: np.ndarray, fs: float, low: float, high: float) -> np.ndarray:
    if signal.ndim == 1:
        signal = signal[None, :]
    n, t = signal.shape[0], signal.shape[-1]
    freqs = np.fft.rfftfreq(t, d=1.0/fs)
    mask = (freqs >= low) & (freqs <= high)
    out = np.empty_like(signal, dtype=np.float64)
    for i in range(signal.shape[0]):
        S = np.fft.rfft(signal[i])
        S[~mask] = 0
        out[i] = np.fft.irfft(S, n=t).real
    return out.squeeze()

def normalize(x: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    mu = x.mean(axis=-1, keepdims=True)
    sd = x.std(axis=-1, keepdims=True) + eps
    return (x - mu) / sd

def preprocess(signal: np.ndarray, fs: float) -> np.ndarray:
    if signal.ndim == 1:
        signal = signal[None, :]
    x = normalize(signal)
    x = bandpass(x, fs=fs, low=8.0, high=12.0)
    return x.squeeze()
