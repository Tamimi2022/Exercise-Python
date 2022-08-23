__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from cgi import test
import glob
from importlib.resources import path
import os
import shutil
from zipfile import ZipFile


# Point 1
def clean_cache():
    if not os.path.exists("./files/cache"):              
        print("Creating new Dir 'cache")
        os.mkdir("./files/cache")                         
    else:
        print("Cleaning/Removing The new Dir 'cache")
        shutil.rmtree("./files/cache")
        os.mkdir("./files/cache")
    
# Point 2
def cache_zip(zip_path: str, cache_path: str):
    test = os.path.abspath('data.zip')
    print(test)
    #clean_cache()
    with ZipFile(zip_path, "r") as zip:
        zip.extractall(cache_path)
        
# Point 3
def cached_files():
    path = os.getcwd() + "/files/cache//"
    files_list = glob.glob(path + "*.txt")
    return files_list

# Point 4
def find_password(files_list):
    for list in files_list:
        with open(list, "r") as l:
            for text in l.readlines():
                if 'password' in text:
                    return (text.split(": ")[1]).strip()
                
    print(find_password(files_list))
    
if __name__ == '__main__':
    pass