for xs in range(10,1000): # Rakamları toplamı 9'dan büyük olan tek basamaklı rakam yok. O yüzden 10'dan başlattım.
    x = str(xs)
    if xs < 100:
        s1 = int(x[0])
        s2 = int(x[1])
        toplam = s1 + s2
        if toplam > 9:
            print(x,end=" ")
    if 100 < xs and xs < 1000:
        s1 = int(x[0])
        s2 = int(x[1])
        s3 = int(x[2])
        toplam = s1 + s2 + s3
        if toplam > 9:
            print(xs,end=" ")
