def msg_from_number_grade(number_grade, is_student):
    """
    Return a letter grade message when given a number grade.

    Params:
        number_grade  int
        is_student  bool

    Returns:
        str
    """
    string_1 = "letter grade:"
    string_2 = "F."
    string_3 = "D."
    string_4 = "C."
    string_5 = "B."
    string_6 = "A."
    if is_student:
        string_7 = "*Note: This student needs extra help"
    else:
        string_7 = "*Note: This class needs extra help"
    string_8 = "error"

    if 59 >= number_grade >= 0:
        msg = string_1 + ' ' + string_2 + ' ' + string_7
    elif 69 >= number_grade >= 60:
        msg = string_1 + ' ' + string_3 + ' ' + string_7
    elif 79 >= number_grade >= 70:
        msg = string_1 + ' ' + string_4 + ' ' + string_7
    elif 89 >= number_grade >= 80:
        msg = string_1 + ' ' + string_5
    elif 100 >= number_grade >= 90:
        msg = string_1 + ' ' + string_6
    else:
        msg = string_1 + ' ' + string_8

    return msg

