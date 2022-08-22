# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# Point 1
#import zen_of_python

# All Import
from datetime import datetime
import math
import sys
import time
import greet

# Point 2
def wait(seconds):
    time.sleep(seconds)
    return

# Point 3
def my_sin(float):
    return math.sin(float) # Using math module

# Point 4
def iso_now():
    current_date = datetime.now() # Using datetime module
    return current_date.strftime("%Y-%m-%dT%H:%M")

# Point 5
def platform():
    return sys.platform # Using sys module
print(sys.platform)

# Point 6
def supergreeting_wrapper(supergreeting):
    return greet.supergreeting(supergreeting) # Calls 