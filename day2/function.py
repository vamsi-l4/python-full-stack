def func():#function  definitiomn 
    print("Function in day2/function.py") #function body 
func()    #function call 



def fun(*a):
    print("this is arbutary arguments function",a)
fun(1,2,3)    


def fun(**a):
    print("this is keyword arbutary arguments function",a)
fun(name="john",age=25)


def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()            


def add(a,b):
    print("sum is:",a+b)
add(4,5)    
def sub(a,b):
    print("difference is:",a-b)    
sub(5,4)    