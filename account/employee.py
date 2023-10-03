class Employee:
    hourly_rate = 10
    __emp_counter = 0

    def __init__(self, emp_name: str):
        Employee.__emp_counter += 1
        self.__emp_id = Employee.__emp_counter
        self.__emp_name = emp_name
        self.__emp_department = None
        self.__number_of_hours_worked = 0

    def number_of_salary(self, number_of_hours_worked):
        if number_of_hours_worked > 0:
            number_of_hours_worked *= self.hourly_rate
            self.__number_of_hours_worked = number_of_hours_worked


    def get_emp_id(self):
        return self.__emp_id

    def get_number_of_salary(self):
        return self.__number_of_hours_worked

    def emp_assign_department(self, department):
        self.emp_department = department

    def get_emp_assign_department(self):
        return self.emp_department

    def print_employee_details(self):
        details = f"{self.__emp_id} {self.__emp_name} {self.__emp_department}"
        return details
