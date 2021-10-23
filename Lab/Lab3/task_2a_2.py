def pig_latin(string):
    string = string.split(" ")
    vowels = ['a','e','i','o','u']
    for i in range(len(string)):
        if string[i][0].lower() in vowels:
            string[i] += "hay"
        else:
            string[i] += f"{string[i][0]}ay"
            string[i].replace(string[i][0], "")
    return string


string = input("Enter Sentance: ")
updated = pig_latin(string)
print(updated)