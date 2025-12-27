#sets
# Creating a set with elements
numbers = {1,2,2,3,4}
print(numbers)  # Output: {1, 2, 3, 4} (duplicates are removed)

# Creating an empty set
empty_set = set()
print(empty_set) # Output: set()

#Typecasting to Set
list_data=[1,2,2,3,4]
set_data=set(list_data)  #{1,2,3,4}
print(set_data)

#common set methods
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}
numbers.remove(2)
print(numbers)  # Output: {1, 3, 4}
numbers.discard(5) #Does not raise an error if the element is missing
print(numbers)  # Output: {1, 3, 4}
numbers.pop() # removes and returns an arbitrary element 
print(numbers)  # Output: {3, 4} (or other elements depending on what was popped)
numbers.clear()
print(numbers)  # Output: set()
items = {10, 20, 30}
item = items.pop()
print(item)    # Output: (could be 10 or 20 or 30)
print(items)   # Remaining items
#set operations 
set_a={1,2,3}
set_b={3,4,5}
#union
print(set_a.union(set_b))
#intersection
print(set_a.intersection(set_b))
#difference
print(set_a.difference(set_b))
#symmetric difference
print(set_a.symmetric_difference(set_b))
#Subset and Superset
set_c={1,2}
print(set_c.issubset(set_a))  # Output: True
print(set_a.issuperset(set_c))  # Output: True
print(set_a.issubset(set_b))  # Output: False
print(set_b.issuperset(set_a))  # Output: False
#Frozen Sets    
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4})
#frozen sets are immutable
# frozen_set.add(5)  # This will raise an AttributeError
# frozen_set.remove(2)  # This will raise an AttributeError
#Set Comprehensions
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}



