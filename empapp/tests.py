import email
import django
from django.test import TestCase
from django.contrib.auth import get_user_model
from empapp import models

# Create your tests here.

User = get_user_model()
class UserTestCast(TestCase):
    
    def test_employee(self):
        emp = models.EmployeeInfo()
        emp.emp_name = "Mr. Jaman"
        emp.mobile = "01234567892"
        emp.email = "jaman123@gmail.com"
        emp.designation = "2"
        emp.report_to = "1"

        self.assertEqual(emp.emp_name, "Mr. Jaman")

