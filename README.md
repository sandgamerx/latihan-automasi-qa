Comprehensive QA Automation Practice (Web, API, Mobile)

Welcome to my QA automation practice repository! This project is a collection of test automation frameworks covering the three main pillars of quality assurance: Web (Selenium), API (Requests), and Mobile (Appium). All tests are written in Python using the Pytest framework.

This repository is also configured with GitHub Actions to run tests automatically (CI/CD) and publish test reports using Allure Report.


🚀 Key Features

• Web Automation: Utilizes Selenium to test the Sauce Demo e-commerce website.

• Mobile Automation: Employs Appium to test native Android applications like Calculator, Tokopedia, and TikTok.

• API Automation: Uses the Requests library to test endpoints from Reqres.in.

• Professional Framework: Built with Pytest, implementing the Page Object Model (POM) for clean and maintainable code.

• Interactive Reports: Generates rich and interactive test reports using Allure Report.

• Integrated CI/CD: A GitHub Actions workflow automatically runs Web and API tests on every push to the main branch.

• Modular Project Structure: The code is organized into separate folders for each tested application for easy management.


🛠️ Prerequisites (Environment Setup)

Before running this project on your local machine, ensure you have installed all the necessary software.

1. General Software:

&nbsp; &nbsp; &nbsp; • Python: Version 3.9+.

&nbsp; &nbsp; &nbsp; • Git: For cloning the repository.

&nbsp; &nbsp; &nbsp; • Java JDK: Required by Allure Report. Version 11 or higher is recommended.

&nbsp; &nbsp; &nbsp; • Node.js & NPM: Required to install the Allure Commandline tool.

2. For Web Automation (Selenium):

&nbsp; &nbsp; &nbsp; • Google Chrome: Or another supported browser.

&nbsp; &nbsp; &nbsp; • ChromeDriver: Ensure its version matches your Google Chrome version.

3. For Mobile Automation (Appium):

&nbsp; &nbsp; &nbsp; • Android Studio: For the Android SDK and emulators.

&nbsp; &nbsp; &nbsp; • Appium Server: npm install -g appium

&nbsp; &nbsp; &nbsp; • Appium Inspector: To inspect elements in mobile applications.

&nbsp; &nbsp; &nbsp; • Appium Drivers: appium driver install uiautomator2

🏃‍♂️ How to Run Tests Locally

1. Clone the Repository

Bash

    git clone https://github.com/sandgamerx/latihan-automasi-qa.git
    cd latihan-automasi-qa

2. Create and Activate a Virtual Environment (venv)

This will isolate the project's Python libraries.

PowerShell

    # Create the venv
    python -m venv .venv

    # Activate on PowerShell
    . \.venv\Scripts\activate

    # Or activate on Git Bash
    source ./.venv/Scripts/activate

3. Install All Required Libraries

Bash

    pip install -r requirements.txt

4. Running Specific Tests

You can run tests for each module separately. Ensure you are in the root project folder (latihan-automasi-qa).

Running Web Tests (SauceDemo):

Bash

    pytest WEB_PROJECTS/SauceDemo/
  
Running API Tests:

Bash

    pytest API/
  
Running Mobile Tests (Example: TikTok):

  &nbsp; &nbsp; &nbsp; • Ensure the Appium Server is running in a separate terminal (appium).

  &nbsp; &nbsp; &nbsp; • Ensure your physical device or emulator is connected.

 &nbsp; &nbsp; &nbsp;  • Update the conftest.py file inside the application's folder with your device UDID.

Bash

    pytest MOBILE_PROJECTS/TikTok_App/

📊 Generating Allure Reports

Allure provides a very detailed visualization of the test results.

1. Run Tests and Collect Data
Add the --alluredir flag when running pytest.

Bash

    # Example for all tests
    pytest --alluredir=allure-results

    # Example for web tests only
    pytest WEB_PROJECTS/SauceDemo/ --alluredir=allure-results

2. Serve the Report in a Browser

Use the allure commandline to serve the report from the collected data.

Bash

    allure serve allure-results

This will automatically open the report in your default browser.

☁️ CI/CD Integration with GitHub Actions

Automatic Execution: Every push to the main branch automatically triggers the workflow defined in .github/workflows/run-tests.yml.

Online Reports: After the workflow completes, the latest Allure report is automatically published to GitHub Pages. You can view it at: https://sandgamerx.github.io/latihan-automasi-qa/.

Thank you for visiting my learning project!

===================================================================

Latihan Automasi QA Lengkap (Web, API, Mobile)

Selamat datang di repositori latihan automasi QA saya! Proyek ini adalah kumpulan framework automasi pengujian yang mencakup tiga pilar utama: Web (Selenium), API (Requests), dan Mobile (Appium). Semua tes ditulis menggunakan Python dengan framework Pytest.

Repositori ini juga dikonfigurasi dengan GitHub Actions untuk menjalankan tes secara otomatis (CI/CD) dan mempublikasikan laporan tes menggunakan Allure Report.

🚀 Fitur Utama

