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


# when making tuples try avoid this
people = "Alan", "John"
animals = "dog",

print("===== Unpacking arguments =====")  # Tuple orqali Argumentlarni yoyish
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups  # *z listdagi qolgan qiymatlarni o'ziga oladi
print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args -> tuple
def calculate(*args):
    print("*args", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("--"*20)
calculate(0, 2, 300)
print("--"*20)
calculate(5, 7)


print("--"*20)
# **kwargs -> dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]}")


# CALL
introduce(name="Alan", age=21)
introduce(name="Martin", age=35, single=False)
