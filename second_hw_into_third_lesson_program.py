string_1 = "The Student's letter grade:"
string_2 = "F."
string_3 = "D."
string_4 = "C."
string_5 = "B."
string_6 = "A."
string_7 = "*Note: Student needs extra help"
string_8 = "error"

keep_going = True
i = 0
while keep_going:
    i += 1
    input_str = input(f'Enter grade for student# {i} or "quit" to stop grading: ')
    if input_str == 'quit':
        keep_going = False
    elif not input_str.isdigit():
        print('Incorrect input!')
        i -= 1
    else:
        grade_int = int(input_str)
        if 59 >= grade_int >= 0:
            print(string_1, string_2, string_7)
        elif 69 >= grade_int >= 60:
            print(string_1, string_3, string_7)
        elif 79 >= grade_int >= 70:
            print(string_1, string_4, string_7)
        elif 89 >= grade_int >= 80:
            print(string_1, string_5)
        elif 100 >= grade_int >= 90:
            print(string_1, string_6)
        else:
            print(string_1, string_8)
else:
    print('All done!\n')

