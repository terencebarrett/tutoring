string_1 = "The Student's letter grade:"
string_2 = "F."
string_3 = "D."
string_4 = "C."
string_5 = "B."
string_6 = "A."
string_7 = "*Note: Student needs extra help"
string_8 = "error"

x = 77

if x <= 59 and x >= 0:
    print (string_1, string_2, string_7)

if x <= 69 and x >= 60:
    print (string_1, string_3, string_7)

if x <= 79 and x >= 70:
    print (string_1, string_4, string_7)

if x <= 89 and x >= 80:
    print (string_1, string_5)

if x <= 100 and x >= 90:
    print (string_1, string_6)

if x >= 100 or x <= 0:
    print (string_1, string_8)

