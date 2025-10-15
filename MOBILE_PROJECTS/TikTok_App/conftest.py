# MOBILE_PROJECTS/TikTok_App/conftest.py

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
    appium_options = UiAutomator2Options()
    appium_options.platform_name = "Android"
    appium_options.udid = "RR8NA0BFQNW" 
    appium_options.app_package = "com.ss.android.ugc.trill"
    appium_options.app_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    # -----------------------------------
    appium_options.no_reset = True
    appium_options.set_capability("unicodeKeyboard", True)
    appium_options.set_capability("resetKeyboard", True)

    print("\n--- Menghubungkan ke Perangkat Fisik (Aplikasi TikTok) ---")
    appium_driver = webdriver.Remote("http://localhost:4723", options=appium_options)
    
    yield appium_driver
    
    print("\n--- Menutup koneksi ---")
    appium_driver.quit()