pilihan = 1
pilihan = 2
pilihan = 3
pilihan = 4
pilihan = 5



print (50*"=")
print ("Terima Kasih Telah Menggunakan Tools Ini :)")
print ("Author: Hilman.4TX")
print ("Jenis Alat: Penghitungan Matematika")
print ("Komunitas: BL4CK.4TX")
print (50*"=")

print ("1.Penjumlahan")
print ("2.Pengurangan")
print ("3.Perkalian")
print ("4.Pembagian")
print ("5.Modulus")

pilihan = input("Pilih Yang Mana : ")
pilihan = int(pilihan)

#Penjumlahan

if (pilihan==1):
  print("Masukkan Input Dengan Benar!")
  tam1 = input("Masukkan Angka Pertama : ")
  tam1 = int(tam1)
  tam2 = input("Masukkan Angka Kedua : ")
  tam2 = int(tam2)
  tasl = tam1 + tam2
  print (tasl)
  
#Akhir Penjumlahan

#Pengurangan

elif(pilihan==2):
  print("Masukkan Input Dengan Benar Ya :)")
  ran1 = input("Masukkan Angka Pertama : ")
  ran1 = int(ran1)
  ran2 = input("Masukkan Angka Kedua : ")
  ran2 = int(ran2)
  ranl = ran1 - ran2
  print (ranl)
  
#Akhir Pengurangan

#Perkalian

elif(pilihan==3):
  print("Silahkan Masukkan Input Yang Benar :) ")
  kal1 = input("Masukkan Angka Pertama : ")
  kal1 = int(kal1)
  kal2 = input("Masukkan Angka Kedua : ")
  kal2 = int(kal2)
  kalh = kal1 * kal2
  print (kalh)

#Akhir Perkalian

#Pembagian

elif(pilihan==4):
  print ("Masukkan Input Yang Benar :)")
  bgi1 = input("Masukkan Angka Pertama : ")
  bgi1 = int(bgi1)
  bgi2 = input("Masukkan Angka Kedua : ")
  bgi2 = int(bgi2)
  bgihsl = bgi1 // bgi2
  print (bgihsl)

#Akhir Pembagian


#Modulus

elif(pilihan==5):
  print("Modulus Adalah Sisa Pembagian :)")
  dul1 = input("Masukkan Angka Pertama : ")
  dul1 = int(dul1)
  dul2 = input("Masukkan Angka Kedua : ")
  dul2 = int(dul2)
  dulhsl = dul1 % dul2
  print (dulhsl)



#Akhir Modulus












