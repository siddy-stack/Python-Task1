import unittest as test
from src.task1 import is_valid_email,is_valid_phone,FILE_NAME
import os


class TestValidation(test.TestCase):

    # PHONE NUMBER TESTS
    def test_valid_phone(self):
        self.assertTrue(is_valid_phone("9876543210"))

    def test_phone_with_letters(self):
        self.assertFalse(is_valid_phone("98765abc10"))

    def test_phone_short_length(self):
        self.assertFalse(is_valid_phone("987654321"))

    def test_phone_long_length(self):
        self.assertFalse(is_valid_phone("98765432101"))

    # EMAIL TESTS
    def test_valid_email(self):
        self.assertTrue(is_valid_email("john@gmail.com"))

    def test_email_missing_at(self):
        self.assertFalse(is_valid_email("johngmail.com"))

    def test_email_missing_dotcom(self):
        self.assertFalse(is_valid_email("john@gmail"))

    def test_email_wrong_domain(self):
        self.assertFalse(is_valid_email("john@gmail.org"))

class TestFileWrite(test.TestCase):

      def test_contact_file_created(self):
          self.assertTrue(os.path.exists(FILE_NAME))

if __name__ == "__main__":
    test.main()