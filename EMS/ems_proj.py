dict = {101 : {'name' : 'Sparsh', 'age' : 20, 'department' : 'SDE', 'salary' : 10000000}, 102 : {'name' : 'Jiya', 'age' : 20, 'department' : 'SWE', 'salary' : 90000}, 103 : {'name' : 'Vishal', 'age' : 21, 'department' : 'HR', 'salary' : 50000}}

def option_menu():
    print("1 -> Add employee")
    print("2 -> View all employees")
    print("3 -> Search for employee")
    print("4 -> Exit")
    return


def add_emp():
    emp_id = int(input('enter employee id -> '))
    if emp_id in dict:
        print("enter a unique id \n")
        add_emp()

    name = input('enter the name of employee -> ')
    age = int(input('enter the age -> '))
    department = input('enter the department -> ')
    salary = int(input('enter the salary -> '))

    dict[emp_id] = {'name' : name, 'age' : age, 'department' : department, 'salary' : salary}
    print("employee added successfully")
    return


def view_employees():
    if len(dict) == 0:
        print("No employees available")
        return

    print(f"{'ID':<10} {'Name':<20} {'Age':<10} {'Department':<20} {'Salary':<10}")
    print('-' * 70)
    for emp_id, data in dict.items():
        print(f"{emp_id:<10} {data['name']:<15} {data['age']:<10} {data['department']:<20} {data['salary']:<10}")


def search_employee():
    emp_id = int(input("enter the employee ID you want to search for -> "))
    
    if emp_id in dict.keys():
        print('name -> ',dict[emp_id]['name'],'\n')
        print('age -> ',dict[emp_id]['age'],'\n')
        print('department -> ',dict[emp_id]['department'],'\n')
        print('salary -> ',dict[emp_id]['salary'],'\n')

    else:
        print('Employee not found')


ans = input('enter your choice -> ')
while(ans.lower() != 'exit' and ans != '4'):

    if(ans.lower() == 'add employee' or ans == '1'):
        print()
        add_emp()

    elif(ans.lower() == 'view all employees' or ans == '2'):
        print()
        view_employees()

    elif (ans.lower() == 'search for employee' or ans == '3'):
        print()
        search_employee()

    elif (ans.lower == 'exit' or ans == '4'):
        print("thank-you")
        exit()

    else:
        print("Invalid choice. Please try again.")

    print()
    option_menu()

    ans = input('enter your choice -> ')

