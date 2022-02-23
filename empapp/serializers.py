from rest_framework import serializers
from django.contrib.auth import get_user_model
from empapp import models
 
User = get_user_model()

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','is_superuser','is_active','is_staff','date_joined')

class EmployeeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.EmployeeInfo
        fields = ('id','emp_name','mobile','email','get_designation_display')
