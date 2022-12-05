
class Employee:
    def __init__(self,firstName,lastName,idNumber,hours,wage):
        self.FirstName = firstName
        self.LastName = lastName
        self.IDNumber = idNumber
        self.HoursWorked = hours
        self.Wage = wage



def WeeklyPay(self):
    if(self.HoursWorked > 40):
        return (40 * self.Wage) + (self.HoursWorked - 40) * 1.5 * self.Wage
    else:
        return self.HoursWorked * self.Wage


file = open("10.06 Payroll.txt")
employees =[] 

for i in range(3):
    line = file.readline()
    lineData = line.strip().split(',')
    emp = Employee(lineData[0].strip(),lineData[1].strip(),int(lineData[2].strip()),float(lineData[3].strip()),float(lineData[4].strip()))
    employees.append(emp) 

print('{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("First","Last","ID","Hours","Hourly","Weekly"))
print('{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Name","Name","Number","Worked","Wage","Pay"))

for emp in employees:
    print('{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format(emp.FirstName,emp.LastName,emp.IDNumber,emp.HoursWorked,emp.Wage,round(emp.WeeklyPay(),2)))