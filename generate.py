import argparse
import random
import string

parser = argparse.ArgumentParser()
parser.add_argument("-uc", "--upper-chars", help="Upper Characters", action='store_true')
parser.add_argument("-lc", "--lower-chars", help="Lower Characters",  action='store_true')
parser.add_argument("-n", "--numbers", help="Numbers",  action='store_true')
parser.add_argument("-sc", "--special-chars", help="Special Characters",  action='store_true')
parser.add_argument("-l", "--length", help="Password Length", required=True)
pars = parser.parse_args()

class GeneratePassword():
    def __init__(self, *args):
        self.upperChars = pars.upper_chars
        self.lowerChars = pars.lower_chars
        self.specialChars = pars.special_chars
        self.numbers = pars.numbers
        self.length = int(pars.length)
    
    def CreateNewPassword(self):
        charset = []
        upperChars = string.ascii_uppercase
        lowerChars = string.ascii_lowercase
        specialChars = string.punctuation
        numbers = string.digits
        if self.upperChars:
            charset.extend(upperChars)
        if self.lowerChars:
            charset.extend(lowerChars)
        if self.specialChars:
            charset.extend(specialChars)
        if self.numbers:
            charset.extend(numbers)
        temp = random.choices(charset, k = self.length)
        password = ''.join(temp)
        return password

if __name__ == "__main__":
    password = GeneratePassword(pars.upper_chars, pars.lower_chars, pars.special_chars, pars.numbers, int(pars.length))
    print(password.CreateNewPassword())