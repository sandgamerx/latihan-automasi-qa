# ProductsPage.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        # TINGKATKAN WAKTU TUNGGU DI SINI JUGA
        self.wait = WebDriverWait(self.driver, 20) # <-- Ubah dari 10 menjadi 20
        
        self.burger_menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.driver.find_element(*self.burger_menu_button).click()
        logout_button = self.wait.until(EC.element_to_be_clickable(self.logout_link))
        logout_button.click()