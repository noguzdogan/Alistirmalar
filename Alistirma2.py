# inf değerini standart modülleri kullanarak 'int' tipine dönüştüremediğim gibi
# 'float' tipindeki verileri for döngüsü içine alamadım. Bu yüzden int32'nin max
# değerini baz alarak for döngüsü oluşturdum. Ancak programın daha hızlı son-
# lanabilmesi için bu değeri biraz küçülttüm.

# Biraz uzun sürüyor ama yakın bir sonuç veriyor :)
import math
sol_taraf = 0
for x in range(1,2**26-1):
    sol_taraf += 1/x**2
value_pi = math.sqrt(6*sol_taraf)
print("pi sayısının yaklaşık değeri: ",value_pi)


# sonsuz konusunu derste bana hatırlat lütfen, herkes öğrenmiş olsun
# burada 2** sayısını neden bu rakam aldın anlamadım, gereksiz yere programı yormuşsun. 

# Hocam int'in max değerini baz alıp 2'nin üssünü bir bir azaltayım dedim çünkü değeri
# arttırdıkça pi'nin değeri daha da yakın oluyordu.
