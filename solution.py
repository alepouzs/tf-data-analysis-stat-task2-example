import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 487382438 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    return np.max(x), (np.max(x - 0.053) / ((1 - p) ** (1 / len(x))) + 0.053
