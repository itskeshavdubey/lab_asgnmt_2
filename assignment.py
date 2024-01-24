class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def sort_table(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter.")

    def display_table(self):
        for emp in self.employees:
            print(emp)

if __name__ == "__main__":
    employee_table = EmployeeTable()

    employee_table.add_employee(Employee("161E90", "Ramu", 35, 59000))
    employee_table.add_employee(Employee("171E22", "Tejas", 30, 82100))
    employee_table.add_employee(Employee("171G55", "Abhi", 25, 100000))
    employee_table.add_employee(Employee("152K46", "Jaya", 32, 85000))

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    sorting_parameter = int(input("Enter your choice (1/2/3): "))

    employee_table.sort_table(sorting_parameter)
    print("\nSorted Employee Table:")
    employee_table.display_table()
    
    print("\nEnd")
    print("\n Keshav Dubey | 2110110687")