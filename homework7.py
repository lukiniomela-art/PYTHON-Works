class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def greet(self):
        
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person1 = person("Alice", 30)
person2 = person("Bob", 25)
person3 = person("givi", 35)

person1.greet()
person2.greet()
person3.greet()

#task 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


rect1 = Rectangle(5, 10)
square1 = Rectangle(4, 4)

print(rect1.area())
print(rect1.perimeter())
print(rect1.is_square())

print(square1.area())
print(square1.perimeter())
print(square1.is_square())

#task 3

class bank_account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("tanxa ar miigeba")


    def withdraw(self, amount):
        if amount > self.balance:
            print("arasakmarisi tanxa")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account({self.owner}): ${self.balance}"
    
accaunt1 = bank_account("Alice", 1000)
print("\n")
accaunt2 = bank_account("davita", 500)

accaunt3 = bank_account("luka", 700)    

print(accaunt1)
print(accaunt2)
print(accaunt3)


#task 4


class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound.")


class dog(animal):
    def speak(self):
        print(self.name + " says Woof!")


class cat(animal):
    def speak(self):
        print(self.name + " says Meow!")


animals = [dog("Rex"), cat("Whiskers"), animal("Bob")]

for a in animals:
    a.speak()



