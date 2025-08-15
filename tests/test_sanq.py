import numpy as np
from src.sanq.preprocessing import preprocess
from src.sanq.features import basic_features
from src.sanq.embeddings import text_hash_embed

def test_preprocess_and_features():
    fs = 128.0
    t = np.linspace(0, 2, int(2*fs), endpoint=False)
    signal = np.sin(2*np.pi*10*t)  # 10 Hz alpha
    x = preprocess(signal, fs=fs)
    feats = basic_features(x, fs=fs)
    assert "psd_alpha" in feats

def test_text_embedding_dim():
    v = text_hash_embed("mente tranquila em paisagem azul", dim=128)
    assert v.shape[0] == 128
