
## Section 9 — Dictionaries

# 1. Create a dictionary representing a person with keys name, age, and city. Print the person's name and city.
# 2. Add a new key email to the dictionary, then update the age, then print the whole dictionary.
# 3. Loop through the dictionary and print each key with its value in the format key: value.
# 4. Create a dictionary that maps 3 country names to their capitals. Ask the user for a country and print its capital (handle the case where the country is not found). 

# 1. Create Dictionary
 

person = {
    "name": "Moaiz",
    "age": 24,
    "city": "Lahore"
}

print("Name:", person["name"])
print("City:", person["city"])


 
# 2. Add and Update
 

person["email"] = "moaiz@example.com"
person["age"] = 25

print("\nUpdated Dictionary:")
print(person)


 
# 3. Loop Through Dictionary
 

print("\nDictionary Contents:")

for key, value in person.items():
    print(key,":", value)


 
# 4. Country Capitals
 

capitals = {
    "Pakistan": "Islamabad",
    "India": "New Delhi",
    "Japan": "Tokyo"
}

country = input("\nEnter a country: ")

if country in capitals:
    print("Capital:", capitals[country])
else:
    print("Country not found.")