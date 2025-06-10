

try:
#  num1=int(input())
#  num2=int(input())
#  res=num1/num2
 file =open("./name.txt","r+")
 print(f"the result is {file.readlines()}")
#  file=open("./name.txt","w")
 file.write("Very Good")
#  print(f"the result is {}")
except Exception as e:

   print(f"error is {e}")
else:
   print("you try in good way")
finally:
  print("bro completed")
  file.close()
   
   