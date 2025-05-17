def reversed(name):
    pal = ""
    for char in name:
       pal = char + pal
    return pal 

name_list = []

while True:
    name = input("Enter a word: ")
    if name == "":
        print(name_list)
        break

    while reversed(name) == name and reversed(name) != "":
        print("Yes, " + "'" + name + "'" + " is a palindrome!")
        name_list.append(name)
        break
    if reversed(name) != name:
        print("No, " + "'" + name + "'" + " is not a palindrome.")
