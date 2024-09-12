import pytest
import user_registration

def test_validate_first_name():
    assert user_registration.validate_first_name("Sam") == True
    assert user_registration.validate_first_name("John") == True
    assert user_registration.validate_first_name("sam") == False
    assert user_registration.validate_first_name("Jo") == False
    assert user_registration.validate_first_name("j") == False

def test_validate_last_name():
    assert user_registration.validate_last_name("Thube") == True
    assert user_registration.validate_last_name("Doe") == True
    assert user_registration.validate_last_name("thube") == False
    assert user_registration.validate_last_name("Do") == False
    assert user_registration.validate_last_name("d") == False

def test_validate_email():
    assert user_registration.validate_email("abc@bl.co") == True
    assert user_registration.validate_email("abc.xyz@bl.co.in") == True
    assert user_registration.validate_email("abc@bl") == False
    assert user_registration.validate_email("abc@bl.") == False
    assert user_registration.validate_email("abc.xyz@bl.co.inn") == False

def test_validate_mobile():
    assert user_registration.validate_mobile("91 9876543210") == True
    assert user_registration.validate_mobile("01 1234567890") == True
    assert user_registration.validate_mobile("919876543210") == False
    assert user_registration.validate_mobile("91 98765432") == False
    assert user_registration.validate_mobile("9876543210") == False

def test_validate_password():
    assert user_registration.validate_password("Password1!") == True
    assert user_registration.validate_password("A1b2c3d4!") == True
    assert user_registration.validate_password("GoodPass1@") == True
    assert user_registration.validate_password("Strong1$") == True

    assert user_registration.validate_password("password1") == False    
    assert user_registration.validate_password("Password1") == False    
    assert user_registration.validate_password("Password!!") == False   
    assert user_registration.validate_password("Pass1!") == False       
    assert user_registration.validate_password("12345678!") == False    
    assert user_registration.validate_password("Password!") == False  


if __name__ == "__main__":
    pytest.main()
