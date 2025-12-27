#dictonary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
#Accessing Values
print(my_dict['name'])  #output:Alice
print(my_dict.get('age')) #output:30
#adding and updating keu-value pairs
my_dict['age'] =31  #update age
my_dict['profession']= 'ENGINEER' #add profession
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'profession': 'ENGINEER'}
#removing key-value pairs
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'profession': 'ENGINEER'}
removed_value = my_dict.pop('profession')
print(removed_value)  # Output: ENGINEER
print(my_dict)  # Output: {'name': 'Alice', 'age': 31 }
#Dictionary Built-in Methods
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(len(my_dict))  # Output: 3    
print(my_dict.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York'])
print(my_dict.items())   # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
my_dict.clear()
print(my_dict)  # Output: {}