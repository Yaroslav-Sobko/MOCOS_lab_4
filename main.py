import numpy as np
import matplotlib.pyplot as plt

# Крок 1: Згенерувати тестову послідовність
N = 2200
A = 1.0  # Амплітуда
phi = np.pi / 4  # Фазовий зсув
x = np.linspace(0, 10, N)  # Інтервал x для вимірювання значень
noise = np.random.uniform(-0.05 * A, 0.05 * A, N)  # Випадкове відхилення
y = A * np.sin(x + phi) + noise  # Згенерована послідовність

# Крок 2: Допоміжні функції для обчислення середніх значень
def arithmetic_mean(values):
    return np.mean(values)

def harmonic_mean(values):
    return len(values) / np.sum(1 / values)

def geometric_mean(values):
    a = np.array(values)
    return a.prod() ** (1.0 / len(a))

# Крок 3: Допоміжна функція виводу результату на екран
def plot_function(x, y, title):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Крок 4: Допоміжні функції для обчислення точного значення та порівняння з наближеним
def exact_value(x):
    return A * np.sin(x + phi)

def compare_values(approximate, exact):
    absolute_error = np.abs(approximate - exact)
    relative_error = absolute_error / np.abs(exact)
    max_absolute_error = np.max(absolute_error)
    max_relative_error = np.max(relative_error)
    min_absolute_error = np.min(absolute_error)
    min_relative_error = np.min(relative_error)
    return max_absolute_error, max_relative_error, min_absolute_error, min_relative_error

# Крок 5: Порівняти максимуми й мінімуми абсолютних і відносних похибок різних методів
approximate_mean_a = arithmetic_mean(y)
exact_mean_a = arithmetic_mean(exact_value(x))
max_absolute_error_a, max_relative_error_a, min_absolute_error_a, min_relative_error_a = compare_values(approximate_mean_a, exact_mean_a)

approximate_mean_h = harmonic_mean(y)
exact_mean_h = harmonic_mean(exact_value(x))
max_absolute_error_h, max_relative_error_h, min_absolute_error_h, min_relative_error_h = compare_values(approximate_mean_h, exact_mean_h)

approximate_mean_g = geometric_mean(y)
exact_mean_g = geometric_mean(exact_value(x))
max_absolute_error_g, max_relative_error_g, min_absolute_error_g, min_relative_error_g = compare_values(approximate_mean_g, exact_mean_g)


# Крок 6: Візуалізація результатів
plot_function(x, y, 'Generated Sequence')
plot_function(x, exact_value(x), 'Exact Function')
plt.grid()
plt.plot(x, y)
plt.plot(x, exact_value(x))
plt.show()

# Друкуємо результати порівняння
print('Approximate Arithmetic Mean:', approximate_mean_a)
print('Exact Arithmetic Mean:', exact_mean_a)
print('Max Absolute Arithmetic Error:', max_absolute_error_a)
print('Max Relative Arithmetic Error:', max_relative_error_a)
print('Min Absolute Arithmetic Error:', min_absolute_error_a)
print('Min Relative Arithmetic Error:', min_relative_error_a)

print('\n\n\nApproximate Harmonic Mean:', approximate_mean_h)
print('Exact Harmonic Mean:', exact_mean_h)
print('Max Absolute Harmonic Error:', max_absolute_error_h)
print('Max Relative Harmonic Error:', max_relative_error_h)
print('Min Absolute Harmonic Error:', min_absolute_error_h)
print('Min Relative Harmonic Error:', min_relative_error_h)

print('\n\n\nApproximate Geometric Mean:', approximate_mean_g)
print('Exact Geometric Mean:', exact_mean_g)
print('Max Absolute Geometric Error:', max_absolute_error_g)
print('Max Relative Geometric Error:', max_relative_error_g)
print('Min Absolute Geometric Error:', min_absolute_error_g)
print('Min Relative Geometric Error:', min_relative_error_g)