import math


def f(x):
    return x - math.cos(x)

def df(x):
    return 1 + math.sin(x)

def newton(x0, tol=1e-10, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        x_new = x - fx / dfx
        print(f"iter {i+1:3d}: x = {x_new:.15f}, f(x) = {f(x_new):.3e}")
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    raise RuntimeError("not converged")


if __name__ == "__main__":
    x0 = 1.0
    root, n_iter = newton(x0)
    print(f"\nroot: x = {root:.15f} (converged in {n_iter} iterations)")
