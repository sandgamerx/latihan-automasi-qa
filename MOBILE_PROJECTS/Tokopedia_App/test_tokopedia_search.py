# test_tokopedia_search.py

import pytest
import allure
import time
from MOBILE_PROJECTS.Tokopedia_App.Pages.HomePage import HomePage
from MOBILE_PROJECTS.Tokopedia_App.Pages.SearchPage import SearchPage

@allure.title("Tes Pencarian Produk di Tokopedia")
def test_product_search(driver):
    """
    Skenario:
    1. Buka aplikasi dan klik kolom pencarian.
    2. Ketik nama produk dan tekan 'Enter'.
    3. Klik produk pertama yang muncul.
    4. Verifikasi (sederhana) bahwa kita pindah ke halaman detail produk.
    """
    
    # Inisialisasi Page Objects
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    
    # --- Aksi Tes ---
    
    # Tunggu beberapa detik agar halaman utama benar-benar termuat
    time.sleep(5)
    
    # 1. Klik kolom pencarian
    home_page.click_search_bar()
    time.sleep(2)

    # 2. Cari produk "iphone 15"
    search_page.enter_search_text("iphone 15")
    time.sleep(5) # Beri waktu hasil pencarian untuk muncul
    
    # 3. Klik produk pertama
    search_page.click_first_product()
    time.sleep(5) # Beri waktu halaman produk untuk termuat

    # --- Verifikasi Sederhana ---
    # Kita hanya akan memverifikasi bahwa URL (current activity) sudah berubah.
    # Ini adalah cara sederhana untuk memastikan kita sudah tidak di halaman pencarian lagi.
    current_activity = driver.current_activity
    print(f"Aktivitas saat ini: {current_activity}")
    
    allure.step(f"Verifikasi bahwa aktivitas saat ini bukan lagi halaman pencarian, melainkan {current_activity}")
    # Contoh verifikasi: pastikan nama 'activity' mengandung kata 'pdp' (Product Detail Page)
    assert 'pdp' in current_activity.lower()