# test_tiktok_search.py
import pytest
import allure
import time
from MOBILE_PROJECTS.TikTok_App.Pages.TikTokHomePage import TikTokHomePage
from MOBILE_PROJECTS.TikTok_App.Pages.TikTokSearchPage import TikTokSearchPage
#from appium.webdriver.common.appiumby import AppiumBy

@allure.title("Tes Pencarian di Aplikasi TikTok")
def test_tiktok_search(driver):
    """
    Skenario:
    1. Buka aplikasi dan tekan tombol Cari.
    2. Masukkan kata kunci "nasi goreng mantab".
    """
    
    print("\nMenunggu aplikasi TikTok dimuat...")
    time.sleep(5)
    
    home_page = TikTokHomePage(driver)
    search_page = TikTokSearchPage(driver)
    
    # 1. Tekan tombol Cari (Search) di Home Page
    home_page.click_search()
    print("Berhasil pindah ke halaman Cari.")
    time.sleep(3) # Jeda agar halaman pencarian termuat
    
    # 2. Masukkan kata kunci
    keyword = "nasi goreng mantab"
    search_page.enter_keyword(keyword)
    print(f"Berhasil mencari kata kunci: {keyword}")
    time.sleep(5) # Jeda untuk melihat hasil pencarian
    
    # --- LANGKAH AKHIR: Klik Hasil Pencarian Pertama ---
    try:
        search_page.click_first_result() # Panggil metode baru dari Page Object
        print("Berhasil mengklik video hasil pencarian pertama.")
        time.sleep(5)
        
    except Exception as e:
        # Gagal mengklik karena tidak menemukan hasil
        pytest.fail(f"Gagal mengklik hasil pencarian: {e}")
        
    # --- Verifikasi Sederhana ---
    # Tambahkan verifikasi di sini (misalnya, cek apakah video mulai diputar)