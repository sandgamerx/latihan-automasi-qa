import time
from selenium import webdriver
from LoginPage import LoginPage # Kita masih menggunakan POM

def test_login_success():
    """Tes skenario login yang berhasil."""
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    time.sleep(1) # Tunggu sesaat
    
    # --- ASSERTION PYTEST ---
    # 'assert' adalah perintah Pytest untuk verifikasi.
    # Jika kondisi setelah 'assert' adalah True, tes lulus.
    # Jika False, tes gagal.
    assert "inventory.html" in driver.current_url

    driver.quit()

def test_login_failed():
    """Tes skenario login yang gagal."""
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    expected_message = "Sorry, this user has been locked out"
    actual_message = login_page.get_error_message()
    
    # --- ASSERTION PYTEST ---
    assert expected_message in actual_message

    driver.quit()