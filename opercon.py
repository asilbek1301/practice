''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("===== Operators =====")
# + - > >= < <= == is * /     // % += **

a = 19
b = 5

result = a // b  # a ni b ga bolganda butun qiymati
left = a % b  # a ni b ga bolganda qoldigi
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print()
print("a:", a)

print("b*b:", b**2)
print("b**b:", b**3)

print("-"*50)
# ==   -> objektlar orasida objectning faqat valularini solishtiradi
c = dict(name="Alan", age=21)
d = dict(name="Alan", age=21)
e = c

print("c==d:", c == d)  # only value
print(id(c), id(d), id(e))

# is   -> reference ni solishtiradi
print("c is d", c is d)
print("c is e", c is e)


print("===== Condition =====")
# Condition lar TRUTHY va FALSY qiymatlarni tekshiradi
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("===== Logical Operators =====")
age = 21

# Simple Condition
# person = None
# if age > 18:
#     person = "Adult"
# else:
#     person = "Child"


# Ternary
person = "adult" if age > 18 else "minor"
print("person:", person)

print("-"*50)

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:  # executes if not student
    print("Welcome here, do you want to be student!")
elif is_admin:
    print("Please go to this office!")
elif is_guest and is_parent:
    print("Waiting room is over there!")
else:
    print("Etc")

# True  or   False   -> True
# True  and  False   -> False
