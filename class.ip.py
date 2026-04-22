''' CLASS deep diving
    (1) ENCAPSULATION (getter vs setter)
    (2) INHERITANCE 
    (3) POLYMORPHISM 
'''

print("===== INHERITANCE =====")
# PARENT > CHILD [only provides public & protected properties(state + method)]


class Animal():  # Parent
    description = "This class parent for animals"

    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


class Cat(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "meow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-"*50)
dog.make_voice()
fish.make_voice()

print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)


print("===== POLYMORPHISM =====")  # POLY (bir qancha) + MORPHISM (shakl)

dog.make_voice()
fish.make_voice()

print("-"*50)
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)  # Fish is Child to Animal
data2 = issubclass(Animal, object)  # Animal is Child to object
print("data:", data1, data2)
