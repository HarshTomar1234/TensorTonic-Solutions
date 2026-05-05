import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    sig_x = 1 / (1 + np.exp(-x))

    return sig_x



    