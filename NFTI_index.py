import numpy as np

def nfti(t_self_array, t_captured_array, theta=1.0):
    return np.mean(t_self_array - theta * t_captured_array)

# Пример данных (часы в сутки)
population_self = np.array([6, 5, 7, 4, 8, 3])
population_captured = np.array([2, 3, 1, 4, 0, 5])

print("NFTI =", nfti(population_self, population_captured))
