''' Functions
  (1) DEFINE vs CALL
  (2) Parameter vs Argument
  (3) Keyword & Default Arguments
  (4) Scope
'''

print("====== DEFINE (parameter) vs CALL (argument) ======")
# build in function(avvaldan qurilib berilgan) > print() type()
# Function - reusable block of code
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parameter
'''
def greet(a):
  pass # function bo'sh bo'lsa ham albatta pass sintaksi bo'lishi kerak
'''


def greet(a):
    print(f"How do you do, {a}")  # void function (none qiymat qaytaradi)


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - argument
result1 = greet('ALAN')
print("result:", result1)

result2 = greeting("Martin")
print("result2:", result2)

print("====== Keyword & Default arguments ======")

# DEFINE
def give_greet(name, age=22):  # Default argument
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Justin", age=28)  # Keyword argument
print("result3:", result3)

result4 = give_greet(name="Alan")
print("result4:", result4)
