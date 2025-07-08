def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}---->{value}")
    
person(name = "Meet",age = 20)