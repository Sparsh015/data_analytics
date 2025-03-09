class programmer :
    company = "Microsoft" 

    def __init__(self , name , salary) :
        self.name = name
        self.salary = salary

ans = "y"
while(ans != "n"):
    
    p_n = input( "enter details name ")
    p_s = int(input( "enter details salary ")) 

    p = programmer(p_n , p_s)

    print(p.name , p.salary , p.company )

    ans = input("more inputs ? (y/n) ")


