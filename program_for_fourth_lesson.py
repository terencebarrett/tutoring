
from statistics import mean

# TODO: Allow reentering the student name with a different grade

string_1 = "letter grade:"
string_2 = "F."
string_3 = "D."
string_4 = "C."
string_5 = "B."
string_6 = "A."
string_7 = "*Note: Student needs extra help"
string_8 = "error"

keep_going = True
i = 0
grade_dict = {}
while keep_going:
    i += 1
    # TODO: Clean up input so a quit on either stops immediately and doesn't ask for the second input
    input_grade_str = input(f'Enter grade for student# {i} or "quit" to stop grading: ')
    input_name_str = input(f'Enter name for student# {i} or "quit" to stop grading: ')
    if input_grade_str == 'quit' or input_name_str == 'quit':  # TODO: Use any()?
        keep_going = False
    elif not input_grade_str.isdigit() \
            or input_name_str.isdigit() \
            or int(input_grade_str) > 100 \
            or int(input_grade_str) < 0 \
            or input_name_str in list(grade_dict.keys()):
        print('Incorrect input!')
        i -= 1
    else:
        grade_int = int(input_grade_str)
        if 59 >= grade_int >= 0:
            msg = string_1 + ' ' + string_2 + ' ' + string_7
        elif 69 >= grade_int >= 60:
            msg = string_1 + ' ' + string_3 + ' ' + string_7
        elif 79 >= grade_int >= 70:
            msg = string_1 + ' ' + string_4 + ' ' + string_7
        elif 89 >= grade_int >= 80:
            msg = string_1 + ' ' + string_5
        elif 100 >= grade_int >= 90:
            msg = string_1 + ' ' + string_6
        else:
            msg = string_1 + ' ' + string_8
        print(msg)
        grade_dict[input_name_str] = {'msg': msg, 'number_grade': grade_int}
else:
    print('All done!\n')
    names = list(grade_dict.keys())
    number_grades = []
    for name in names:
        print(name, '\t', 'number grade:', grade_dict[name]['number_grade'], ',', grade_dict[name]['msg'])
        number_grades.append(grade_dict[name]['number_grade'])
    print('The average grade is', round(mean(number_grades)))
