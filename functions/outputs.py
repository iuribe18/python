def format_name(f_name, l_name):
    #docstring
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

input_f_name = input("What is your first name? ")
input_l_name = input("What is your last name? ")
print(format_name(input_f_name, input_l_name))