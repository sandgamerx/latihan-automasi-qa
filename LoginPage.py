# LoginPage.py

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # --- BAGIAN YANG HILANG ADA DI SINI ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")
    # ------------------------------------

    @allure.step("Buka halaman login")
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Masukkan username: {username}")
    def enter_username(self, username):
        user_input = self.wait.until(EC.element_to_be_clickable(self.username_input))
        user_input.send_keys(username)

    @allure.step("Masukkan password")
    def enter_password(self, password):
        pass_input = self.wait.until(EC.element_to_be_clickable(self.password_input))
        pass_input.send_keys(password)

    @allure.step("Klik tombol login")
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    @allure.step("Dapatkan pesan error")
    def get_error_message(self):
        error_element = self.wait.until(EC.presence_of_element_located(self.error_message))
        return error_element.text