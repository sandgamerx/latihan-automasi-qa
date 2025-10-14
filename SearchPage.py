# SearchPage.py
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        
        # Gunakan resource-id yang benar dari Inspector
        self.search_input = (AppiumBy.ID, "com.tokopedia.tkpd:id/et_search") 
        
        # Alamat ini perlu diverifikasi nanti di halaman hasil pencarian
        self.first_product = (AppiumBy.ID, "com.tokopedia.tkpd:id/product_name") 

    @allure.step("Ketik '{text}' di kolom pencarian")
    def enter_search_text(self, text):
        # 1. Tunggu sampai elemennya ada di halaman
        search_field = self.wait.until(
            EC.presence_of_element_located(self.search_input)
        )
        # 2. Klik dulu untuk memastikan fokus
        search_field.click()
        # 3. Hapus teks yang mungkin sudah ada (jika ada)
        search_field.clear()
        # 4. Baru ketik teksnya
        search_field.send_keys(text)
        
        # 5. Tekan 'Enter'
        self.driver.press_keycode(66)