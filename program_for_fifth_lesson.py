
from statistics import mean

import matplotlib.pyplot as plt

from src.utilities import msg_from_number_grade


# TODO: Allow reentering the student name with a different grade


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
        msg = msg_from_number_grade(grade_int, is_student=True)
        print(msg)
        grade_dict[input_name_str] = {'msg': msg, 'number_grade': grade_int}
else:
    print('All done!\n')
    names = list(grade_dict.keys())
    number_grades = []
    for name in names:
        print(name, '\t', 'number grade:', grade_dict[name]['number_grade'], ',', grade_dict[name]['msg'])
        number_grades.append(grade_dict[name]['number_grade'])
    average_grade = round(mean(number_grades))
    print('The average grade is', average_grade, ',', msg_from_number_grade(average_grade, is_student=False))

# Plot the student grades
fig_1 = plt.figure()
plt.plot(names, number_grades, 'bd', label='Grades')
plt.plot(names, [average_grade] * len(names), 'r:', label='Class Average')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.legend()
plt.title(f'Test results for the {len(names)} students (class average: {average_grade})')
plt.grid()
plt.savefig('plots/grades.png')
plt.show()

