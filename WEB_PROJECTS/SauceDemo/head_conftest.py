# conftest.py

import pytest
from selenium import webdriver
import allure # <-- Tambahkan impor ini
# Kita tidak butuh 'os' dan 'datetime' lagi untuk cara ini

# FUNGSI BARU: Untuk menambahkan opsi --browser ke Pytest
def pytest_addoption(parser):
    """Fungsi ini menambahkan opsi custom '--browser' ke command line Pytest."""
    parser.addoption(
        "--browser", action="store", default="chrome", help="Pilih browser: chrome atau firefox"
    )

@pytest.fixture(scope="session")
def driver(request): # <-- Minta 'request' di sini
    """
    Fixture ini sekarang bisa membaca opsi dari command line
    dan membuka browser yang sesuai.
    """
    # Baca nilai dari opsi --browser yang diberikan di terminal
    browser_name = request.config.getoption("browser")
    
    # Siapkan browser berdasarkan nama yang dipilih
    if browser_name.lower() == "chrome":
        print("\n--- (SESI) Membuka Browser Chrome ---")
        options = webdriver.ChromeOptions()
        # Tambahkan semua opsi Chrome kita yang sebelumnya
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordLeakDetection")
        browser = webdriver.Chrome(options=options)
        
    elif browser_name.lower() == "firefox":
        print("\n--- (SESI) Membuka Browser Firefox ---")
        browser = webdriver.Firefox()
        
    else:
        # Jika browser tidak dikenal, berikan error
        raise pytest.UsageError(f"--browser '{browser_name}' tidak dikenal. Pilih 'chrome' atau 'firefox'.")

    yield browser

    print(f"\n--- (SESI) Menutup Browser {browser_name.capitalize()} ---")
    browser.quit()

# --- HOOK UNTUK SCREENSHOT SAAT GAGAL (VERSI ALLURE) ---

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook ini sekarang akan melampirkan screenshot ke laporan Allure
    jika sebuah tes gagal.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        try:
            # Ambil fixture 'driver' dari konteks tes
            driver = item.funcargs['driver']
            
            # Ambil screenshot dan lampirkan ke Allure
            allure.attach(
                driver.get_screenshot_as_png(),  # Mengambil data gambar mentah
                name="screenshot_on_failure",     # Nama lampiran di laporan
                attachment_type=allure.attachment_type.PNG
            )
            print("\n   -> Screenshot dilampirkan ke laporan Allure.")
            
        except Exception as e:
            print(f"\n   -> Gagal melampirkan screenshot: {e}")

# Fixture cleanup_after_test tidak perlu diubah sama sekali
# ... (kode fixture cleanup_after_test tetap di sini) ...