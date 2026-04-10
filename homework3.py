#task 1

movies = ["kungfu_panda", "cars", "bad_guys", "joker", "fight_club"]

print(movies[0])
print(movies[-1])

movies.append("interstellar")
movies.insert(3, "batman")
movies.remove("bad_guys")

print(movies)
print(len(movies))

#task 2

numbers = []

for i in range(5):
    num = int(input(f"number {i+1}: "))
    numbers.append(num)

print("numbers", numbers)
print("maximumi" , max(numbers))
print("minimumi", min(numbers))
print("jami", sum(numbers))
print("sashvalo", sum(numbers) / len(numbers))

#task 3

evens = []
odds = []

for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print("evens", evens)
print("odds", odds)

#task 4

my_password = "password123"

while True:
    password = input("Enter password: ")
    if password == my_password:
        print("paroli sworia")
        break
    else:
        print("wvdoma ar moxerxda")

# კიდე შეიძლება attempts ის გამოყენება არვიცი ახსენით თუ არა attempts = 0 და ბოლოს   
# if attempts == 3: print("Account locked!") break
       
# Task 5

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Task 6

sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

for char in sentence.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)