'''
@Author: Samadhan Thube
@Date: 2024-09-09
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-09-09
@Title : User Registration Problem
'''

import re

def validate_first_name(first_name):
    """
    Description:
        Validates if the first name starts with a capital letter and has at least 3 characters using regex.
    
    Parameter:
        first_name: The first name entered by the user.
    
    Return:
        bool: True if the first name is valid, False otherwise.
    """
    pattern = r"^[A-Z][a-zA-Z]{2,}$"
    if re.match(pattern, first_name):
        return True
    return False

def validate_last_name(last_name):
    """
    Description:
        Validates if the last name starts with a capital letter and has at least 3 characters using regex.
    
    Parameter:
        last_name (str): The last name entered by the user.
    
    Return:
        bool: True if the last name is valid, False otherwise.
    """
    pattern = r"^[A-Z][a-zA-Z]{2,}$"
    if re.match(pattern,last_name):
        return True
    return False

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    if validate_first_name(first_name):
        print("First name is valid.")
    else:
        print("Invalid first name. Please ensure it starts with a capital letter and is at least 3 characters long.")

    if validate_last_name(last_name):
        print("Last name is valid.")
    else:
        print("Invalid last name. Please ensure it starts with a capital letter and is at least 3 characters long.")
        
if __name__ == "__main__":
    main()
