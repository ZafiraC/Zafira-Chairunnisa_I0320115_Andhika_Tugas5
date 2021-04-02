# SOAL NO 2
nama = input("Masukkan nama anda: ")
nilai = int(input("Masukkan nilai anda: "))
if nilai >= 85 and nilai <= 100:
    print('Halo'+','+str(nama)+'!'+' '+'Nilai anda setelah dikonversi adalah A')
elif nilai >= 80 and nilai < 85:
    print('Halo'+','+str(nama)+'!'+' '+'Nilai anda setelah dikonversi adalah A-')
elif nilai >= 75 and nilai < 80:
    print('Halo'+','+str(nama)+'!'+' '+'Nilai anda setelah dikonversi adalah B+')
elif nilai >= 70 and nilai < 75:
    print('Halo'+','+str(nama)+'!'+' '+'Nilai anda setelah dikonversi adalah B')
elif nilai >= 65 and nilai < 70:
    print('Halo'+','+str(nama)+'!'+' '+'Nilai anda setelah dikonversi adalah C+')
elif nilai >= 60 and nilai < 65:
    print('Halo'+','+str(nama)+'!'+' '+'Nilai anda setelah dikonversi adalah C')
elif nilai < 60:
    print('Halo'+','+str(nama)+'!'+' '+'Nilai anda setelah dikonversi adalah E')
print()