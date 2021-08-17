import pytest
import re
import src.exercise

def test_exercise():
    assert src.exercise.sumaFibonacci() == 4613730, "Verifica el funcionamiento del programa"   
