'''OBJECTS
   (1) What is object
   (2) Iterable objects & RANGE
   (3) DICTIONARY
   (4) Error handling systems
'''

import array  # package/module
import math
from math import ceil, asin  # aynan ceil methodini togridan-togri chaqirish usuli
print("===== What is object =====")
# An object has state and method properties.
# Everything is object in Python!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigms(uslubiyat) -> Functional Programming & OOP
# OOP 4 CONCEPTS -> Abstraction | Encapsulation | Inheritance | Polymorphism
result1 = math.ceil(97.7)  # CALL
print(f"result1: {result1}")

result2 = ceil(98.7) # pachagedan togridan-togri chaqirilgan methodni chaqirish
print("result2:", result2)


print("===== Error handling systems =====")
car_dict = dict(name="Tayota", year=2026, electric=True)

try:
   print("passed here")
   a = car_dict.speed # car_dict ni ichidan speed statini topishga harakat qiladi
   result = car_dict["origin"] # xatolik sodir bo'lsa exceptga yuboradi
   print("result:", result)
except Exception as err:
   print("General Error:", err)
else: # tepadagi hamma mantiq ishga tushsa else execution boladi
   print("Executed successfully without errors")
finally: # xatolik sodir bo'lsa ham har diom ishga tushadi
   print("Final closing logic")

# Exception -> har qanday errorlarni handle qilib beradi