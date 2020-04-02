days = [("Sun",0), ("mon",1), ("tue",2), ("wed",3), ("thus",4), ("fri",5), ("satu",6)]
i = int(input("enter starting day number: "))
j = int(input("length of the stay: "))
for day, number in days:
    if j < 7:
        x = i + j   #if j<7 then add it with i
        x= x - 7    #then minus 7 from addition will give you the day 
        if number == x:
            print(day)
    if j > 7:
        while j > 7:
            y= j%7
        print(y)
        i = i + y
        if number == i:
            print(day)
