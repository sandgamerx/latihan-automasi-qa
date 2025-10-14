from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import sys

# ======================================================
# KONFIGURASI APP & DEVICE
# ======================================================
capabilities = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "udid": "RR8NA0BFQNW",  # pastikan sama dengan adb devices
    "appPackage": "com.tokopedia.tkpd",
    "appActivity": "com.tokopedia.navigation.presentation.activity.MainParentActivity",
    "noReset": True
}

options = UiAutomator2Options().load_capabilities(capabilities)

# ✅ Gunakan endpoint lengkap /wd/hub
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
wait = WebDriverWait(driver, 15)

# ======================================================
# FUNGSI PENCARIAN
# ======================================================
def search_tokopedia(keyword):
    try:
        print(f"🔍 Mencari: {keyword}")

        # Klik kolom pencarian di halaman utama
        search_icon = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.tokopedia.tkpd:id/search_text_home"))
        )
        search_icon.click()

        # Input keyword di kolom search (ID baru)
        search_input = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.tokopedia.tkpd:id/et_search"))
        )
        search_input.send_keys(keyword)

        # Tekan enter (KEYCODE 66)
        driver.press_keycode(66)

        # Tunggu hasil muncul
        time.sleep(5)

        # Ambil nama produk dari hasil pencarian
        products = driver.find_elements(AppiumBy.ID, "com.tokopedia.tkpd:id/product_name")

        if not products:
            print(f"⚠️ Tidak ada hasil yang ditemukan untuk: {keyword}")
        else:
            print(f"\n✅ Hasil pencarian untuk '{keyword}':")
            for p in products[:5]:
                print("-", p.text)

    except (TimeoutException, NoSuchElementException) as e:
        print("❌ Gagal menemukan elemen:", e)

    finally:
        driver.quit()

# ======================================================
# MAIN EXECUTION
# ======================================================
if __name__ == "__main__":
    if len(sys.argv) > 1:
        keyword = " ".join(sys.argv[1:])
    else:
        keyword = "sepeda lipat"

    search_tokopedia(keyword)
