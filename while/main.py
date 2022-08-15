from itertools import count
from operator import le
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

# Part 1
def unique_koala_facts(numbers):
    if numbers in range(1000):
        facts = []
        count = 0
        while len(facts) < numbers:
            count += 1
            unique_fact = random_koala_fact()
            if unique_fact not in facts:
                facts.append(unique_fact)
            elif count > 1000:
                break
            else :
                continue
        return facts
    
# Part 2
def num_joey_facts():
    facts = []
    count = 0
    single_fact = random_koala_fact() # Infinite loop
    if 'joey' in single_fact:  
        single_fact = random_koala_fact()
    while count < 10 :
        unique_fact = random_koala_fact() # from Part 1
        if 'joey' in unique_fact.lower() and unique_fact not in facts:
           facts.append(unique_fact)
        elif unique_fact == single_fact:
            count += 1
        else:
            continue
    return len(facts)

# Part 3
def koala_weight():
    while True:
        unique_fact = random_koala_fact() # from Part 1
        if 'kg' in unique_fact:
            return int(unique_fact[unique_fact.find('kg')-2:unique_fact.find('kg')])
        else :
            continue
print(koala_weight())