from scipy.differentiate import derivative as scipy_derivative


def forward_difference(f, x, h=1e-5):
    """前進差分商: f'(x) ≈ (f(x+h) - f(x)) / h"""
    return (f(x + h) - f(x)) / h


def backward_difference(f, x, h=1e-5):
    """後進差分商: f'(x) ≈ (f(x) - f(x-h)) / h"""
    return (f(x) - f(x - h)) / h


def central_difference(f, x, h=1e-5):
    """中心差分商: f'(x) ≈ (f(x+h) - f(x-h)) / 2h"""
    return (f(x + h) - f(x - h)) / (2 * h)


def scipy_diff(f, x):
    """scipy.differentiate.derivative による数値微分"""
    return scipy_derivative(f, x).df


if __name__ == "__main__":
    # f(x) = x^2 の微分 → f'(x) = 2x で検証
    f = lambda x: x ** 2
    x = 3.0
    exact = 2 * x  # 6.0

    print(f"真値:                          {exact}")
    print(f"前進差分商:                    {forward_difference(f, x)}")
    print(f"後進差分商:                    {backward_difference(f, x)}")
    print(f"中心差分商:                    {central_difference(f, x)}")
    print(f"scipy.differentiate.derivative: {scipy_diff(f, x)}")
