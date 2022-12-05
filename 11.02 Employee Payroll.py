class Employee:
    def __init__(self,first_name,last_name, id_number, wage):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.wage = wage
        self.hours_worked = 0

def set_hours_worked(self,hours_worked):
    self.hours_worked = hours_worked

def WeeklyPay(self):
    if(self.hours_worked <=40):
        return self.wage * self.hours_worked
    else:
        return 40 * self.wage + 1.5 * (self.hours_worked-40) * self.wage

def find_employee(empList, employeeId):
    for i in range(len(empList)):
        if(empList[i].id_number == employeeId):
            return i
        return -1

def load_employees():
    f = open("Employees.txt","r")
    employees = []
    line = f.readline()
    while(line):
        line = line.strip()
        data = line.split(',')
    if(len(data) == 4):
        first_name = data[0]
        last_name = data[1]
        id_number = int(data[2])
        wage = float(data[3])
        emp = Employee(first_name,last_name,id_number,wage)
        employees.append(emp)
        line = f.readline()
        return employees

def update_employees(empList):
    f = open("Hours.txt","r")
    line = f.readline()
    while(line):
        line = line.strip()
        data = line.split(',')
    if(len(data) == 2):
        employee_id = int(data[0])
        hours_worked = int(data[1])
        ind = find_employee(empList,employee_id)
    if(ind == -1):
        print("\nUnable to find employee id:",employee_id)
    else:
        empList[ind].set_hours_worked(hours_worked)
        line = f.readline()

def displayEmployees(empList):
    print("\n{0:>20} {1:>20} {2:>20} {3:>20} {4:>20} {5:>20}\n".format("First Name","Last Name","ID Number","Hours Worked","Hourly Wage","Weekly Pay"))
    for emp in empList:
        print("\n{0:>20} {1:>20} {2:>20} {3:>20.2f} {4:>20.2f} {5:>20.2f}\n".format(emp.first_name, emp.last_name, emp.id_number, emp.hours_worked, emp.wage, emp.WeeklyPay()))
def main():
    empList = load_employees()
    update_employees(empList)
    displayEmployees(empList)
    if __name__ == "__main__":
        main()