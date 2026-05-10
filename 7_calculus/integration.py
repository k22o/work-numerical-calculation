import numpy as np
from scipy.integrate import quad


def trapezoidal(f, a, b, n=1000):
    """台形公式: 2点間を線形補間して積分"""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    return h / 2 * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))


def simpson(f, a, b, n=1000):
    """シンプソンの1/3公式: 3点間を2次補間して積分 (n は偶数)"""
    if n % 2 != 0:
        raise ValueError("n は偶数である必要があります")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    weights = np.ones(n + 1)
    weights[1:-1:2] = 4  # 奇数インデックス
    weights[2:-2:2] = 2  # 偶数インデックス（端除く）
    return h / 3 * np.dot(weights, f(x))


def gauss_legendre(f, a, b, n=5):
    """ガウス・ルジャンドル求積: ルジャンドル多項式の零点を節点として使用"""
    nodes, weights = np.polynomial.legendre.leggauss(n)
    # [-1, 1] -> [a, b] に変換
    x = (b - a) / 2 * nodes + (a + b) / 2
    return (b - a) / 2 * np.dot(weights, f(x))


def scipy_quad(f, a, b):
    """scipy.integrate.quad による数値積分"""
    result, _ = quad(f, a, b)
    return result


if __name__ == "__main__":
    # f(x) = x^2 の [0, 1] 上の積分 → 真値 = 1/3
    f = lambda x: x ** 2
    a, b = 0.0, 1.0
    exact = 1 / 3

    print(f"真値:                     {exact:.15f}")
    print(f"台形公式 (n=1000):        {trapezoidal(f, a, b):.15f}")
    print(f"シンプソン (n=1000):      {simpson(f, a, b):.15f}")
    print(f"ガウス・ルジャンドル(n=5): {gauss_legendre(f, a, b):.15f}")
    print(f"scipy.integrate.quad:     {scipy_quad(f, a, b):.15f}")
