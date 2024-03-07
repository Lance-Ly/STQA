import pytest
from app.bmi_calculator import calculate_bmi, bmi_category

def test_calculate_bmi():
    assert calculate_bmi(5, 7, 160) == pytest.approx(25.08, 0.01)

def test_bmi_category_underweight():
    assert bmi_category(17) == 'Underweight'

def test_bmi_category_normal():
    assert bmi_category(22) == 'Normal weight'

def test_bmi_category_overweight():
    assert bmi_category(27) == 'Overweight'

def test_bmi_category_obese():
    assert bmi_category(31) == 'Obese'
