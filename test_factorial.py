import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.factorial import factorial

def test_factorial_1_falla():
    assert factorial(1) == 1

def test_factorial_1_pasa():
    assert factorial(1) == 1

def test_tipo_falla():
    with pytest.raises(TypeError):
        factorial("a")

def test_tipo_pasa():
    assert factorial(5) == 120

def test_negativo_falla():
    with pytest.raises(ValueError):
        factorial(-5)

def test_negativo_pasa():
    with pytest.raises(ValueError):
        factorial(-5)

def test_positivo_falla():
    assert factorial(5) == 120

def test_positivo_pasa():
    assert factorial(5) == 120
