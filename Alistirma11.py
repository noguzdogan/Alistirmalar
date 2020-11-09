liste = []
for x in range(1,125): #350'den büyük herhangi bir sayı için kalan her zaman 350 olduğu için ben burada 125'i baz alarak işlem yapamanın uygun olduğunu düşündüm.
    # k1,k2 ve k3 kalanları temsil ediyor.
    k1 = 125 % x
    k2 = 200 % x
    k3 = 350 % x
    if k1 == k3 and k2 == k3 and k1 == k3:
        liste.append(k1)
        enbuyuk = x
liste.sort(reverse = True)
print("En büyük kalan: ",liste[0],"\nEn büyük kalanı veren X sayısı: ",enbuyuk)
