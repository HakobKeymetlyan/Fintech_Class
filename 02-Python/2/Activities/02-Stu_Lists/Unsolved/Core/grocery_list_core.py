# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries

grocery_list = ["water", "butter", "eggs", "apples", "cinnamon", "sugar", "milk"]



# @TODO: Find the first two items on the list

print(grocery_list [0:4])


# @TODO: Find the last five items on the list

print(grocery_list[-5:])


# @TODO: Find every other item on the list, starting from the second item
print(grocery_list[1::2])



# @TODO: Add an element to the end of the list

grocery_list.append("Cognac")
print(grocery_list)


# @TODO: Changes a specified element within the list at the given index
index = grocery_list.index("Cognac")
grocery_list[index] = "Ararat Cognac"

print(grocery_list)

# @TODO: Calculate how many items you have in the list

print(len(grocery_list))
