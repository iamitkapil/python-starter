# tests/test_vuln_eval.py
import pytest
from app.vuln_eval import run_expression_vulnerable, run_expression_secure

def test_eval_calculation():
    assert run_expression_vulnerable("2 + 3") == 5

def test_eval_can_run_module_calls():
    # This demonstrates that eval can be used to access modules.
    # This example is safe: retrieving math.sqrt(16) produces 4.0.
    assert run_expression_vulnerable("__import__('math').sqrt(16)") == 4.0

def test_literal_eval_is_strict():
    with pytest.raises(ValueError):
        # ast.literal_eval will not evaluate function calls; should raise for this input
        run_expression_secure("__import__('math').sqrt(16)")
