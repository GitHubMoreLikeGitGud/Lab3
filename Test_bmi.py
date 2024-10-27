from Lab2.bmi import calculate_bmi

def test_bmi_under_weight():
    # Testing an "Under Weight" BMI
    assert calculate_bmi(1.73, 50) == -1

def test_bmi_normal_weight():
    # Testing a "Normal Weight" BMI
    assert calculate_bmi(1.73, 65) == 0

def test_bmi_over_weight():
    # Testing an "Over Weight" BMI
    assert calculate_bmi(1.73, 80) == 1