string_1 = "The Student's letter grade:"
string_2 = "F."
string_3 = "D."
string_4 = "C."
string_5 = "B."
string_6 = "A."
string_7 = "*Note: Student needs extra help"
string_8 = "error"

x = 65

if 59 >= x >= 0:
    print(string_1, string_2, string_7)
elif 69 >= x >= 60:
    print(string_1, string_3, string_7)
elif 79 >= x >= 70:
    print(string_1, string_4, string_7)
elif 89 >= x >= 80:
    print (string_1, string_5)
elif 100 >= x >= 90:
    print(string_1, string_6)
else:
    print(string_1, string_8)

