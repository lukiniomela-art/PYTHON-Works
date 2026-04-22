#task 1

grades = {
    "luka" : 92,
    "temo" : 76,
    "barbare" : 87,
    "ana_maria" : 49,
    "dato" : 98}


for name, score in grades.items():
    print(f"{name}: {score}")

print(sum(grades.values()) / len(grades))

max_score = max(grades, key=grades.get)

print(f"Highest score: {max_score} with {grades[max_score]}")

#task2 

def count_letters(word):
    word_test = {}
    word = word.lower()

    for i in word:
        if i != " ":
            if i in word_test:
                word_test[i] += 1
            else:
                word_test[i] = 1
    return word_test

print(count_letters("Hello World"))


def merge_lists(list1, list2):
    merged = {}

    for i in list1:
        if i in merged:
            merged[i] += list1[i]
        else:
            merged[i] = list1[i]

    for i in list2:
        if i in merged:
            merged[i] += list2[i]
        else:
            merged[i] = list2[i]

    return merged

print(merge_lists({"milk": 2, "bread": 1, "eggs": 12}, {"bread": 2, "cheese": 1, "milk": 1},  ))
    
def add_contact(contacts, name, phone, email):
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    return contacts
    
def find_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
            
    return None    

def all_emails(contacts):
    emails = []
    for contact in contacts:
        emails.append(contact["email"])
    return emails

contacts = []

add_contact(contacts, "luka", "555-1234", "luka@gmail.com")
add_contact(contacts, "temo", "555-5678", "temo@gmail.com")
add_contact(contacts, "barbare", "555-9999", "barbare@gmail.com")

print(find_contact(contacts, "luka"))
print(all_emails(contacts))