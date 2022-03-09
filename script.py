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


# function to print resturant info
def print_resturant_info(type_of_resturant, resturant_dict):
  if type_of_resturant in resturant_dict:
    for resturant in resturant_dict:
      if type_of_resturant == resturant:
        print("name, price, rating, address")  # need to update with own function..
  else:
    print("No such resturant in this area..")


# print info on resturant
# format:
# \n
# -----------------
# name
# price
# rating
# address \n\n
def print_resturant(resturant):
  pass



