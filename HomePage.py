# HomePage.py
import allure
from appium.webdriver.common.appiumby import AppiumBy

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # Ganti dengan ID yang Anda temukan di Inspector
        self.search_bar = (AppiumBy.ID, "com.tokopedia.tkpd:id/et_search") 

    @allure.step("Klik kolom pencarian di halaman utama")
    def click_search_bar(self):
        # Tambahkan wait untuk memastikan elemen siap diklik
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        wait = WebDriverWait(self.driver, 10)
        search_element = wait.until(EC.element_to_be_clickable(self.search_bar))
        search_element.click()