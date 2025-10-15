# TikTokSearchPage.py
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TikTokSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
        # Kolom Input: Menggunakan ID yang Benar
        self.search_input_field = (AppiumBy.ID, "com.ss.android.ugc.trill:id/g4j") 
        
        # --- PERBAIKAN: XPath Video Pertama Dibuat menjadi Locator ---
        # Menggunakan XPATH yang Anda temukan (diperbaiki sintaksnya)
        self.video_results = (AppiumBy.XPATH, "//android.view.View[@resource-id='com.ss.android.ugc.trill:id/udh']")
        # -------------------------------------------------------------

    @allure.step("Ketik kata kunci: '{keyword}'")
    def enter_keyword(self, keyword):
        # 1. Tunggu sampai elemennya muncul
        search_field = self.wait.until(
            EC.presence_of_element_located(self.search_input_field)
        )
        # 2. Klik, Clear, dan Send Keys
        search_field.click()
        search_field.clear()
        search_field.send_keys(keyword)
        
        # 3. Tekan 'Enter'
        self.driver.press_keycode(66)

    @allure.step("Menekan video hasil pencarian pertama")
    def click_first_result(self):
        """Mencari semua elemen hasil video dan mengklik yang pertama."""
        
        # Gunakan find_elements (perhatikan 's' di akhir)
        video_results = self.driver.find_elements(*self.video_results)
        
        # Verifikasi bahwa ada hasil yang ditemukan
        if not video_results:
            raise Exception("Gagal menemukan hasil pencarian video setelah pencarian.")
            
        # Klik elemen pertama dalam list
        video_results[0].click()