• Automasi Web: Menggunakan Selenium untuk menguji situs web e-commerce Sauce Demo.

• Automasi Mobile: Menggunakan Appium untuk menguji aplikasi Android native seperti Kalkulator, Tokopedia, dan TikTok.

• Automasi API: Menggunakan library Requests untuk menguji endpoint dari Reqres.in.

• Framework Profesional: Dibangun dengan Pytest, menerapkan Page Object Model (POM) untuk kerapian kode.

• Laporan Interaktif: Menghasilkan laporan tes yang kaya dan interaktif menggunakan Allure Report.

• CI/CD Terintegrasi: Workflow GitHub Actions secara otomatis menjalankan tes Web dan API setiap kali ada push ke branch main.

• Struktur Proyek Modular: Kode diorganisir ke dalam folder terpisah untuk setiap aplikasi yang diuji agar mudah dikelola.

🛠️ Prasyarat (Setup Lingkungan)

Sebelum menjalankan proyek ini di mesin lokal Anda, pastikan Anda telah menginstal semua perangkat lunak yang diperlukan.

1. Perangkat Lunak Umum:

&nbsp; &nbsp; &nbsp; • Python: Versi 3.9+.

&nbsp; &nbsp; &nbsp; • Git: Untuk mengkloning repositori.

&nbsp; &nbsp; &nbsp; • Java JDK: Diperlukan oleh Allure Report. Versi 11 atau lebih tinggi direkomendasikan.

&nbsp; &nbsp; &nbsp; • Node.js & NPM: Diperlukan untuk menginstal Allure Commandline.

2. Untuk Automasi Web (Selenium):

&nbsp; &nbsp; &nbsp; • Google Chrome: Atau browser lain yang didukung.

&nbsp; &nbsp; &nbsp; • ChromeDriver: Pastikan versinya sesuai dengan versi Google Chrome Anda.

3. Untuk Automasi Mobile (Appium):

&nbsp; &nbsp; &nbsp; • Android Studio: Untuk Android SDK dan emulator.

&nbsp; &nbsp; &nbsp; • Appium Server: npm install -g appium

&nbsp; &nbsp; &nbsp; • Appium Inspector: Untuk menginspeksi elemen di aplikasi mobile.

&nbsp; &nbsp; &nbsp; • Appium Drivers: appium driver install uiautomator2

🏃‍♂️ Cara Menjalankan Tes Secara Lokal

&nbsp; &nbsp; &nbsp; 1. Kloning Repositori

Bash

    git clone https://github.com/sandgamerx/latihan-automasi-qa.git
    cd latihan-automasi-qa
    
2. Buat dan Aktifkan Lingkungan Virtual (venv)

Ini akan mengisolasi library Python proyek Anda.

PowerShell

    # Buat venv
    python -m venv .venv

    # Aktifkan di PowerShell
    . \.venv\Scripts\activate

    # Atau aktifkan di Git Bash
    source ./.venv/Scripts/activate
    
3. Instal Semua Library yang Dibutuhkan

Bash

    pip install -r requirements.txt
    
4. Menjalankan Tes Spesifik

Anda dapat menjalankan tes untuk setiap modul secara terpisah. Pastikan Anda berada di root folder (latihan-automasi-qa).

Menjalankan Tes Web (SauceDemo):

Bash

    pytest WEB_PROJECTS/SauceDemo/

Menjalankan Tes API:

Bash

    pytest API/

Menjalankan Tes Mobile (Contoh: TikTok):

&nbsp; &nbsp; &nbsp; • Pastikan Appium Server berjalan di terminal terpisah (appium).

&nbsp; &nbsp; &nbsp; • Pastikan HP fisik atau emulator Anda terhubung.

&nbsp; &nbsp; &nbsp; • Perbarui conftest.py di dalam folder aplikasi dengan UDID perangkat Anda.

Bash

    pytest MOBILE_PROJECTS/TikTok_App/
    
📊 Menghasilkan Laporan Allure

Laporan Allure memberikan visualisasi hasil tes yang sangat detail.

1. Jalankan Tes dan Kumpulkan Data

Tambahkan flag --alluredir saat menjalankan pytest.

Bash

    # Contoh untuk semua tes
    pytest --alluredir=allure-results

    # Contoh untuk tes web saja
    pytest WEB_PROJECTS/SauceDemo/ --alluredir=allure-results
    
2. Tampilkan Laporan di Browser

Gunakan allure commandline untuk menyajikan laporan dari data yang terkumpul.

Bash

    allure serve allure-results

Ini akan secara otomatis membuka laporan di browser Anda.

☁️ Integrasi CI/CD dengan GitHub Actions

Eksekusi Otomatis: Setiap push ke branch main akan secara otomatis memicu workflow yang didefinisikan di .github/workflows/run-tests.yml.

Laporan Online: Setelah workflow selesai, laporan Allure terbaru secara otomatis dipublikasikan ke GitHub Pages. Anda dapat melihatnya di: https://sandgamerx.github.io/latihan-automasi-qa/.

Terima kasih telah mengunjungi proyek belajar saya!
