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
    # Langkah 1: Isi form login
    # Situs ini menggunakan ID yang jelas, ini adalah selector terbaik!
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Berhasil mengisi form dan mengklik login.")

    # Langkah 2: Verifikasi (Assertion)
    # Kita tunggu sampai elemen judul 'Products' muncul.
    # Jika tidak muncul dalam 10 detik, WebDriverWait akan error.
    products_title_locator = (By.XPATH, "//span[text()='Products']")
    wait.until(EC.presence_of_element_located(products_title_locator))
    
    # Jika baris di atas berhasil tanpa error, artinya elemen ditemukan.
    print("VERIFIKASI BERHASIL: Login sukses, judul 'Products' ditemukan.")
    print("--- TEST PASSED ---")

except Exception as e:
    # Jika ada error apapun (misal elemen tidak ditemukan), tes gagal.
    print("VERIFIKASI GAGAL: Sesuatu berjalan salah.")
    print(f"Error: {e}")
    print("--- TEST FAILED ---")

finally:
    # Blok 'finally' akan selalu dieksekusi, baik tes berhasil maupun gagal
    print("Menutup browser dalam 5 detik...")
    time.sleep(5)
    driver.quit()