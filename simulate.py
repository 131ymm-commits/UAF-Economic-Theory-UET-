import numpy as np
import matplotlib.pyplot as plt

# Параметры
beta = 0.1      # скорость захвата времени
gamma = 0.05    # восстановление t_self
kappa = 0.3     # скорость интеграции
delta = 0.02    # распад интеграции
E_level = 1.2   # эффективность матрёшки
c_i = 0.8       # издержки интеграции

# Начальные состояния
t_self = 8.0
t_captured = 2.0
alpha = 0.5

history = []
for _ in range(100):
    # Уравнения (дискретные)
    d_captured = beta * (1 - alpha) * 1.0 - gamma * t_self
    d_alpha = kappa * (E_level - c_i) * alpha * (1 - alpha) - delta * (1 - alpha)
    
    t_captured += d_captured * 0.1
    t_self -= d_captured * 0.1   # консервация общего времени
    alpha += d_alpha * 0.1
    
    t_self = max(0, min(24, t_self))
    t_captured = max(0, min(24, t_captured))
    alpha = max(0, min(1, alpha))
    
    history.append((t_self, t_captured, alpha))

history = np.array(history)
plt.plot(history[:,0], label='t_self')
plt.plot(history[:,1], label='t_captured')
plt.plot(history[:,2], label='α (интеграция)')
plt.legend()
plt.title('Динамика времени агента (UET)')
plt.xlabel('время, шаги')
plt.ylabel('часы / α')
plt.grid()
plt.show()
