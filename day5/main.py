import mini as mf
print("/t GRADE BOOK /n")
while True :
    
    print("1.add_student")
    print("2.avg_student")
    print("3.search_student")
    print("4.upadate_student")
    print("5.remove_student")
    choices=int(input("enter the choice :"))
    if choices==1:
        mf.add_student()
    elif choices==2:
        mf.avg_student()
    elif choices==3:
        mf.search_student()
    elif choices==4:
        mf.update_student()
    elif choices==5:
        mf.remove_student()
    else:
       print("close the the GRADE BOOK")