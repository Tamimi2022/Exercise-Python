from itertools import count
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
# Part 1
def shortest_names(countries):
    shortest_name = []
    short = min(countries, key=len)
    for country in countries:
        if len(country) == len(short):
            shortest_name.append(country)
    return shortest_name

# Part 2
def most_vowels(countries):
    vowels = 'aeiouAEIOU'
    y = []
    for country in countries:
        count = 0
        for char in country:
            if char in vowels:
                count = count + 1
        y.append([country, count])
        y = sorted(y, key=lambda x: x[1], reverse=True)
    return [item[0] for item in y[:3]]

# Part3
def alphabet_set(countries):
    combined_alphabet = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for country in countries:
        for char in country.lower():
            if char.isalpha() and char in alphabet:
                alphabet.remove(char)
                if country in combined_alphabet:
                    continue
                else:
                    combined_alphabet.append(country)
            continue
        continue
    return combined_alphabet
            
    

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))