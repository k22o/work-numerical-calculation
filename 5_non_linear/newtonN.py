import numpy as np


def newton_nd(F, J, x0, tol=1e-10, max_iter=100):
    """
    F  : R^n -> R^n  (residual vector function)
    J  : R^n -> R^(n x n)  (Jacobian function)
    x0 : initial guess (array-like)
    """
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        Fx = F(x)
        Jx = J(x)
        dx = np.linalg.solve(Jx, -Fx)  # solve J * dx = -F
        x = x + dx
        norm = np.linalg.norm(Fx)
        print(f"iter {i+1:3d}: x = {x}, ||F(x_prev)|| = {norm:.3e}")
        if np.linalg.norm(dx) < tol:
            return x, i + 1
    raise RuntimeError("not converged")


# --- example: 2-variable system ---
# f1(x, y) = x^2 + y^2 - 1  = 0
# f2(x, y) = y - x^2         = 0
# solution: intersection of unit circle and parabola y = x^2

def F(v):
    x, y = v
    return np.array([
        x**2 + y**2 - 1,
        y - x**2,
    ])


def J(v):
    x, y = v
    return np.array([
        [2*x,  2*y],
        [-2*x,  1 ],
    ])


if __name__ == "__main__":
    x0 = [0.5, 0.5]
    root, n_iter = newton_nd(F, J, x0)
    print(f"\nroot : x = {root}")
    print(f"F(x) = {F(root)}")
    print(f"converged in {n_iter} iterations")
