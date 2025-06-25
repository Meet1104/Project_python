age = int(input("Enter your age :-"))

if age >= 0 :
    if age <= 12 :
        print("child")
    else :
        if age <= 19 :
            print("teen")
        else :
            if age <= 59 :
                print("adult")
            else :
                if  60 <= age :
                    print("senior")
else:
    print("invaild age")

    
    
