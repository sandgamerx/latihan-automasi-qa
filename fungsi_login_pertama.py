import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    """Fungsi ini menyiapkan driver Chrome dan WebDriverWait."""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    return driver, wait

def perform_login(driver, username, password):
    """Fungsi ini membuka web dan melakukan aksi login."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    print(f"Mencoba login dengan user: {username}")

def verify_login_success(wait):
    """Fungsi ini memverifikasi jika login berhasil."""
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Products']")))
        print("VERIFIKASI SUKSES: Login berhasil.")
        print("--- TEST PASSED ---")
    except Exception:
        print("VERIFIKASI GAGAL: Login seharusnya berhasil, tapi gagal.")
        print("--- TEST FAILED ---")

def verify_login_failed(wait):
    """Fungsi ini memverifikasi jika login gagal dengan pesan yang benar."""
    try:
        error_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        if "Sorry, this user has been locked out" in error_element.text:
            print("VERIFIKASI SUKSES: Pesan error yang benar muncul.")
            print("--- TEST PASSED ---")
        else:
            print("VERIFIKASI GAGAL: Pesan error tidak sesuai.")
            print("--- TEST FAILED ---")
    except Exception:
        print("VERIFIKASI GAGAL: Elemen pesan error tidak ditemukan.")
        print("--- TEST FAILED ---")

def close_driver(driver):
    """Fungsi untuk menutup browser."""
    time.sleep(3)
    driver.quit()

# --- EKSEKUSI UTAMA ---

# Tes 1: Skenario Sukses
print("\n--- MENJALANKAN TES LOGIN SUKSES ---")
driver_sukses, wait_sukses = setup_driver()
perform_login(driver_sukses, "standard_user", "secret_sauce")
verify_login_success(wait_sukses)
close_driver(driver_sukses)

# Tes 2: Skenario Gagal
print("\n--- MENJALANKAN TES LOGIN GAGAL ---")
driver_gagal, wait_gagal = setup_driver()
perform_login(driver_gagal, "locked_out_user", "secret_sauce")
verify_login_failed(wait_gagal)
close_driver(driver_gagal)