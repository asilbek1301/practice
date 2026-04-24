''' Tuple
    (1) What is tuple: tuple vs list
    (2) Unpacking arguments
    (3) zip
'''

print("===== What is tuple: tuple vs list =====")
# Java/PHP/NodeJS array => Python list (Python array juda ham spesifik hollarda ishlatiladi)

# literal
numbs = [3, 5, 1, 2]  # LIST (array)
# car_dic = {"brand": "Ferrari", "year": 1995} # OBJECT


# constructor
letter = list("Hello World!")  # LIST (array)
# person_dict = dict(name="Alan", age=21) # OBJECT


fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

print("===== TUPLE =====")
# Tuple ning list dan farqi uning qiymatlarini hech qachon o'zgartirib bo'lmaydi
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
print(tuple_obj[2])
# animals[0] = "bird"
