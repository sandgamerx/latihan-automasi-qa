# test_tiktok_scroll.py
import pytest
import allure
import time
import random
from TikTokHomePage import TikTokHomePage # Impor Page Object baru

@allure.title("Tes Interaksi Berulang di TikTok")
def test_tiktok_scroll_and_like(driver):
    print("\nMenunggu aplikasi TikTok dimuat...")
    time.sleep(5)
    
    home_page = TikTokHomePage(driver)
    screen_size = driver.get_window_size()
    
    # --- Logika untuk Aksi Berulang ---
    
    # 1. Dapatkan ukuran layar HP sekali saja di awal
    screen_size = driver.get_window_size()
    width = screen_size['width']
    height = screen_size['height']
    
    # 2. Tentukan koordinat untuk swipe
    start_x = width // 2
    start_y = int(height * 0.8)
    end_x = width // 2
    end_y = int(height * 0.2)
    
    for i in range(10):
        print(f"\n--- Iterasi ke-{i + 1} ---")
        time.sleep(random.randint(2, 4))
        
        # Ganti double tap dengan klik tombol Like
        home_page.click_like()
        
        time.sleep(1)
        
        print("Melakukan scroll...")
        driver.swipe(start_x, start_y, end_x, end_y, 500)
        
    print("\n--- Selesai melakukan 10x scroll dan like ---")
    time.sleep(5)