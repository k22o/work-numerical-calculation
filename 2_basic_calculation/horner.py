"""
Horner's method for polynomial evaluation.
"""

import numpy as np

def horner(coeffs: list[float], x: float) -> float:
    """Evaluate a polynomial at x using Horner's method.

    Args:
        coeffs: Coefficients [a0, a1, ..., an] (ascending order of degree).
        x: Point at which to evaluate the polynomial.

    Returns:
        p(x)
    """
    result = 0.0
    for a in coeffs:
        result = a + x * result
    return result


if __name__ == "__main__":
    # p(x) = 3x^2 + 2x + 1  =>  coeffs = [3, 2, 1]
    coeffs = [3, 2, 1]
    x = 2.0

    result_horner = horner(coeffs, x)
    result_numpy = np.polyval(list(coeffs), x)

    print(f"p(x) = 3x^2 + 2x + 1 ,  x = {x}") 
    print(f"  Horner : {result_horner}")
    print(f"  NumPy  : {result_numpy}")
    print(f"  差分   : {abs(result_horner - result_numpy)}")
