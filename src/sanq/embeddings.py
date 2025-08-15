from __future__ import annotations
import numpy as np
import hashlib

def text_hash_embed(text: str, dim: int = 128) -> np.ndarray:
    v = np.zeros(dim, dtype=np.float32)
    for token in text.split():
        h = int(hashlib.sha256(token.encode("utf-8")).hexdigest(), 16)
        idx = h % dim
        v[idx] += 1.0
    if np.linalg.norm(v) > 0:
        v = v / np.linalg.norm(v)
    return v
