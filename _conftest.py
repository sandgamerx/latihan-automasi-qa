# conftest.py

import pytest
from selenium import webdriver
from ProductsPage import ProductsPage 

@pytest.fixture(scope="session") #ganti dengan scope="function" untuk jalankan test buka tutup browser, ganti scope="session" untuk sekali jalan
def driver():
    #chrome_options = webdriver.ChromeOptions()
    #prefs = {
    #    "credentials_enable_service": False,
    #    "profile.password_manager_enabled": False
    #}
    #chrome_options.add_experimental_option("prefs", prefs)
    
        # Menonaktifkan pop-up yang sudah kita identifikasi sebelumnya
    #chrome_options.add_argument("--disable-save-password-bubble")
    #chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    
        # --- MATIKAN SEMENTARA MODE HEADLESS UNTUK DEBUGGING ---
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--window-size=1920,1080")
    # --------------------------------------------------------

    print("\n--- (SESI) Membuka Browser Chrome (Mode Normal/Visual) ---")
    #browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Firefox() #bisa pindah antara firefox atau chrome
    
    yield browser

    print("\n--- (SESI) Menutup Browser di Akhir Sesi---")
    browser.quit()
    
# ... fixture cleanup_after_test tetap sama ...
@pytest.fixture(scope="function", autouse=True)
def cleanup_after_test(driver):
    """
    Fixture level FUNGSI. Dijalankan otomatis SETELAH setiap tes.
    Tugasnya adalah membersihkan state browser secara total.
    """
    # 'yield' berarti di titik inilah tesnya akan berjalan
    yield

    # --- TEARDOWN / PEMBERSIHAN ---
    print("\n--- (FUNGSI) Memulai Pembersihan Total ---")
    
    # 1. Coba logout jika memungkinkan
    if "inventory.html" in driver.current_url:
        print("   -> Kondisi: Berhasil login, melakukan logout...")
        products_page = ProductsPage(driver)
        products_page.logout()
    else:
        print("   -> Kondisi: Tidak login, logout dilewati.")
        
    # 2. Hapus semua sisa data (cookies, storage)
    print("   -> Menghapus semua cookies...")
    driver.delete_all_cookies()
    print("   -> Membersihkan Local Storage & Session Storage...")
    driver.execute_script("window.sessionStorage.clear()")
    driver.execute_script("window.localStorage.clear()")
    
    print("--- Pembersihan Selesai ---")