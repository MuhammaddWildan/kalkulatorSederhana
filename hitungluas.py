#def HitungLuas():
	#clearScreen()
def dua():
	print("====TAMBAH====")
	data = int(input("Masukan Data :"))
	dara = int(input("Masukan Data 2 :"))
	hasil = data + dara
	print("Hasilnya Adalah==>",hasil,"<==")
def satu():
	print("====KALI====")
	data = int(input("Masukan Data : "))
	dara = int(input("Masukan Data 2 :"))
	hasil = data * dara
	print("Hasilnya Adalah ==>",hasil,"<==")
def tiga():
	print("====MINUS====")
	data = int(input("Masukan Data :"))
	dara = int(input("Masukan Data 2 :"))
	hasil = data - dara
	print("Hasilnya Adalah==>",hasil,"<==")
def empat():
	print("====SISA BAGI====")
	data = int(input("Masukan Data :"))
	dara = int(input("Masukan Data 2 :"))
	hasil = data % dara
	print("Hasilnya Adalah==>",hasil,"<==")
def nol():
	print("Data Yang Ada Masukan Masih Dalam Perbaikan Kami Para Develover Terima Kasih")	
#MENU

print("--- PROGRAM KALKULATOR SEDERHANA ---")

print("[1]_KALI(×)")
print("[2]_TAMBAH(+)")
print("[3]_MINUS(-)")
print("[4]_SISA PEMBAIAN(÷)")
print("[0]_Tutup")
#Pilih MENU
menu = int(input("Pilih menu : ")) #input nomor menu
import time

print("LOADING")

a = [
       
       '[10%]',
       '[16%]',
       '[20%]',
       '[23%]',
       '[24%]',
       '[36%]',
       '[44%]',
       '[45%]',
       '[49%]',
       '[50%]',
       '[56%]',
       '[58%]',
       '[60%]',
       '[77%]',
       '[78%]',
       '[80%]',
       '[87%]',
       '[89%]',
       '[99%]',
       '[100%]',
]

for i in enumerate(a):
	time.sleep(0.10)
	print(i)
#Cek MENU Pilihan

if menu==1:
    satu()
elif menu==2:
	dua()
elif menu==3:
	tiga()
elif menu==4:
	empat()
elif menu==0:
	nol()
else:
	print("DATA YG ANDA MASUKAN TIDAK ADA DALAM MENU MAAF :(")