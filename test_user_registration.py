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
    assert user_registration.validate_email("abc.xyz@bl.co.inn") == True
    assert user_registration.validate_email("abc@bl") == False
    assert user_registration.validate_email("abc@bl.") == False
    

if __name__ == "__main__":
    pytest.main()
