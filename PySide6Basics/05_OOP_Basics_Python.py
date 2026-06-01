# Laptop
class Laptop():
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def show_specs(self):
        print("\nBrand :", self.brand, "\nRAM :", self.ram, " GB",sep='')

lap1 = Laptop("Lenovo", 8)
lap2 = Laptop("Asus", 12)

lap2.show_specs()


# Book
class Book():
    def read(self):
        print("reading")

a = Book()
a.read()

# Introduce Person

class Person():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def intro(self):
        print("\nHi I am ", self.name, "\nI am ", self.age, " years old", "\nI'm from ",self.city, sep='')

labh = Person("Labhesh", 23, "Jalgaon")

labh.intro()
