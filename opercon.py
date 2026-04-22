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
