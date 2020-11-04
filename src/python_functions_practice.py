def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string_1):
    return len(string_1)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

#It's not clear to me why these functions are repeated in the test file
#are we supposed to do them mutliple times?
import calendar
def number_to_full_month_name(month_num):
    return calendar.month_name[month_num]

def number_to_short_month_name(month_num):
    return calendar.month_abbr[month_num]

def volume_of_cube(num_1):
    return pow(num_1, 3)
    #return num_1**3 [tried this too but the above reads nicer to me]

def reverse_string(string_1):
    return "".join(reversed(string_1))
    #also read that return string_1[::-1] would be possible and faster
    # but it seems less readable and I understand it less

def fahrenheit_to_celsius(fahr):
    return (fahr - 32) * 5/9
    #They are same at -40