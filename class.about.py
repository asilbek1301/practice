''' CLASS
    (1) What is class
    (2) Ordinary vs static properties
    (3) special/magic methods
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


print("===== special/magic methods =====")
# Python's most common special methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args): # __new__ special method kopincha ishlatilmaydi
      print("* __new__ *")
      return super().__new__(cls)

    def __init__(self, name, year): # __init__ special method constructor uchun ishlatiladi 
      self.name = name
      self.year = year

    # method
    def start_engine(self):
      print(f"the {self.name} started engine")

    def stop_engine(self):
      print(f"the {self.name} stopped engine")

    def __str__(self): # __str__ special methodi classdan yasalgan objectni print qilganda ishlatiladi
      return f"{self.name} was produced in {self.year} year!" 

    def __call__(self): # __call__ special methodi classdan yasalgan objectni function qilib chaqirganda ishlatiladi
      print("Object called as function!")
      return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("-----")
your_car = Car("Tesla", 2026)
print(your_car) # __str__
response = your_car() # __call__ --> look like function
print("response:", response)
