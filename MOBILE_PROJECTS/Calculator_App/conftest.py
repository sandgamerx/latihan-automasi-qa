# conftest.py

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
    appium_options = UiAutomator2Options()
    appium_options.platform_name = "Android"
    
    # Ganti 'deviceName' menjadi alamat unik HP Anda
    appium_options.udid = "RR8NA0BFQNW" # <-- PASTE KODE ANDA DI SINI
    
    appium_options.app_package = "com.google.android.calculator"
    appium_options.app_activity = "com.android.calculator2.Calculator"

    print("\n--- Menghubungkan ke Perangkat Fisik Samsung A51 ---")
    appium_driver = webdriver.Remote("http://localhost:4723", options=appium_options)
    
    yield appium_driver
    
    print("\n--- Menutup koneksi ---")
    appium_driver.quit()