
from statistics import mean

import matplotlib.pyplot as plt

from src.utilities import msg_from_number_grade


# TODO: highlight when a student's grade is being overwritten and ask to confirm

keep_going = True
i = 0
grade_dict = {}
while keep_going:
    i += 1
    input_str = input('Enter student name and their numerical grade (with a '
                      'space between) -- or "quit" to finish: ')
    input_list = input_str.split()
    if 'quit' in input_str:
        keep_going = False
    elif len(input_list) != 2 \
            or input_list[0].isdigit() \
            or not input_list[1].isdigit() \
            or int(input_list[1]) > 100 \
            or int(input_list[1]) < 0:
        print('Incorrect input!')
        i -= 1
    else:
        input_name_str = input_list[0]
        grade_int = int(input_list[1])
        msg = msg_from_number_grade(grade_int, is_student=True)
        print(msg)
        grade_dict[input_name_str] = {'msg': msg, 'number_grade': grade_int}
else:
    print('All done!\n')
    names = list(grade_dict.keys())
    number_grades = []
    for name in names:
        print(name, '\t', 'number grade:', grade_dict[name]['number_grade'],
              ',', grade_dict[name]['msg'])
        number_grades.append(grade_dict[name]['number_grade'])
    average_grade = round(mean(number_grades))
    print('The average grade is', average_grade, ',',
          msg_from_number_grade(average_grade, is_student=False))

# Plot the student grades
fig_1 = plt.figure()
plt.plot(names, number_grades, 'bd', label='Grades')
plt.plot(names, [average_grade] * len(names), 'r:', label='Class Average')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.legend()
plt.title(f'Test results for the {len(names)} students '
          f'(class average: {average_grade})')
plt.grid()
plt.savefig('plots/grades.png')
plt.show()
