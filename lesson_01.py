# Lesson 01: Basics, Variables, Lists

# Show python in a bare system console before moving to the IDE
# Execute one line: Alt-Shift-e
# Type into console one line at a time
# Run as a script
# Show code completion in editor and console

# python --version
# dir()  # First function
# vars()
# exit()

print('Hello World!')

x = 3
print(x)  # A simple function
# x
# who

y = 8.4
# who

name = 'Terry'
# name
print(name)

number_list = [1, 2, 3]
word_list = ['fox', 'eagle', 'red panda']
variable_list = [x, y]
print(variable_list)

mixed_list = ['one', 9, x]
print(mixed_list)

# mixed_list_2 = ['9', z, 'chicken']
z = [2**3, 6+3, 'one' + 'two' + 'three']
mixed_list_2 = ['9', z, 'chicken']
print(mixed_list_2)

# reset
# del x

type(x)
type(y)
type(name)
type(number_list)

len(number_list)
print(number_list)
number_list[0]
number_list[1]
number_list[2]
# number_list[3]
number_list[-1]
number_list[-2]
number_list[-3]
# number_list[-4]
number_list[:]
number_list[1:]
number_list[:-1]

print(number_list)
number_list[1] = 999
print(number_list)

# https://docs.python.org/3/tutorial/introduction.html



