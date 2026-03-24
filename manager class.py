class Person:
    def __init__(self, name, age):
        """Initialize the person's name and age."""
        self.name = name
        self.age = age

    def display_person_info(self):
       
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        """Initialize employee attributes including those from Person."""
        super().__init__(name, age)  # Call the constructor of Person
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        
        print(f"Employee ID: {self.employee_id}, Salary: ${self.salary:.2f}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
       super().__init__(name, age, employee_id, salary)  # Call the constructor of Employee
        self.department = department

    def display_manager_info(self):
        self.display_person_info()   # Call method from Person
        self.display_employee_info() # Call method from Employee
        print(f"Department: {self.department}")


manager1 = Manager("Alice Johnson", 40, "MGR102", 85000, "IT")


print("Manager Information:")
manager1.display_manager_info()
