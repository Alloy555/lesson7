'''Homework'''
'''Task 1

A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print “My favorite movie is named {name}”.'''


def favorite_movie(name):
    print('My favorite movie is named ' + name)


favorite_movie('Avatar')

'''Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.'''


def make_country(name, capital):
    country = {}
    country['name'] = name
    country['capital'] = capital
    return country


my_country = make_country('Ukraine', 'Kyiv')
print(my_country)