import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver dan wait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.saucedemo.com/")

try:
    # Langkah 1: Isi form login dengan user yang akan gagal
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Berhasil mengisi form dan mengklik login.")

    # Langkah 2: Verifikasi (Assertion) pesan error
    # Kita cari elemen error-nya dan ambil teks di dalamnya
    error_message_locator = (By.XPATH, "//h3[@data-test='error']")
    error_element = wait.until(EC.presence_of_element_located(error_message_locator))
    
    # Ambil teks dari elemen
    actual_message = error_element.text
    expected_message = "Epic sadface: Sorry, this user has been locked out."

    # Bandingkan teks yang kita dapat dengan yang kita harapkan
    if actual_message == expected_message:
        print(f"VERIFIKASI BERHASIL: Pesan error yang benar muncul: '{actual_message}'")
        print("--- TEST PASSED ---")
    else:
        # Ini terjadi jika elemen ditemukan, tapi teksnya berbeda
        print("VERIFIKASI GAGAL: Pesan error tidak sesuai.")
        print(f"Pesan Sebenarnya: '{actual_message}'")
        print(f"Pesan Harusnya: '{expected_message}'")
        print("--- TEST FAILED ---")

except Exception as e:
    # Ini terjadi jika elemen pesan error-nya tidak ditemukan sama sekali
    print("VERIFIKASI GAGAL: Elemen pesan error tidak ditemukan.")
    print(f"Error: {e}")
    print("--- TEST FAILED ---")

finally:
    print("Menutup browser dalam 5 detik...")
    time.sleep(5)
    driver.quit()