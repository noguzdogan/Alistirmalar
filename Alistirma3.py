# range 18'den sonrası için hep aynı sonucu verdiği için kısa sürede sonuç
# elde etmek adına range'in durduğu noktayı 18 olarak belirledim
value_exp = 0
def faktoriyel(i):
    if i==0:
        return 1
    else:
        return i * faktoriyel(i-1)
for i in range(0,18):
    value_exp += 1/faktoriyel(i)
print("e sayısının yaklaşık değeri: ",value_exp)
