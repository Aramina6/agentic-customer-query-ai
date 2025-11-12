from langchain_core.tools import tool
from sympy import sympify, simplify


@tool
def calculate(expression: str) -> str:
    """
    Safely evaluate a math expression.
    Example: "150 * 0.8" → "Result: 120.0"
    """
    try:
        expr = sympify(expression.replace("^", "**"))  # allow ^ for power
        result = simplify(expr).evalf()
        return f"Result: {result}"
    except Exception as e:
        return f"Math error: {e}"
