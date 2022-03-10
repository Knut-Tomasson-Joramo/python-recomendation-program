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
def print_resturant_info(type_of_resturant, resturant_list):
  for resturant in resturant_list:
    if type_of_resturant == resturant[0]:
      print_resturant(resturant)
  


# print info on resturant
# format:
# \n
# -----------------
# name
# price
# rating
# address \n\n
def print_resturant(resturant):
  print("--------------------------\n")
  print("Name:\t\t{0}\nPrice:\t\t{1}/5\nRating:\t\t{2}/5\nAddress:\t{3}\n\n".format(
    resturant[1],
    resturant[2],
    resturant[3],
    resturant[4]))


# Greeting to the user
def greeting(city="Oslo"):
  print("""
  #############################################
  ######## welcome to {} resturants! ########
  #############################################\n\n
  """.format(city))


def promt_for_food():
  return input("Type in the beginning of what type of food you you would like:\n\n")


# get list of resturants matching input
def get_matching_resturants(string_input, list_of_resturants):
  result = []
  for resturant in list_of_resturants:
    if string_input == list_of_resturants[0][0:len(string_input)]:
      result.append(resturant)
  if not result:
    return False, result
  else:
    return True, result


# function to run whole program
def main_program():
  greeting()

  loop = True
  while loop:
    type_of_food = get_requested_type(promt_for_food(), types)
  
    while not type_of_food:
      print("This type is not in our database..\n")
      try_again = input("Would you like to try again? (y/n): ")
      if try_again != "y":
        return None
      type_of_food = get_requested_type(promt_for_food(), types)
    
    print("\nThe types of food matching your input is: {}\n".format(type_of_food))
    while len(type_of_food) > 1:
      the_chosen_one = input("write the beginning of the food you want or 'exit' to quit: \n\n")
      if the_chosen_one == "exit":
        return None
      type_of_food = get_requested_type(the_chosen_one, type_of_food)
      if len(type_of_food) > 1:
        print("\nThe types of food matching your input is: {}\n".format(type_of_food))
      elif len(type_of_food) == 0:
        print("This type of food is not in our database..\n\n")

    answer = input("\nThe only type matching is {}. show results? (y/n)\n".format(type_of_food[0]))
    if answer == "y":
      print_resturant_info(type_of_food[0], restaurant_data)


main_program()
