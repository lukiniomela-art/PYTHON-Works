def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("John"))
print(greet("luka", "dilamshvidobis"))
print(greet("mari", greeting="gamarjoba"))

#task 2

PI = 3.14159

def circle_area(radius):
    return PI * radius * radius

def circle_circumference(radius):
    return 2 * PI * radius

def circle_info(radius):
    area = circle_area(radius)
    circumference = circle_circumference(radius)
    return area, circumference

area, circumference = circle_info(5)
print(area)
print(circumference)

#task 3

def list_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    smallest = min(numbers)
    largest = max(numbers)
    return total, average, smallest, largest

total, average, smallest, largest = list_stats([10, 25, 3, 47, 18, 32, 6])
print(total)
print(average)
print(smallest)
print(largest)


#task 4
print("task 4")
def count_words(sentence):
    words = sentence.split()
    word_count = len(words)
    char_count = len(sentence.replace(" ", ""))
    longest = max(words, key=len)
    return word_count, char_count, longest

word_count, char_count, longest = count_words("the quick brown fox jumps over the lazy dog")

print(word_count)
print(char_count)
print(longest)


print("task 5")

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def class_report(grades):
    for score in grades:
        grade = letter_grade(score)
        print(f"Score: {score} -> Grade: {grade}")
    
    average = sum(grades) / len(grades)
    print(f"Class average: {average}")

class_report([92, 85, 67, 74, 55, 91, 80])


#task 6


import random

def generate_password(length=12, use_digits=True, use_uppercase=True):
    chars = "abcdefghijklmnopqrstuvwxyz"
    
    if use_uppercase:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if use_digits:
        chars += "0123456789"
    
    password = ""
    for i in range(length):
        password += random.choice(chars)
    
    return password

print(generate_password())
print(generate_password(8))
print(generate_password(16, use_digits=False))