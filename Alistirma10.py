toplam = 0
for xs in range(10000,100000):
    x = str(xs)
    if x[0] == x[3] and x[1] == x[4]:
        toplam +=1
print("İlk iki rakamı son iki rakamına eşit olan 5 basamaklı sayıların toplam adedi: ",toplam)
