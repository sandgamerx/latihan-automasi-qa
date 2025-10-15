# conftest.py (di root Latihan_Automasi/)
import sys
import os

# Tambahkan root directory Anda ke Python path
# Ini memungkinkan import seperti 'from MOBILE_PROJECTS.TikTok_App.Pages...'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Di sini Anda bisa menaruh fixture global (misalnya API driver, jika ada)