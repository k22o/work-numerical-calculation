import numpy as np
from scipy.integrate import solve_ivp


def euler(f, x0, y0, x_end, h=0.01):
    """オイラー法: y_{n+1} = y_n + h * f(x_n, y_n)"""
    xs = [x0]
    ys = [y0]
    x, y = x0, y0
    while x < x_end - 1e-12:
        y = y + h * f(x, y)
        x = x + h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def midpoint(f, x0, y0, x_end, h=0.01):
    """中点法: 2次精度のルンゲクッタ法"""
    xs = [x0]
    ys = [y0]
    x, y = x0, y0
    while x < x_end - 1e-12:
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        y = y + h * k2
        x = x + h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def runge_kutta4(f, x0, y0, x_end, h=0.01):
    """4次ルンゲクッタ法: 4次精度"""
    xs = [x0]
    ys = [y0]
    x, y = x0, y0
    while x < x_end - 1e-12:
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def scipy_solve(f, x0, y0, x_end, rtol=1e-8, atol=1e-10):
    """scipy.integrate.solve_ivp による求解 (RK45、自動刻み幅制御)"""
    sol = solve_ivp(
        lambda x, y: [f(x, y[0])],
        [x0, x_end],
        [y0],
        rtol=rtol,
        atol=atol,
    )
    return sol.t, sol.y[0]


if __name__ == "__main__":
    # dy/dx = y, y(0) = 1 → 真値: y = e^x
    f = lambda x, y: y
    x0, y0, x_end = 0.0, 1.0, 2.0
    exact = lambda x: np.exp(x)

    methods = {
        "オイラー法          (h=0.01)": euler(f, x0, y0, x_end, h=0.01),
        "中点法              (h=0.01)": midpoint(f, x0, y0, x_end, h=0.01),
        "ルンゲクッタ4次     (h=0.01)": runge_kutta4(f, x0, y0, x_end, h=0.01),
        "scipy RK45 (rtol=1e-8)      ": scipy_solve(f, x0, y0, x_end),
    }

    print(f"x=2.0 での比較 (真値: {exact(2.0):.10f})")
    print("-" * 55)
    for name, (xs, ys) in methods.items():
        y_end = ys[-1]
        error = abs(y_end - exact(xs[-1]))
        print(f"{name}: y={y_end:.10f}  誤差={error:.2e}")
