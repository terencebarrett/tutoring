# Lesson 02: Booleans, If/then/else, f-strings

# Ctrl-D to duplicate text segments or line(s)
# Ctrl-/ to comment or uncomment line(s)

# f-strings are the best strings
string_1 = 'The person is identified as: John'
print(string_1)

string_1 = 'The person is identified as: Mary'
print(string_1)

string_2 = 'The person is identified as:'
name = 'Herbert'
print(string_2, name)

name = 'Eliza'
print(string_2, name)

string_3 = string_2 + ' ' + name
print(string_3)

print(f'The person is identified as: {name}')  # First f-string

name = 'Dirk'
print(f'The person is identified as: {name}')


# Booleans
x = 3

x == 3
x != 3
x < 4
x > 10
x >= 1
x <= 3

y = 9

x == y
x < y

result_1 = True
print(result_1)
type(result_1)

result_2 = False
print(result_2)
type(result_2)

result_1 == result_2
result_1 == (not result_2)

test_1 = x > y
print(test_1)

test_2 = x != y
print(test_2)

test_3 = x == y
print(test_3)


# If statement (if/elif/else; with reference to booleans: if True then ...)

if 13 < 10:
    print('First number is less than the second')

if False:
    print('First number is less than the second')

a = 40
b = 10
print(f'a: {a}, b: {b}')
if a < b:
    print('a is less than b')
else:
    print('a is not less than b')

c = 13
d = 10
print(f'c: {c}, d: {d}')
if c < d:
    print('c is less than d')
elif c == d:
    extra_info = 'Yes!'
    print(f'c is equal to d, {extra_info}')
else:
    print('c is greater than d')

h = 11
i = 12
j = 13
print(f'h: {h}, i: {i}, j: {j}')
if h < i and i < j:  # can also be written as h < i < j
    # print('h, i, j are in ascending order')
    print(f'{h}, {i}, {j} are in ascending order')
elif h < i or i < j:
    print('At least one set (h, i) or (i, j) is in ascending order')
else:
    print('h, i, and j are just some stupid numbers')


# Challenge:

# Write a script that has a variable holding a student's numerical grade, and uses the logic below
#   to print (using the letter grade as a variable printed in an f-string) the
#   appropriate message:
#
#     0 - 59: "The student's letter grade: F"
#     60 - 69: "The student's letter grade: D"
#     70 - 79: "The student's letter grade: C"
#     80 - 89: "The student's letter grade: B"
#     90 - 100: "The student's letter grade: A"
#     For a number outside the range 0-100: "The student's letter grade: error"
#
#   If the grade is C or lower, print an additional message about giving the student extra help
#
#   And for a taste of the philosophy of Python, type "import this" into the Python command line


