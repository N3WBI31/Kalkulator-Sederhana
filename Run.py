#Ini Adalah Program Matematika Sederhana
#Buat Belajar Program Python Sedikit-Sedikit
try:
	import requests as r, os,time
	from colorama import Back,init,Fore
except ModuleNotFoundError:
	exit("Install Module Terlebih Dahulu ! !")
except r.exceptions.ConnectionError:
	exit("Tidak Ada Koneksi Internet !")

#Jika Ingin Menampilkan Ip = r.get("https://api.ipify.org").text
#jika ingin lihat time=time.asctime(time.localtime(time.time()))
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

localtime = time.asctime(time.localtime(time.time()))
os.system("clear")
print (f"{W}[{Y}•{W}] Local Time:{G} {localtime}")

print (Fore.RED+"██   ██  █████  ██      ██   ██ ██    ██ ██       █████  ████████  ██████  ██████  ")
print ("██  ██  ██   ██ ██      ██  ██  ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ ")
print ("█████   ███████ ██      █████   ██    ██ ██      ███████    ██    ██    ██ ██████  ")
print (Fore.WHITE+"██  ██  ██   ██ ██      ██  ██  ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ ")
print ("██   ██ ██   ██ ███████ ██   ██  ██████  ███████ ██   ██    ██     ██████  ██   ██ ")
print ("\t\033[1;95m   ["+Back.WHITE+Fore.BLACK+"Ini Adalah Kalkulator Sederhana Yang Di Buat RelGanz \033[00m"+Fore.RED+"\033[1;95m]\n")

try:
	print (f"{W}Note:{G} Tambahkan Ip Jika Ingin Menggunakan Ip {B}&{G} Koneksi Internet {R}! ! !")
	operator = input(f"{R} (\033[1;96mx,-,/,+{R}) {B}Chose Operator:{G} ")
	angka_1 = float(input(f"{W}Masukkan Angka Pertama:{G} "))
	angka_2 = float(input(f"{W}Masukkan Angka Kedua:{G} "))
except ValueError:
	exit(f"{W}Masukin Yang Bener Kaka {G}(ヾ￣▽￣){W}")
except KeyboardInterrupt:
	exit(f"{W}Program Dihentikan{R} ! !")

#buat run nya
if operator == "x" or operator == "*":
	hasil = angka_1 * angka_2
	print (f"Hasil Perkalian: {hasil}")
if operator == "+":
	hasil = angka_1 + angka_2
	print (f"Hasil Pertambahan: {hasil}")
if operator == "/":
	hasill = angka_1 / angka_2
	print (f"Hasil Pembagian: {hasill}")
if operator == "-":
	hasil = angka_1 - angka_2
	print (f"Hasil Pengurangan: {hasil}")