from __future__ import annotations
import numpy as np

def psd_simple(x: np.ndarray, fs: float, nperseg: int = 256):
    if x.ndim == 1:
        x = x[None, :]
    step = nperseg // 2
    freqs = np.fft.rfftfreq(nperseg, d=1.0/fs)
    psds = []
    for ch in x:
        frames = [ch[i:i+nperseg] for i in range(0, len(ch)-nperseg+1, step)]
        acc = 0.0
        for fr in frames:
            F = np.fft.rfft(fr * np.hanning(len(fr)))
            acc += (np.abs(F) ** 2)
        psd = acc / max(1, len(frames))
        psds.append(psd)
    return freqs, np.vstack(psds)

def basic_features(x: np.ndarray, fs: float) -> dict:
    freqs, psd = psd_simple(x, fs)
    bands = {
        "delta": (0.5, 4),
        "theta": (4, 8),
        "alpha": (8, 12),
        "beta": (12, 30),
        "gamma": (30, 45),
    }
    feats = {}
    for name, (lo, hi) in bands.items():
        mask = (freqs >= lo) & (freqs <= hi)
        feats[f"psd_{name}"] = psd[:, mask].mean(axis=1)
    feats["psd_total"] = psd.mean(axis=1)
    return feats
