import re
import mylogging 

logger = mylogging.logger_init('user_registration')

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
        logger.info("First name validation passed")
        return True
    logger.error("Invalid first name: %s", first_name)
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
        logger.info("Last name validation passed")
        return True
    logger.error("Invalid last name: %s", last_name)
    return False

def validate_email(email):
    """
    Description:
        Validates if the email follows the required format with 3 mandatory parts (abc, bl & co)
        and 2 optional parts (xyz & in) in the format abc.xyz@bl.co.in.
    
    Parameter:
        email (str): The email address entered by the user.
    
    Return:
        bool: True if the email is valid, False otherwise.
    """
    pattern =r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2})?$"
    
    if re.match(pattern,email):
        logger.info("Email validation passed")
        return True
    logger.error("Invalid email: %s", email)
    return False

def validate_mobile(mobile):
    """
    Description:
        Validates if the mobile number follows the format: country code, followed by a space, and a 10-digit number.
    
    Parameter:
        mobile (str): The mobile number entered by the user.
    
    Return:
        bool: True if the mobile number is valid, False otherwise.
    """
    pattern = r"^\d{2} \d{10}$"

    if re.match(pattern, mobile):
        logger.info("Mobile number validation passed")
        return True
    logger.error("Invalid mobile number: %s", mobile)
    return False
    

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile no: ")
    
    if validate_first_name(first_name):
        print("First name is valid.")
    else:
        print("Invalid first name. Please ensure it starts with a capital letter and is at least 3 characters long.")

    if validate_last_name(last_name):
        print("Last name is valid.")
    else:
        print("Invalid last name. Please ensure it starts with a capital letter and is at least 3 characters long.")
    
    if validate_email(email):
        print("Email is valid.")
    else:
        print("Invalid email.")
        
    if validate_mobile(mobile):
        print("Mobile number is valid.")
    else:
        print("Invalid mobile number.")
             

if __name__ == "__main__":
    main()
