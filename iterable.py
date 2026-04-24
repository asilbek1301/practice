print("===== Iterable objects & RANGE =====")
# Iterable objects(takrorlanish xususiyatiga ega objectlar) -> string dict tuple list range map filter

range_obj = range(3) # [0, 3)
print("range_obj:", range_obj)
text = "MIT"
for letter in text:
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")

print("===== DICTIONARY =====")
# Dictionary is JSON object!
person = {"name": "Alan", "age": 21, "single": True} # togridan-togri hosil qilish
person_obj = dict(name="Alan", age=21, single=True) #dict functioni orqali hosil qilish
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# method: get()
# name = person_obj["name"] # objectning keyini togridan-togri olish
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0) # objectda get methodidan chaqirilgan key yoq bolsa 0ni oladi
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"] # objectdan single stateni ochirib beradi
for key in person_obj:
    print(f"the key: {key} => value {person_obj.get(key)}")
