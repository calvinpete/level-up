import unittest
from uber_signup import Signup
from uber_signup import Driver

class TestRider(unittest.TestCase):

    def setUp(self):
        self.calvin_p = Signup("calvin", "pete", "tinkacalvin@gmail.com", "0773548160", "tropics54")

    def test_creation(self):
        self.assertIsInstance(self.calvin_p, Signup)

    def test_fullName(self):
        self.assertEqual(self.calvin_p.full_name(), "calvinpete")

    def test_validatePhoneNumber(self):
        with self.assertRaises(ValueError):
            Signup.validate_phone('900p9w4q67')

    def test_validateEmail(self):
        with self.assertRaises(ValueError):
            Signup.validate_email("tinkacalvin@gmailoe")

    def test_validatePassword(self):
        with self.assertRaises(ValueError):
            self.calvin_p.validate_password()

    def test_addRider(self):
        self.assertEqual(self.calvin_p.add_rider(), [['calvin', 'pete', "Valid email address", "valid phone number", 'tropics54', None]])


class TestDriver(unittest.TestCase):

    def setUp(self):
        self.Roger = Driver("Mark", "Roger", "markroger@gmail.com", "0783145213", "arsenalfc", "kampala", "N0898")

    def test_creation(self):
        self.assertIsInstance(self.Roger, Signup)

    def test_fullName(self):
        self.assertEqual(self.Roger.full_name(), "MarkRoger")

    def test_validatePhoneNumber(self):
        with self.assertRaises(ValueError):
            Driver.validate_phone('9877j7f8980')

    def test_validateEmail(self):
        with self.assertRaises(ValueError):
            Driver.validate_email("f377777777777")

    def test_validatePassword(self):
        with self.assertRaises(ValueError):
            self.Roger.validate_password()

    def test_addRider(self):
        self.assertEqual(self.Roger.add_driver(), [["Mark", "Roger", "Valid email address", "valid phone number", "arsenalfc", "kampala", "N0898"]])


if __name__ == '__main__':
    unittest.main()