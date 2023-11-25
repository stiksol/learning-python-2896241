# file = open(r"Files\essay.txt", 'r')
# content = file.read()
# final_string = ""
# for i in content.split():
#     final_string = final_string + i.capitalize() + " "
#
# print(len(content))
#
# user_entries = ['10', '19.1', '20']
# outcome = [float(user_entry) for user_entry in user_entries]
# print(outcome)
#
#
# day_temperatures = {'morning':(23.6,54.7,56.7), 'noon':(23.5,54.8,56.8), 'evening':(23.5,54.8,56.9)}

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_value =  max(grades)
    min_value = min(grades)
    return f"Max: {max_value}, Min: {min_value}"


print(get_max())
