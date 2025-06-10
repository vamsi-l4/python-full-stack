

student={
    "name":"saiRam",
    "age":"20",
    "marks":[98,99,95],
    "present":True

}
print(student["name"])
student["age"]=21
print(student["age"])
sum=0
for i in student["marks"]:

    sum+=i
student["avg"]=sum/len(student["marks"])
print(student)
for i in student:

        print(f"{i}={student[i]}")
del student["name"] #using None instant of del
print(student)