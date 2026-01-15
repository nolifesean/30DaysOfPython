# Day 4: 30 Days of Python Programming

# Exercises Day 4 

# Number 1
string_list = ["Thirty", "Days", "Of", "Python"]
print(" ".join(string_list))

# Number 2
str1 = "Coding"
str2 = "For"
str3 = "All"
space = " "
print(str1 + space + str2 + space + str3)

# Number 3, 4, 5, 6 & 7
company = "Coding For All"
print(company)
print("Length:", len(company))
print("Uppercase:", company.upper())
print("Lowercase:", company.lower())

# number 8
print("Capitalized:", company.capitalize())
print("Title Case:", company.title())
print("Swap Case:", company.swapcase())

# Number 9
print("Sliced: ", company[0:6])

# Number 10
print("Is there Coding in the string?: starts at the", company.find("Coding"), "index")
print("Is there Coding in the string?: starts at the", company.index("Coding"), "index")

# Number 11
print("=====================================================")
print("String:", company)
print("String replaced to 'Python:'", company.replace("Coding For All", "Python"))

# Number 12
print("=====================================================")
string2 = "Python for Everyone"
print("String:", string2)
print("Replaced Everyone for 'All':", string2.replace("Everyone", "All"))

# Number 13
print("=====================================================")
string3 = "Coding For All"
print("String:", string3)
print("Split by space:", string3.split(" "))

# Number 14
print("=====================================================")
big_company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("Companies: ", big_company.split(","))

# Number 15
print("=====================================================")
print("String:", string3)
print("What is the first character?:", string3[0])

# Number 16
print("What is the last index?:", len(string3)-1)

# Number 17
print("What is the character at index 10?:", string3[10])

# Number 18
print("=====================================================")
string4= "Python For Everyone"
print("String:", string4)
print("Acronym/Abbreviation:", string4[0] + string4[7] + string4[-8])

# Number 19
print("=====================================================")
string5 = "Coding For All"
print("String:", string5)
print("Acronym/Abbreviation:", string5[0] + string5[7] + string5[-3])

# Number 20 & 21
print("=====================================================")
print("String:", string5)
print("First Occurence of C at index:", string5.index('C'))
print("First Occurence of F at index:", string5.index('F'))


# Number 22
print("=====================================================")
string6 = "Coding For All People"
print("String:", string6)
print("Last occurence of l at:", string6.rfind('l'))

# Number 23, 24, 25, 26 & 27
print("=====================================================")
statement = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
print("String:", statement)
print("First occurence of the word 'because' at index:", statement.index(sub_string))
print("Last occurence of the word 'because' at index:", statement.rindex(sub_string))
print("Sliced statement:", statement[31:54])
print("Position of the first occurence of 'because':", statement.find(sub_string))
print("Sliced statement:", statement[31:54])

# Number 28 & 29
print("=====================================================")
string7 = "Coding For All"
sub_string2 = "Coding"
print("String:", string7)
print("Does the string start with 'Coding'?:", string7.startswith(sub_string2))
print("Does the string end with 'coding'?:", string7.endswith('coding'))

# Number 30
print("=====================================================")
string8 = '   Coding For All      '
print("String with spaces:", string8, "|")
print("Removed Trailing Left and Right spaces:", string8.strip())

# Number 31
print("=====================================================")
string9 = "30DaysOfPython"
string10 = "thirty_days_of_python"
print("String 1:", string9)
print("String 2:", string10)
print("Is string 1 indentifier?:", string9.isidentifier())
print("Is string 2 indentifier?:", string10.isidentifier())
print("Therefore, string 2 returns True as a valid identifier.")

# Number 32
print("=====================================================")
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']


