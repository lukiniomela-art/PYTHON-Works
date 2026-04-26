#task 1

'''
ნუ პირველ რიგში ჩვენ ლისთში უნდა ვიპოვოთ პატარა ციფრი
ნუ ამისათის უნდა დავიწყოთ ლისთის პირველი რიცხვიდან და პირველ
რიცხვს მივიღებთ ყველაზე პატარად ხოლო
შემდეგ თუ ვნახეთ ლისთში ნუ თუ იყო უფრო პატარა ის გახდება ლისთის ყველაზე პატარა
ხოლო ამას გადავწერთ ფუნქციის სახით
უფრო ზუსტად:
1. ავიღოთ სიის პირველი რიცხვი და დავარქვათ მას current_smallest
2. გადავუაროთ სიაში არსებულ ყველა რიცხვს
3. თუ რომელიმე რიცხვი current_smallest-ზე პატარაა, განვაახლოთ current_smallest ამ რიცხვით
4. ყველა რიცხვის შემოწმების შემდეგ დავაბრუნოთ current_smallest


არვიცი ესე სწორედ ვხსნი ვერგავიგე სავით პირობა
იმედია კაია
'''

def current_minimum(numbers):
    current_smallest = numbers[0]
    for number in numbers:
        if number < current_smallest:
            current_smallest = number
    return current_smallest

print(current_minimum([1, 2, 3, 4, 5]))
print(current_minimum([-3, -10, -1, -7]))
print(current_minimum([0, 0, 0, 0, 0]))
print(current_minimum([5]))

#task 2
print(">>> Task 2")

'''
შევქმნათ ცვლადი count და დავაყენოთ 0-ზე
გადავუაროთ სიაში ყველა რიცხვს
თუ რიცხვი ლუწია (number % 2 == 0)
count-ს დავუმატოთ 1
ბოლოს დავაბრუნოთ count


'''

def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 5, 6]))
print(count_even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(count_even([3, 5, 7, 9]))

#task 3

'''
არვიცი რატო მარა
ვერ გავიგე ეს დავალება
და გკითხავთ
'''

#task 4

'''
გავიაროთ ყველა ციფრი სიაში და
თუ სიის რომელიმე ციფრი ტოლია ჩვენი სამიზნე ციფრის
უნდა დავაბრუნოთ სიმართლე ნუ თი არა თუ ვერ ვიპოვეთ ფოლსი


'''

def contains(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False

print(contains([1, 2, 3, 4, 5], 3))
print(contains([1, 2, 3, 4, 5], 6))

#task 5

'''
უნდა შევქმნათ ცვლადი count და დავაყენოთ 0-ზე
შემდეგ გადავაქციოთ text და letter ერთნაირ ფორმატში (lowercase)
შემდეგ გადავუაროთ text-ში არსებულ ყველა სიმბოლოს
თუ სიმბოლო ტოლია letter-ს count-ს დავუმატოთ 1
ბოლოს დავაბრუნოთ count
'''

def count_letters(text, letter):
    count = 0


    text = text.lower()
    letter = letter.lower()


    for char in text:
        if char == letter:
            count += 1
    return count

print(count_letters("hello world", "o"))
print(count_letters("m seria gatrinolebuli", "i"))
print(count_letters("abGuBUBYBbad", "b"))


#task 6

'''
1. შევქმნათ ცარიელი სია result
2. გადავუაროთ ყველა ელემენტს items-ში
3. თუ ელემენტი ჯერ არ არის result-ში:
       დავამატოთ result-ში
4. დავაბრუნოთ result

ასე უსგ უსჯ ს პრინციპით 
ვიპოვით სიაში არსებულ ყველა უნიკალურ ელემენტს 
და კოდი იმ ელემენტს რეზულტში არ გადაიტანს რომელიც
უკვე გვაქ

'''

def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))
print(remove_duplicates(["apple", "banana", "apple", "orange", "banana"]))
print(remove_duplicates([]))