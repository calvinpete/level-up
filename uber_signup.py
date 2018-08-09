class Signup(object):
    """ A signup form of
    the UBER website."""

    def __init__(self, first_name, last_name, email_address, phone_number, password, promotion_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = Signup.validate_email(email_address)
        self.phone_number = Signup.validate_phone(phone_number)
        self.password = password
        self.promotion_code = promotion_code

    def full_name(self):
        return '{}{}'.format(self.first_name, self.last_name)

    @staticmethod
    def validate_email(email_address):
        import re
        e_mail = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        matcher = e_mail.match(email_address)
        if matcher:
            return "Valid email address"
        else:
            return "Invalid email address"

    def validate_password(self):
        import re
        pwd = re.compile("((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,})")
        matcher1 = pwd.match(self.password)
        if matcher1:
            return self.password
        else:
            return """Password should have more than 7 characters with at least
            one Uppercase, one Lowercase and one number"""

    @staticmethod
    def validate_phone(phone_number):
        import re
        phone_no = re.compile("(\d).{6,}")
        matcher2 = phone_no.match(phone_number)
        if matcher2:
            return "valid phone number"
        else:
            return "invalid phone number"

    def check_user(self):
        pass

    def add_rider(self):
        pass


class Driver(Signup):
    def __init__(self, first_name, last_name, email_address, phone_number, password, city, invite_promo_code=None):
        super(Driver, self).__init__(first_name, last_name, email_address, phone_number, password)
        self.city = city
        self.invite_promo_code = invite_promo_code

    def validate_password(self):
        import re
        pwd = re.compile("((?=.*\d)(?=.*[a-z]).{5,})")
        matcher1 = pwd.match(self.password)
        if matcher1:
            return self.password
        else:
            return "Password should have more than 4 characters  with at least one lowercase and one number"

