# CalculatorPage.py

import allure
from appium.webdriver.common.appiumby import AppiumBy

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        
        # Definisikan semua alamat elemen di satu tempat
        self.digit_map = {
            '0': (AppiumBy.ID, "com.google.android.calculator:id/digit_0"),
            '1': (AppiumBy.ID, "com.google.android.calculator:id/digit_1"),
            '2': (AppiumBy.ID, "com.google.android.calculator:id/digit_2"),
            '3': (AppiumBy.ID, "com.google.android.calculator:id/digit_3"),
            '4': (AppiumBy.ID, "com.google.android.calculator:id/digit_4"),
            '5': (AppiumBy.ID, "com.google.android.calculator:id/digit_5"),
            '6': (AppiumBy.ID, "com.google.android.calculator:id/digit_6"),
            '7': (AppiumBy.ID, "com.google.android.calculator:id/digit_7"),
            '8': (AppiumBy.ID, "com.google.android.calculator:id/digit_8"),
            '9': (AppiumBy.ID, "com.google.android.calculator:id/digit_9")
        }
        self.button_plus = (AppiumBy.ACCESSIBILITY_ID, "tambah")
        self.button_minus = (AppiumBy.ACCESSIBILITY_ID, "kurang")
        self.button_equals = (AppiumBy.ACCESSIBILITY_ID, "sama dengan")
        self.result_field = (AppiumBy.ID, "com.google.android.calculator:id/result_final")
        self.clear_button = (AppiumBy.ACCESSIBILITY_ID, "kosongkan")

    @allure.step("Menekan tombol angka: {digit}")
    def press_digit(self, digit):
        """Menekan tombol angka berdasarkan karakter ('0'-'9')."""
        self.driver.find_element(*self.digit_map[digit]).click()

    @allure.step("Menekan tombol Tambah (+)")
    def press_plus(self):
        self.driver.find_element(*self.button_plus).click()

    @allure.step("Menekan tombol Kurang (-)")
    def press_minus(self):
        self.driver.find_element(*self.button_minus).click()

    @allure.step("Menekan tombol Sama Dengan (=)")
    def press_equals(self):
        self.driver.find_element(*self.button_equals).click()

    @allure.step("Membersihkan hasil (Clear)")
    def press_clear(self):
        self.driver.find_element(*self.clear_button).click()
        
    @allure.step("Mendapatkan teks hasil akhir")
    def get_result(self):
        return self.driver.find_element(*self.result_field).text