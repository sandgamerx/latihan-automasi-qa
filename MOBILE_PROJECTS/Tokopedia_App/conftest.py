# conftest.py

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
    appium_options = UiAutomator2Options()
    appium_options.platform_name = "Android"
    appium_options.udid = "RR8NA0BFQNW" # Pastikan ini masih UDID HP Anda

    # --- UBAH DUA BARIS DI BAWAH INI ---
    appium_options.app_package = "com.tokopedia.tkpd"
    appium_options.app_activity = "com.tokopedia.navigation.presentation.activity.NewMainParentActivity"
    # ------------------------------------
    
    # Tambahkan noReset agar tidak login ulang terus-menerus
    appium_options.no_reset = True 

     # --- TAMBAHAN BARU ---
    # Meminta Appium untuk tidak menggunakan keyboard khusus dari vendor
    appium_options.set_capability("unicodeKeyboard", True)
    appium_options.set_capability("resetKeyboard", True)
    # --------------------

    print("\n--- Menghubungkan ke Perangkat Fisik (Aplikasi Tokopedia) ---")
    appium_driver = webdriver.Remote("http://localhost:4723", options=appium_options)
    
    yield appium_driver
    
    print("\n--- Menutup koneksi ---")
    appium_driver.quit()