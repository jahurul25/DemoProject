from django.db import models

# Create your models here.


class EmployeeInfo(models.Model):  
    emp_name      = models.CharField(max_length=50, verbose_name="Full Name")
    mobile        = models.CharField(max_length=20, unique=True, verbose_name="Mobile Number")
    email         = models.CharField(max_length=20, verbose_name="Email Address", blank=True, null=True)
    designation_type = (
        ("1", "CTO"), 
        ("2", "Senior Software Eng"), 
        ("3", "Software Eng")
    ) 
    designation   = models.CharField(max_length=1, choices=designation_type, verbose_name="Designation")
    report_to     = models.CharField(max_length=1, choices=designation_type, verbose_name="Report To")
    created       = models.DateTimeField(auto_now_add=True)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return str(self.emp_name)
    
    class Meta:
        managed = True
        db_table = "employee_info"
        verbose_name_plural = "Employee Info"

