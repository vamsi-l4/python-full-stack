print("For loops")
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

print("range in for loop")

for i in range(5):
    print(i)


print("While loops")

count=0
while count<5:
    print("count is:",count)
    count+=1

print("Break :")
for i in range(10):
    if i==5:
        break
    print(i)  
print("Continue :")
for i in range(10):
    if i%2==0:
        continue
    print(i)

print("nested loops:")
for i in range(3):
    for j in range (2):
        print("i:",i,"j:",j)

        