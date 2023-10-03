import unittest
from employee import Employee


class Employee_test(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee("IKENNA JAMES")
        self.employee2 = Employee("john john")
        self.employee3 = Employee("mikel")

    def test_employee_salary(self):
        self.employee.number_of_salary(8)
        self.assertEqual(80, self.employee.get_number_of_salary())

    def test_to_assign_department(self):
        self.employee.emp_assign_department("Packaging department")
        self.assertEqual("Packaging department", self.employee.get_emp_assign_department())

    def test_that_u_can_print_employee(self):
        details = "1 IKENNA JAMES None"
        self.assertEqual(details, self.employee.print_employee_details())
        details = "2 john john None"
        self.assertEqual(details, self.employee2.print_employee_details())

    def test_i_can_get_id(self):
        self.assertEqual(self.employee.get_emp_id(), 1)
        self.assertEqual(self.employee2.get_emp_id(), 2)
        self.assertEqual(self.employee3.get_emp_id(), 3)
