# test_mobile_calculator.py

import pytest
import allure
from CalculatorPage import CalculatorPage
import time

# --- Siapkan Data Tes ---
# Format: (angka1, operator, angka2, hasil_yang_diharapkan)
test_data = [
    ('7', '+', '5', '12'),
    ('9', '-', '3', '6'),
    ('1', '+', '0', '1')
]

@allure.title("Tes Fungsionalitas Kalkulator")
@pytest.mark.parametrize("num1, operator, num2, expected_result", test_data)
def test_calculator_operations(driver, num1, operator, num2, expected_result):
    """
    Satu fungsi tes untuk menangani berbagai skenario perhitungan.
    """
    calc = CalculatorPage(driver)
    
    # Gunakan 'try...finally' untuk memastikan kalkulator selalu dibersihkan
    try:
        allure.dynamic.title(f"Tes Perhitungan: {num1} {operator} {num2} = {expected_result}")
        
        # --- Aksi Tes ---
        calc.press_digit(num1)
        
        if operator == '+':
            calc.press_plus()
        elif operator == '-':
            calc.press_minus()
        
        calc.press_digit(num2)
        calc.press_equals()
        
        time.sleep(1) # Beri waktu hasil untuk muncul

        # --- Verifikasi ---
        actual_result = calc.get_result()
        assert actual_result == expected_result
        
    finally:
        # --- Pembersihan ---
        # Langkah ini akan selalu dijalankan, baik tes lulus maupun gagal.
        # Ini penting agar tes berikutnya dimulai dari kondisi kalkulator yang bersih.
        calc.press_clear()