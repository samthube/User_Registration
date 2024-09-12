import unittest
import user_registration

class TestUserRegistration(unittest.TestCase):

    def test_validate_first_name(self):
        
        self.assertTrue(user_registration.validate_first_name("Sam"))
        self.assertTrue(user_registration.validate_first_name("John"))
        
        self.assertFalse(user_registration.validate_first_name("sam"))
        self.assertFalse(user_registration.validate_first_name("Jo"))
        self.assertFalse(user_registration.validate_first_name("j"))

    def test_validate_last_name(self):
       
        self.assertTrue(user_registration.validate_last_name("Thube"))
        self.assertTrue(user_registration.validate_last_name("Doe"))
        
        self.assertFalse(user_registration.validate_last_name("thube"))
        self.assertFalse(user_registration.validate_last_name("Do"))
        self.assertFalse(user_registration.validate_last_name("d"))

    def test_validate_email(self):
      
        self.assertTrue(user_registration.validate_email("abc@bl.co"))
        self.assertTrue(user_registration.validate_email("abc.xyz@bl.co.in"))
       
        self.assertFalse(user_registration.validate_email("abc@bl"))
        self.assertFalse(user_registration.validate_email("abc@bl."))
        self.assertFalse(user_registration.validate_email("abc.xyz@bl.co.inn"))

    def test_validate_mobile(self):
        
        self.assertTrue(user_registration.validate_mobile("91 9876543210"))
        self.assertTrue(user_registration.validate_mobile("01 1234567890"))
        
        self.assertFalse(user_registration.validate_mobile("919876543210"))
        self.assertFalse(user_registration.validate_mobile("91 98765432"))
        self.assertFalse(user_registration.validate_mobile("9876543210"))
        
    def test_validate_password(self):
        
        self.assertTrue(user_registration.validate_password("Password123"))
        self.assertTrue(user_registration.validate_password("Valid123"))
        self.assertTrue(user_registration.validate_password("abcdefgh"))
        self.assertTrue(user_registration.validate_password("PassWord8"))

        self.assertFalse(user_registration.validate_password("short7"))     
        self.assertFalse(user_registration.validate_password("abc"))        
        self.assertFalse(user_registration.validate_password("1234567"))   
        self.assertFalse(user_registration.validate_password(""))           
        self.assertFalse(user_registration.validate_password("Aa1")) 

if __name__ == "__main__":
    unittest.main()
