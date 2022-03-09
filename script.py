# file name:      script.py
# creation date:  08.03.2022
# author:         Knut Tomasson Joramo
# 
# portfolio project codecademy.com computersience 102
# task is to build a recommendation software
# 

from resturants import restaurant_data, types

# function to get all types that matches input
def get_requested_type(string_input, list_of_types):
  result_list = []
  for type in list_of_types:
    if string_input == type[0:len(string_input)]:
      result_list.append(type)
  return result_list

print(get_requested_type("c", types))
