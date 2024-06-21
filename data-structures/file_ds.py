# List : []
#   - len(), max(), del , append(), min(), sorted() , sum(), pop() - last element from list ,
#   - [a:b] : indexing for elements of list
#   c = [a,b] , where a and b are lists
#   for color, nums in zip(*c)

# Tuple : ()
#   - can not modify, not mutable , personal data
#   - del , x in tpl , tpl1 + tpl2 , tpl *2 , tpl[x] : indexing

# Dictionary : {} , not ordered , unique
#   - key-value pair , del , .get(x) : based on key , .del() , .keys() , .values() , pop() : based on key
#   - dct = dict(x=y)

# sets : () , not ordered , unique
#   - .add() , .remove(x) , searching/find fast than list, x in set , pop() : removed random element
#   - x.union(y), intersection() and difference()
#   - automatically removes duplicate values
a = {'red', 'yellow','orange','green'}
b = {'red','orange','black'}
print(a | b) # union
print(a - b) # difference
print(a & b) # intersection