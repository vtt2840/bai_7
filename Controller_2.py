import numpy as np

def create_random_array(M):
    array = np.random.uniform(-1, 1, (6, M))
    rounded_array = np.round(array, 2)
    return rounded_array

