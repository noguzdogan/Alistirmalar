toplam = 0
for xs in range(100,1000):
    x = str(xs)
    if x[0] != x[1] and x[1] != x[2] and x[0] != x[2]:
        toplam = toplam
    else:
        print(x,end=" ")
        toplam+=1
print("\nŞartları sağlayan toplam sayı adedi: ",toplam)
    
