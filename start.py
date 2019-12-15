#plis, jangan di recode sebelum minta izin pada author :)
#from bukittinggi, sumatera barat :)
import os
import sys
import time

try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
except:
    print('Anda belum menginstall selenium, install dengan command "pip2 install selenium" terlebih dahulu!')
    while True:
        install = raw_input('apakah anda ingin menginstall package yang diperlukan? [Y/n] ')
        install.upper()
        if install == 'Y':
            print('Menginstall selenium!')
            os.system('pip2 install selenium')
            os.system('exit')
            break
        elif install == 'N':
            print('Keluar dalam 3 detik!')
            time.sleep(3)
            os.system(exit)
        else:
            print('Masukkan pilihan yang benar!')

driver = None
loginn = 0
Os = None
postingan = None

def system_operasi():
    global Os
    print('''OS yang sedang anda pakai:
1. Windows
2. Kali linux
3. Mac \n''')
    while True:
        Os = input('Pilih salah satu: ')
        if Os == 1:
            os.system('color')
            break
        elif Os == 2:
            break
        else:
            print('Masukkan Pilihan Yang benar!')

def clear():
    if Os == 2 or Os == 3:
        os.system('clear')
    else:
        os.system('cls')

def driverr():
    global driver
    while True:
        clear()
        cover()
        PATH = raw_input('Lokasi file driver: ') 
        try:
            open(PATH, 'r')
            break
        except:
            print('Driver tidak ditemukan! harap masukkan alamat file yang benar! [cth: C:\Users\LENOVO\Downloads\geckodriver.exe]')
            time.sleep(5)
    while True:
        clear()
        cover()
        print('''Tipe driver yang anda gunakan:
1. Firefox (geckodriver)
2. Chrome (chromedriver)
3. Edge (microsoft-edge)
4. Safari\n''') 
        driveer = input('Pilih salah satu: ')
        if driveer == 1:
            jenis = webdriver.Firefox
            break
        elif driveer == 2:
            jenis = webdriver.Chrome
            break
        elif driveer == 3:
            jenis = webdriver.Edge
            break
        elif driveer == 4:
            jenis = webdriver.Safari
            break
        else:
            print('Masukkan pilihan yang benar! ')
            time.sleep(3)
    cover()
    print('Membuka webdriver, harap tunggu!')
    driver = jenis(executable_path=PATH)

def buka(x):
    try:
        driver.get(x)
    except:
        print('Tidak ada koneksi internet!!')
        while True:
            time.sleep(5)
            return buka(x)

def cari(x, y):
    if y == 'id':
        return driver.find_element_by_id(x)
    elif y == 'class':
        return driver.find_element_by_class_name(x)
    elif y == 'text':
        return driver.find_element_by_link_text(x)
    else:
        return driver.find_element_by_name(x)
        
def ketik(x, y):
    return x.send_keys(y)

def ke_menu():
    while True:
        clear()
        menu = raw_input('Apakah anda ingin kembali ke menu utama? [Y/n] ')
        menu.upper()
        if menu == 'Y':
            os.system('clear')
            menu()
            break
        elif menu == 'N':
            print('Keluar dalam waktu 3 detik!')
            time.sleep(3)
            sys.exit()
        else:
            print('Masukkan pilihan yang benar!')

def login():
    global loginn
    cover()
    emai_l = raw_input("Email Anda: ")
    passwor_d = raw_input("Password: ")
    print('Login ke facebook!')
    buka('https://mbasic.facebook.com')
    email = cari('email', 'name')
    ketik(email, emai_l)
    password = cari('pass', 'name')
    ketik(password, passwor_d)
    cari('login', 'name').click()
    url = driver.current_url
    if 'save-device' in url:
        loginn += 1
    elif 'checkpoint' in url:
        print("Akun anda terkena sesi, harap ikuti petunjuk di layar untuk membuka akun anda kembali")
        time.sleep(2)
        print("Keluar dalam 3 detik!")
        time.sleep(3)
        sys.exit()
    else:
	print("Email/Password anda salah\n")
	return login()
        
