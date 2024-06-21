# format function
mdg = "hello world, my name is {}".format('bhavya')
print(mdg)

# len() function
name = "Bhavya Patel"
print(len(name))
print(name[:6])

# count() function
print(name.count('a'))
print(name.count('a',6, 12))

# endswith() and startswith() functions
print(name.lower().startswith('b'))
print(name.lower().startswith('a'))

# Find : first occurance of particular text
print(name.find('b'))
print(name.find('B'))

# islower() and #isupper() : all values check upper or lower characters
# lower() and upper() : to convert into upper or lower characters

# join() : sep.join() , join list or string with separator
# replace(a,b,x) : replace a with b for x times
# strip() : removing particular character or white space from string

# capitalize() : first char to upper and other lower
# swapcase() : converting lower to upper and upper to lower
# title() : converting it to title, each word first char capital


# input variable : input("something pass")
# msg = "can\'t"
# Escaping sequence :
#     \ : newline ignored
#     \\ : backslash
#     \" , \' : quotes
#      \n : newline , \t : horizontal tab , \v : vertical tab
