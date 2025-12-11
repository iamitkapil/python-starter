
# Test CHANGE to test PR trigger
def run_expression_vulnerable(expr: str):
    """
    VULNERABLE: evaluating arbitrary expressions supplied by users.
    This allows execution of arbitrary Python code.
    """
    return eval(expr)  # DANGEROUS


# SECURE alternative using ast.literal_eval (safe for literals)
import ast

def run_expression_secure(expr: str):
    """
    Secure alternative: allow only Python literals (lists, dicts, numbers, strings).
    """
    return ast.literal_eval(expr)


if __name__ == "__main__":
    print("vulnerable eval:", run_expression_vulnerable("1 + 2"))
    print("secure eval:", run_expression_secure("[1, 2, 3]"))
