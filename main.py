class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, age=2, height=30, name="Пудж"):
        self.age = age
        self.height = height
        self.name = name
        print('Пудж гавкает')
    def grow(self):
        self.age += 1
        self.height += 5
    def __str__(self):
        return f"{self.name}: {self.age} років, рост {self.height} "
class Cat(Animal):
    def __init__(self,age=1, height=10, name='Фамас'):
        self.age = age
        self.height = height
        self.name = name
        print('Фамас бегает и мяукает')
    def grow(self):
        self.age += 1
        self.height += 5
    def __str__(self):
        return f"{self.name}: {self.age} років, рост {self.height} "
cat = Cat()
dog = Dog()
while True:
    x=input("Натисніть ентер щоб собака так кіт росли")
    dog.grow()
    cat.grow()
    print(dog)
    print(cat)
    if x=="q":
        print("Deleting...")
        break