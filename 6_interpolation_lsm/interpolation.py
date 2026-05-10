import numpy as np
import scipy.linalg as sclinalg
import scipy.interpolate as scipl
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


def lagrange_interpolation(x_nodes, y_nodes, x):
    poly = scipl.lagrange(x_nodes, y_nodes)
    return poly(x)


def newton_interpolation(x_nodes, y_nodes, x):
    n = len(x_nodes)
    coeffs = y_nodes.copy().astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coeffs[i] = (coeffs[i] - coeffs[i - 1]) / (x_nodes[i] - x_nodes[i - j])
    result = coeffs[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_nodes[i]) + coeffs[i]
    return result


if __name__ == "__main__":
    n_nodes = 6
    x_nodes = np.linspace(0, 2 * np.pi, n_nodes)
    y_nodes = f(x_nodes)

    x_eval = np.linspace(0, 2 * np.pi, 200)
    y_true = f(x_eval)
    y_lagrange = lagrange_interpolation(x_nodes, y_nodes, x_eval)
    y_newton = np.array([newton_interpolation(x_nodes, y_nodes, x) for x in x_eval])

    print(f"Lagrange max error: {np.max(np.abs(y_lagrange - y_true)):.2e}")
    print(f"Newton   max error: {np.max(np.abs(y_newton   - y_true)):.2e}")

    plt.figure(figsize=(10, 5))
    plt.plot(x_eval, y_true,     "k-",  label="sin(x)", linewidth=2)
    plt.plot(x_eval, y_lagrange, "b--", label="Lagrange")
    plt.plot(x_eval, y_newton,   "r:",  label="Newton",  linewidth=2)
    plt.scatter(x_nodes, y_nodes, color="black", zorder=5, label="nodes")
    plt.legend()
    plt.title(f"Lagrange / Newton Interpolation (n={n_nodes} nodes)")
    plt.tight_layout()
    plt.savefig("interpolation.png", dpi=150)
    plt.show()
