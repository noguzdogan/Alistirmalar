total = 0
print("İlk iki rakamı son rakama eşit olan 3 basamaklı sayılar:\n")
for x in range(100,999):
    iyi_uyu = str(x)
    ilk = iyi_uyu[0]
    orta = iyi_uyu[1]
    son = iyi_uyu[2]
    inttop = int(ilk) + int(orta)
    if (inttop == int(son)):
        print(x,end="\t")
        total += 1
print("\nBu kurala uyan 3 basamaklı sayıların toplam adedi: ",total)
