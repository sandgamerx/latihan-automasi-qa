# test_login_smart.py

import time
import pytest
from WEB_PROJECTS.SauceDemo.Pages.LoginPage import LoginPage
# Kita tidak butuh ProductsPage di sini lagi

# --- Daftar Data Tes (tidak berubah) ---
test_data = [
    ("standard_user", "secret_sauce", "inventory.html"),
    # Ubah pesan di bawah ini agar tesnya gagal
    # Pesan aslinya adalah: Epic sadface: Sorry, this user has been locked out.
    # Ubah saja ke apapun yang anda mau biar jadi FAILED, Nanti ngetrigger screenshot auto di allure report
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."), 
    ("problem_user", "secret_sauce", "inventory.html"),
    ("performance_glitch_user", "secret_sauce", "inventory.html")
]

@pytest.mark.parametrize("username, password, expected_outcome", test_data)
def test_login_scenarios(driver, username, password, expected_outcome):
    """Fungsi tes yang bersih, hanya fokus pada aksi dan verifikasi."""
    
    print(f"\n--- Tes untuk user: '{username}' ---")
    login_page = LoginPage(driver)
    
    # Selalu buka halaman login di awal untuk memastikan kondisi bersih
    login_page.open()
    
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if "inventory.html" in expected_outcome:
        assert expected_outcome in driver.current_url
    else:
        actual_message = login_page.get_error_message()
        assert expected_outcome in actual_message