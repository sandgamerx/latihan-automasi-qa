# TikTokHomePage.py
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TikTokHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
        # --- UBAH DI SINI: Gunakan Resource-ID untuk kecepatan ---
        # Catatan: ID ini mungkin rentan terhadap perubahan aplikasi!
        self.like_button = (AppiumBy.ID, "com.ss.android.ugc.trill:id/eu5")
        # --------------------------------------------------------
        
        # --- UBAH DI SINI: Gunakan ACCESSIBILITY_ID ---
        # Ini adalah metode pencarian tercepat kedua setelah resource-id
        # self.like_button = (AppiumBy.ACCESSIBILITY_ID, "Suka")
        # ---------------------------------------------

        # Tombol Cari (Search) - menggunakan Resource ID dari data Anda
        self.search_button = (AppiumBy.ID, "com.ss.android.ugc.trill:id/i7n") 
        # ---------------------------

    @allure.step("Menekan tombol Suka (Like)")
    def click_like(self):
        """Mencari dan menekan tombol Suka."""
        try:
            # Menggunakan EC.presence_of_element_located untuk pencarian yang sangat cepat
            like_element = self.wait.until(
                EC.presence_of_element_located(self.like_button)
            )
            # Klik elemennya
            like_element.click()
            print("Berhasil menekan tombol Suka.")
        except TimeoutException:
            # Jika timeout, berarti tombol tidak ditemukan (mungkin terhalang/sudah di-like).
            print("Tombol Suka tidak ditemukan dalam waktu 10 detik. Lanjut scroll.")
        except Exception as e:
            print(f"Error tak terduga saat klik Like: {e}")
    
    @allure.step("Menekan tombol Cari (Search)")
    def click_search(self):
        """Menekan ikon Cari di bagian bawah atau atas layar."""
        search_element = self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        )
        search_element.click()