def chat():
    id_group = raw_input('Masukkan ID group: ')
    isi = raw_input('Tulis Pesan: ')
    buka('https://m.facebook.com/browse/group/members/?id=' + id_group + '&start=0&listType=list_nonfriend_nonadmin&refid=18&ref=dbl')
    jumlah = len(driver.find_elements_by_class_name('bn'))
    member = 0
    berhasil = 0
    gagal = 0
    halaman = 1
    while (member <= jumlah):
        url = driver.current_url
        nyari = driver.find_elements_by_class_name('bn')
        href = nyari[0].get_attribute('href')  # >>> None
        if href == None:
            nyari = driver.find_elements_by_class_name('bl')
        try:
            nyari[member].click()
        except:
            gagal += 1
            member += 1
            if member >= jumlah:
                halaman += 1
                try:
                    cari('Lihat Selengkapnya', 'text').click()
                except:
                    print('Selesai! chat terkirim = ' + str(berhasil) + ' , gagal = ' + str(gagal))
                member -= jumlah
                jumlah -= jumlah
                jumlah += len(driver.find_elements_by_class_name('bl'))
            continue
        nama = driver.title
        button = driver.find_elements_by_link_text('Pesan') #add, pesan, lainnya
        if len(button) == 0:
            member += 1
            gagal += 1
            buka(url)
            if member >= jumlah:
                halaman += 1
                try:
                    cari('Lihat Selengkapnya', 'text').click()
                except:
                    print('Selesai! chat terkirim = ' + str(berhasil) + ' , gagal = ' + str(gagal))
                member -= jumlah
                jumlah -= jumlah
                jumlah += len(driver.find_elements_by_class_name('bl'))
            continue
        if len(button) == 2:
            button[1].click()
        elif len(button) == 1:
            link = button[0].get_attribute('href')
            if 'thread' in link:
                button[0].click()
            else:
                buka(url)
                gagal += 1
                member += 1
                if member >= jumlah:
            	    halaman += 1
            	    try:
                        cari('Lihat Selengkapnya', 'text').click()
            	    except:
                        print('Selesai! chat terkirim = ' + str(berhasil) + ' , gagal = ' + str(gagal))
            	    member -= jumlah
            	    jumlah -= jumlah
            	    jumlah += len(driver.find_elements_by_class_name('bl'))
                continue
        else:
            member += 1
            gagal += 1
            buka(url)
            if member >= jumlah:
                halaman += 1
                try:
                    cari('Lihat Selengkapnya', 'text').click()
                except:
                    print('Selesai! chat terkirim = ' + str(berhasil) + ' , gagal = ' + str(gagal))
                member -= jumlah
                jumlah -= jumlah
                jumlah += len(driver.find_elements_by_class_name('bl'))
            continue

        pesan = cari('body', 'name')
        ketik(pesan, isi)
        try:
            cari('Send', 'name').click()
        except:
            cari('send', 'name').click()
        member += 1
        berhasil += 1
        if member <= jumlah:
            buka(url)
        if member >= jumlah:
            halaman += 1
            try:
                cari('Lihat Selengkapnya', 'text').click()
            except:
                print('Selesai! chat terkirim = ' + str(berhasil) + ' , gagal = ' + str(gagal))
            member -= jumlah
            jumlah -= jumlah
            jumlah += len(driver.find_elements_by_class_name('bl'))

def post_group():
    buka('https://m.facebook.com/groups/?seemore')
    jumlah_tag = len(driver.find_elements_by_tag_name('a'))
    nomor_element = 0
    gagal = 0
    berhasil = 0
    while (nomor_element <= jumlah_tag):
        url = driver.current_url
        tag_a = driver.find_elements_by_tag_name('a')
        href = tag_a[nomor_element].get_attribute('class')
        filter = tag_a[nomor_element].get_attribute('tabindex')
        if href == '' and filter == None:
            tag_a[nomor_element].click()
            nama = driver.title
            try:
                post = cari('u_0_0', 'id')
            except:
                print('Wall group ' + nama + ' ditutup, tidak dapat mengirim post!')
                nomor_element += 1
                gagal += 1
                buka(url)
                continue
            ketik(post, postingan)
            cari('view_post', 'name').click()
            nomor_element += 1
            berhasil += 1
            buka(url)
        else:
            nomor_element += 1
        if nomor_element >= jumlah_tag:
            print('Selesai')
            ke_menu()

def cover():
    clear()
    print(
    """
                      ,--.    ,--.
                     ((O ))--((O ))
                   ,'_`--'____`--'_`.
                  _:  ____________  :_
                 | | ||::::::::::|| | |
                 | | ||::::::::::|| | |
                 | | ||::::::::::|| | | 
                 |_| |/__________\| |_|
                   |________________|
                __..-'            `-..__
             .-| : .----------------. : |-.
           ,\ || | |\______________/| | || /.
          /`.\:| | ||  __  __  __  || | |;/,'\   
         :`-._\;.| || '--''--''--' || |,:/_.-':
         |    :  | || .----------. || |  :    |
         |    |  | || '----SSt---' || |  |    |
         |    |  | ||   _   _   _  || |  |    |
         :,--.;  | ||  (_) (_) (_) || |  :,--.;
         (`-'|)  | ||______________|| |  (|`-')
          `--'   | |/______________\| |   `--'
                 |____________________|
                  `.________________,'
                   (_______)(_______)
                   (_______)(_______)
                   (_______)(_______)
                   (_______)(_______)
                  |        ||        |
                  '--------''--------'

	Facebook: Aurora Maisya Putri
	Email: Ardorianda266@gmail.com
	From: Bukittinggi, Sumatera Barat

	If you want to recode, please contact me first:)
    """)

    print('''
    ________________________________________     __________  __   ______________________________ 
    __  ____/_  __ \__  __ \__  ____/__  __ \    ___  __ ) \/ /   ___    |__  __ \__  __ \_  __ \ 
    _  /    _  / / /_  / / /_  __/  __  / / /    __  __  |_  /    __  /| |_  /_/ /_  / / /  / / /
    / /___  / /_/ /_  /_/ /_  /___  _  /_/ /     _  /_/ /_  /     _  ___ |  _, _/_  /_/ // /_/ / 
    \____/  \____/ /_____/ /_____/  /_____/      /_____/ /_/      /_/  |_/_/ |_| /_____/ \____/  
    ''')

def menu():
    if loginn == 0:
        login()
    cover()
    print('''
Pilih salah satu:
1. Kirim Chat ke semua member group
2. Post ke semua group dimana anda telah bergabung ''')

    while True:
        pilih = input('Masukkan pilihan: ')
        if pilih == 1:
            chat()
            break
        elif pilih == 2:
	    global postingan
	    postingan = raw_input('Tuliis Postingan: ')
            post_group()
            break
        else:
            print('Masukkan pilihan yang benar! ')

system_operasi()

driverr()
menu()
