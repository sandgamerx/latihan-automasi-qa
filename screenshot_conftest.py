# conftest.py

import pytest
from selenium import webdriver
import os
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    """Fixture ini memberikan browser yang 100% baru dan bersih."""
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    
    print("\n--- (FUNGSI) Membuka Browser Baru yang Steril ---")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\n--- (FUNGSI) Menutup Browser ---")
    browser.quit()

# --- HOOK UNTUK SCREENSHOT SAAT GAGAL ---

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook ini dijalankan setelah setiap fase tes (setup, call, teardown).
    """
    # Eksekusi semua hook lain untuk mendapatkan objek 'report'
    outcome = yield
    report = outcome.get_result()

    # Kita hanya peduli pada fase 'call' (saat tesnya dijalankan) dan jika tesnya GAGAL
    if report.when == 'call' and report.failed:
        # Buat folder 'screenshots' jika belum ada
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
            
        try:
            # Ambil fixture 'driver' dari konteks tes
            driver = item.funcargs['driver']
            
            # Buat nama file yang unik berdasarkan nama tes dan timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            test_name = item.name.replace('[', '_').replace(']', '') # Bersihkan nama tes
            screenshot_path = os.path.join('screenshots', f'{test_name}_{timestamp}.png')
            
            # Ambil screenshot
            driver.save_screenshot(screenshot_path)
            print(f"\n   -> Screenshot disimpan di: {screenshot_path}")
            
        except Exception as e:
            print(f"\n   -> Gagal mengambil screenshot: {e}")