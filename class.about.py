''' CLASS
    (1) What is class
    (2) Ordinary vs static properties
    (3) Special methods
'''

print("===== What is class =====")
# class - blueprint(shablon) for object creation!
# structure -> state   constructor   method

class Person():
  # state
  message = "static state property"

  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # method
  def introduce(self):
    print(f"{self.name} says: How do you do!")

  def say_age(self):
    print(f"{self.name} says: I am {self.age}")

  @classmethod # classmethod dekorator
  def explain(cls):
    print("static method property executed!")


person1 = Person("Alan", 21)
person2 = Person("Martin", 35)
person3 = Person("Justin", 25)

# ordinary state 
name = person1.name
print("person1.name:", name)

# ordinary method
person1.introduce()
person2.say_age()


print("===== Ordinary vs static properties =====")
# static state
new_message = Person.message
print("new_message:", new_message)

# static method -> @classmethod dekoratori orqali quriladi
Person.explain()
