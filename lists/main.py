# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Part 1
list_films = ['The Matrix', 'Super Man', 'Batman', 'Spiderman']

def alphabetical_order(list_films):
    sorted_list = sorted(list_films)
    return sorted_list
print(alphabetical_order(list_films))

# Part 2
film_names = ['The Poseidon Adventure', 'Cinderella Liberty', 'Tom Sawyer', 'Earthquake', 'Jaws', 'Close Encounters of the Third Kind', 'Star Wars: Episode IV – A New Hope', 'Superman', 'Star Wars: Episode V – The Empire Strikes Back', 'E.T. the Extra-Terrestrial', 'The River', 'Empire of the Sun', 'The Accidental Tourist', 'Born on the Fourth of July', "Schindler's List", 'Seven Years in Tibet', 'Saving Private Ryan', "Angela's Ashes", 'A.I. Artificial Intelligence', 'Memoirs of a Geisha', 'War Horse', 'Lincoln', 'The Book Thief', 'The Post']

def won_golden_globe(film_names):
    won_movies = ['Jaws', 'Star Wars: Episode IV – A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']
    if film_names.lower() in list(map(str.lower, won_movies)):
        return True
    else :
        return False

# Part 3
toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', '35th Anniversary - Live in Poland', 'Toto XIV', 'Old Is New', '40 Tours Around the Sun', 'With a Little Help from My Friends']
list_string = ['Fahrenheit', 'Example A']
def remove_toto_albums(list_string):
  for songs in toto_albums:
      if songs in list_string:
        list_string.remove(songs)
  return list_string
print(remove_toto_albums(list_string))