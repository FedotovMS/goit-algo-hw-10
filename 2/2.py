import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
def monte_carlo_integral(f, a, b, num_points=100000):
    # Генерація випадкових точок
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, max(f(x_random)), num_points)
    
    # Підрахунок кількості точок, що знаходяться під графіком
    under_curve = np.sum(y_random <= f(x_random))
    
    # Обчислення площі під графіком
    area = (under_curve / num_points) * (b - a) * max(f(x_random))
    return area

# Обчислення інтегралів
monte_carlo_result = monte_carlo_integral(f, a, b)
quad_result, error = spi.quad(f, a, b)

# Виведення результатів
print(f"\n\nРезультат інтеграції методом Монте-Карло: {monte_carlo_result}")
print(f"Результат інтеграції методом quad: {quad_result}, Похибка: {error}\n\n")

# Створення графіка для візуалізації
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()