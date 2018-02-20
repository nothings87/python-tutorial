
### Tuples

# Tuples are just like lists, but you can't change their values.
# The values that you give it first up, are the values that you are stuck with for the rest of the program.
# Again, each value is numbered starting from zero, for easy reference. Example: the names of the months of the year.

months = ('January','February','March','April','May','June',\
		'July','August','September','October','November','December');




### Lists

# Lists are extremely similar to tuples.
# Lists are modifiable (or 'mutable', as a programmer may say),
# so their values can be changed.
# Most of the time we use lists, not tuples, because we want to easily change the values of things if we need to.

cats = ['Tom', 'Snappy', 'Kitty'];

# print
print cats[1];

# add
cats.append('Catherine');

# del
del cats[0];


### Dictionary

# word-definition pair(key-value)
phonebook = {'Andrew Parson':991323, \
		'Emily Everett':124424, \
		'Lewis Lame':1199304};


# add
phonebook['Samuel Adams'] = 979934;

# del
del phonebook['Emily Everett'];











