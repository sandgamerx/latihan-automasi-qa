import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Kita gunakan WebDriverWait untuk menunggu secara cerdas, maksimal 10 detik
wait = WebDriverWait(driver, 10)

# --- STRATEGI BARU DENGAN IFRAME ---
try:
    # 1. Tunggu sampai iframe-nya muncul dan langsung pindah fokus ke dalamnya
    # iFrame Google biasanya memiliki 'accountchooser' di dalam atribut 'src'-nya
    iframe_locator = (By.XPATH, "//iframe[contains(@src, 'accountchooser')]")
    wait.until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))
    print("Berhasil masuk ke dalam iFrame pop-up.")

    # 2. Setelah di dalam iFrame, cari dan klik tombolnya
    button_locator = (By.XPATH, "//*[text()='Stay signed out']")
    stay_signed_out_button = wait.until(EC.element_to_be_clickable(button_locator))
    stay_signed_out_button.click()
    print("Pop-up berhasil ditutup.")

    # 3. PENTING: Kembalikan fokus ke halaman utama
    driver.switch_to.default_content()
    print("Berhasil kembali ke halaman utama.")

except Exception as e:
    print("Pop-up tidak muncul atau gagal ditangani, lanjut saja.")
    # Jika gagal, pastikan fokus kembali ke halaman utama
    driver.switch_to.default_content()
# ------------------------------------

# Lanjutkan sisa skrip di halaman utama
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("tutorial gowes 100 km PP untuk pemula")
time.sleep(1) # jeda singkat tetap berguna di sini

search_button = driver.find_element(By.NAME, "btnK")
# Kita coba klik langsung tanpa Keys.ESCAPE dulu
search_button.click()

print(f"Berhasil mengklik tombol cari. Judul halaman sekarang: {driver.title}")

print("Akan menutup browser dalam 10 detik...")
time.sleep(30)

driver.quit()
print("Misi Selesai! Browser sudah ditutup.")