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
    logger.error("Invalid first name: %s. First name must start with a capital letter and be at least 3 characters long.", first_name)
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
    if re.match(pattern, last_name):
        logger.info("Last name validation passed")
        return True
    logger.error("Invalid last name: %s. Last name must start with a capital letter and be at least 3 characters long.", last_name)
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
    
    if re.match(pattern, email):
        logger.info("Email validation passed")
        return True
    logger.error("Invalid email: %s. Email must be in the format abc.xyz@bl.co.in or abc@bl.co", email)
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
    logger.error("Invalid mobile number: %s. Mobile number must be in the format 'XX XXXXXXXXXX'.", mobile)
    return False
   
def validate_password(password):
    """
    Description:
        Validates if the password meets the following criteria:
        - Contains at least one uppercase letter.
        - Contains at least one numeric digit.
        - Has a minimum length of 8 characters.
    
    Parameter:
        password (str): The password entered by the user.
    
    Return:
        bool: True if the password is valid, False otherwise.
    """
    pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
    
    if re.match(pattern, password):
        logger.info("Password validation passed")
        return True
    else:
        if len(password) < 8:
            logger.error("Invalid Password: %s. Password must be at least 8 characters long.", password)
            return False

        if not re.search(r"[A-Z]", password):
            logger.error("Invalid Password: %s. Password must contain at least one uppercase letter.", password)
            return False
    
        if not re.search(r"\d", password):
            logger.error("Invalid Password: %s. Password must contain at least one numeric digit.", password)
            return False
    

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile no: ")
    password = input("Enter your password: ")
    
    validate_first_name(first_name)
    validate_last_name(last_name)
    validate_email(email)
    validate_mobile(mobile)
    validate_password(password)

if __name__ == "__main__":
    main()
