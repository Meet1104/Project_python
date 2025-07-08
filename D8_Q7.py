def students(*kwargs):
    if not kwargs:
        print("no names")
    else:
        for i in kwargs:
            print(i)

students("meet","jay","Vraj")
