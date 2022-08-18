# Do not modify these lines
from unicodedata import name
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
# Part 1
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
            'name': name, 
            'date_of_birth': date_of_birth, 
            'place_of_birth': place_of_birth, 
            'height': float("{:.2f}".format(height)), 
            'nationality': nationality
            }    
    return passport

# Part 2
def add_stamp(passport, country):
        passport_stamp = {
                'stamps': country
        }
        if country not in passport.values():  # visited home country
                if 'stamps' not in passport.keys():  # passport have a stamp
                        passport['stamps'] = [country] # key-value for stamps
                elif country not in passport['stamps']:
                        passport['stamps'].append(country)
                return passport
        
# Part 3
def add_biometric_data(passport, name, value, date):
    if 'biometric' not in passport: # key
        passport['biometric'] = {}
    if name not in passport:
        passport['biometric'][name] = {}
    passport['biometric'][name] = {
                'value' : value,
                'date' : date
                }
    return passport