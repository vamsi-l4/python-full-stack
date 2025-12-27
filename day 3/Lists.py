v=[]
print(type(v))                  #list
#print(v[1])                    #IndexError: list index out of range
L=[4,5,45,'vamsi',"krish"]
print(L)                        #output:[4, 5, 45, 'vamsi', 'krish']
print(L[-1])
print(L[0:3:2])

#type casting of lists:
text = "hello"
text_list = list(text)  # ['h', 'e', 'l', 'l', 'o']
print(text_list)

numbers = (1, 2, 3)
numbers_list = list(numbers)  # [1, 2, 3]
print(numbers_list)

data = {"a", "b", "c"}
data_list = list(data)  # Order not guaranteed: ['a', 'c', 'b']
print(data_list)
#Using map() with Lists:
def square(n):
    return n * n
nums = [1,2,3,4,5]
squared_nums = list(map(square,nums))
print(squared_nums)            #output:[1, 4, 9, 16, 25]

#List Built-in Methods
fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'potato', 'cabbage']
fruits.append('orange')
print(fruits)
fruits.pop(1)
print(fruits)
fruits.insert(1,'banana')
print(fruits)
fruits.remove('banana')
print(fruits)   
fruits.extend(vegetables)
print(fruits)   
fruits.clear()
print(fruits)                #output:['apple', 'banana', 'cherry', 'carrot', 'potato', 'cabbage']
vegetables.clear()
print(vegetables)                 #output:[]
#List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)
#output:[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares) 
#output:[0, 4, 16, 36, 64]
#Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])          #output:[1, 2, 3]
print(matrix[1][2])       #output:6
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
#output:1 2 3 4 5 6 7 8 9
#List Slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:5])        #output:[2, 3, 4]
print(my_list[:4])         #output:[0, 1, 2, 3]
print(my_list[5:])         #output:[5, 6, 7, 8, 9]
print(my_list[::2])        #output:[0, 2, 4, 6, 8]
print(my_list[::-1])       #output:[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]   
#List Membership
my_list = [10, 20, 30, 40, 50]
print(20 in my_list)        #output:True
print(60 not in my_list)    #output:True