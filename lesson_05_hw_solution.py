
# One way to code the TODO: Clean up input so a quit on either stops immediately and doesn't ask for the second input
"""
input_str = input('Enter student name and their numerical grade (with a space between) -- or "quit" to finish: ')
input_list = input_str.split()
if 'quit' in input_str:
    keep_going = False
elif len(input_list) != 2 \
    or input_list[0].isdigit() \
    or not input_list[1].isdigit() \
    or int(input_list[1]) > 100 \
    or int(input_list[1]) < 0 \
    or input_list[0] in list(grade_dict.keys()):
        print('Incorrect input!')
        i -= 1
else:
    input_name_str = input_list[0]
    grade_int = int(input_list[1])
    msg = msg_from_number_grade(grade_int, is_student=True)
    print(msg)
    grade_dict[input_name_str] = {'msg': msg, 'number_grade': grade_int}
"""

# One way to code the TODO: Allow reentering the student name with a different grade
#   Note: The student number shown in the input-request message will have an extra increment,
#          but that doesn't matter to later calculations or plotting
"""
    elif not input_grade_str.isdigit() \
            or input_name_str.isdigit() \
            or int(input_grade_str) > 100 \
            or int(input_grade_str) < 0:
            # or input_name_str in list(grade_dict.keys()): # Just Remove this line 
        print('Incorrect input!')
        i -= 1
"""

# One way to code the TODO: Use any()?
#   Note: This TO-DO will be moot when code for first TO-DO in this file is merged.
"""
if any([input_grade_str=='quit', input_name_str=='quit']):
"""
# A better way (using the new topic of `list comprehensions`):
"""
if any([x=='quit' for x in [input_grade_str, input_name_str]]):
"""