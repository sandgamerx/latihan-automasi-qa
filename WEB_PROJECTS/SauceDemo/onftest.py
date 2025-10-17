# conftest_headless.py

import pytest
from selenium import webdriver

# Fungsi ini menambahkan opsi --browser ke Pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Pilih browser: chrome atau firefox"
    )

@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture ini membuka browser dalam mode headless untuk CI/CD.
    """
    # Baca nilai dari opsi --browser
    browser_name = request.config.getoption("browser")

    # Siapkan browser Chrome
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        
        # Opsi-opsi penting untuk mode headless
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        # Opsi tambahan untuk menonaktifkan pop-up yang mengganggu
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordLeakDetection")
        
        print("\n--- Membuka Browser Chrome (Headless) ---")
        browser = webdriver.Chrome(options=options)
    
    # Anda bisa menambahkan kondisi untuk Firefox jika perlu
    # elif browser_name.lower() == "firefox":
    #     options = webdriver.FirefoxOptions()
    #     options.add_argument("--headless")
    #     browser = webdriver.Firefox(options=options)
        
    else:
        raise pytest.UsageError("--browser harus chrome atau firefox")

    yield browser

    print(f"\n--- Menutup Browser {browser_name.capitalize()} ---")
    browser.quit()