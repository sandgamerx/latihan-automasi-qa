# LoginPage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Waktu tunggu 20 detik sudah bagus
        self.wait = WebDriverWait(self.driver, 20)
        
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        """Metode yang diperbarui agar lebih sabar."""
        # Tunggu sampai elemen bisa diinteraksi, baru isi
        user_input = self.wait.until(EC.element_to_be_clickable(self.username_input))
        user_input.send_keys(username)

    def enter_password(self, password):
        """Metode yang diperbarui agar lebih sabar."""
        # Tunggu sampai elemen bisa diinteraksi, baru isi
        pass_input = self.wait.until(EC.element_to_be_clickable(self.password_input))
        pass_input.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    def get_error_message(self):
        error_element = self.wait.until(EC.presence_of_element_located(self.error_message))
        return error_element.text