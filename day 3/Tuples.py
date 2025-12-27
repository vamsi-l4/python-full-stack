#Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
#Tuples are immutable
#Trying to change an element will raise an error
# my_tuple[0] = 10   This will raise a TypeError
#Tuple Packing and Unpacking
packed_tuple = 1, 2, 3, 4, 5
a, b, c, d, e = packed_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5   
#Tuple Built-in Methods
numbers = (5, 2, 9, 1, 5, 6)
print(numbers.count(5))  # Output: 2
print(numbers.index(9))  # Output: 2
#Nested Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0])        # Output: (1, 2)
print(nested_tuple[1][1])     # Output: 4

#type casting of tuples:
text = "world"
text_tuple = tuple(text)  # ('w', 'o', 'r', 'l', 'd')
print(text_tuple)