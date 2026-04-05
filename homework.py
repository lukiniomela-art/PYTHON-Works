#1 task

name = input("What is your name? ")
print("Hello, " + name.upper())
print("hello, " + name.lower())
print("hello, " + name.title())

#2 task 

sentence = " the quick brown fox jumps over the lazy dog "

print(sentence.strip())
print(sentence.count("o"))
print(sentence.replace("fox", "cat"))

word = sentence.split()
print(word[:3])

#3 task

age = int(input("How old are you? "))

if age < 0:
    print("Invalid age!")
elif age < 13:
    print("You are a child.")
elif age >= 13 and age <= 17:
    print("You are a teenager.")
elif age >= 18 and age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")

#4 task

username = input("username: ")  
password = input("password: ")  

if username == "admin" and password == "secret":
    print("welcome admin")
elif username == "admin":
    print("wrong password")
else:
    print("user not found")

#task 5

age = int(input("How old are you? "))
student = input("Are you a student? (yes/no) ")
if age < 12:
    print("ticket price: $5")
elif age >= 12 and age <= 18 and student == "yes":    
    print("ticket price: $8")
elif age > 18 and age <= 64:
    print("ticket price: $15")
elif age >= 65:
    print("ticket price: $10")


#imedia esaa davaleba cota davikarge failebshi ;)