# inf değerini standart modülleri kullanarak 'int' tipine dönüştüremediğim gibi
# 'float' tipindeki verileri for döngüsü içine alamadım.

import math
sol_taraf = 0
for x in range(1,10000):
    sol_taraf += 1/x**2
value_pi = math.sqrt(6*sol_taraf)
print("pi sayısının yaklaşık değeri: ",value_pi)
