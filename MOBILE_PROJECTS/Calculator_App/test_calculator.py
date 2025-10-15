import time
from appium import webdriver
# Impor kelas Options yang baru
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# LANGKAH 1: Siapkan Desired Capabilities (CARA MODERN)
# Buat objek dari kelas UiAutomator2Options
appium_options = UiAutomator2Options()

# Setel capabilities sebagai atribut dari objek, bukan dictionary
appium_options.platform_name = "Android"
appium_options.device_name = "Pixel 8"
appium_options.app_package = "com.google.android.calculator"
appium_options.app_activity = "com.android.calculator2.Calculator"
# appium_options.automation_name tidak perlu lagi karena sudah jelas dari nama kelasnya

# LANGKAH 2: Hubungkan ke Appium Server
# Masukkan objek 'options' ke parameter 'options'
driver = webdriver.Remote("http://localhost:4723", options=appium_options)
print("Berhasil terhubung ke emulator dan membuka Kalkulator.")

# ...sisa kode tidak perlu diubah...
time.sleep(3)

digit_2 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2")
plus_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "plus")
digit_3 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_3")
equals_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals")

digit_2.click()
plus_button.click()
digit_3.click()
equals_button.click()
print("Berhasil menekan 2 + 3 =")

time.sleep(2)

result_element = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final")
hasil = result_element.text

assert hasil == "5"
print(f"Verifikasi Berhasil: Hasilnya adalah {hasil}")
print("--- TEST PASSED ---")

time.sleep(3)
driver.quit()
print("Sesi selesai.")