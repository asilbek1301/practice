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
