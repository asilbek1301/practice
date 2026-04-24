''' LOOP Operators
    (1) for
    (2) break / else
    (3) while
'''

# belgilangan tarib, belgilangan ketma-ketlik aniq bo'lsa
print("===== for operator =====")
# Iterable objects -> string dict tuple list range map filter
text = "MIT"
numbs = [10, 7, 3, 4]  # List
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)  # [0, 5)

for letter in text:
    print(f"the letter: {letter}")

print("--"*20)

for number in numbs:
    print(f"the number: {number}")

print("--"*20)

for x in range_obj:
    print(f"the element: {x}")

print("--"*20)

for key in car_obj:
    print(f"the element: {key} => value: {car_obj.get(key)}")

print("--"*20)


print("===== for operator =====")  # takrorlanish ketma-ketligini miqdori nomalum bo'lsa
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:  # loop aylanadi, mantiq togri bolsa break ishga tushadi
        print("Reached break")
        break
else:  # for loop da hech qanday break orqali toxtatilishsiz aylansa else ishga tushadi
    print("Looped successfully")


print("===== for operator =====")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the numb equals {numb}")

print("--"*20)
count = 0
while True:
    count += 1
    x = int(input("Find number "))

    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print("Wrong, please find again!")
