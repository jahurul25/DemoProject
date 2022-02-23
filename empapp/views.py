from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response 
from rest_framework.views import APIView
from empapp import serializers
from empapp import models


#User login API
class UserLogin(APIView): 
    def post(self, request):
        try:
            if request.data.get('username') and request.data.get('password'):
                username = (request.data.get('username')).lower()              
                password = request.data.get('password')

                user = authenticate(request, username=username, password=password)
                if user:       
                    refresh = RefreshToken.for_user(user)   
                    return Response({"message": "User login successful", "refresh": str(refresh), "access": str(refresh.access_token)}, status=200)
                else:
                    return Response({"message": "Login failed"}, status=400)
            else: 
                return Response({"message": "User not found", "user": "Username & password is mandatory"}, status=400)   
        except:
            return Response({"message": "Error", "data": None}, status=400)

#GET All Employee list & Employee Registration API
class EmployeeInfo(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.EmployeeSerializer

    def get(self, request):
        try:
            employee_list   = models.EmployeeInfo.objects.filter(status=True).order_by("designation")
            serializer = self.serializer_class(employee_list, many=True)
            return Response({"message": "Data found", "data": serializer.data}, status=200) 
        except:
            return Response({"message": "Error", "data": None}, status=400)

    def post(self, request, format='json'):
        try:
            emp_name    = request.data.get('emp_name') 
            mobile      = request.data.get('mobile') 
            email       = request.data.get('email') 
            designation = request.data.get('designation')
            report_to   = request.data.get('report_to')

            if emp_name and mobile and designation and report_to:
                check_employee = models.EmployeeInfo.objects.filter(mobile=mobile)
                if not check_employee:
                    models.EmployeeInfo.objects.create(emp_name = emp_name, mobile=mobile, email=email, designation=designation, report_to=report_to)
                    return Response({"message": "Employee registration successful!"}, status=200)
                else:
                    return Response({"message": "This mobile number already exist!"}, status=400)
            else:
                return Response({"message": "Employee registration failed!", "data": None}, status=400)
        except:
            return Response({"message": "Error", "data": None}, status=400)


#Find Employee By the Reporting Boss Designation ID
class FindEmployeeInfo(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.EmployeeSerializer

    def get(self, request, id): 
        try:
            employee_list   = models.EmployeeInfo.objects.filter(report_to=id, status=True).order_by("designation")
            if employee_list:
                serializer = self.serializer_class(employee_list, many=True)
                return Response({"message": "Data found", "data": serializer.data}, status=200) 
            else:
                return Response({"message": "Data not found", "data": None}, status=400) 
        except:
            return Response({"message": "Error", "data": None}, status=400)

#Employee List Show in HTML Page
def EmployeeList(request):
    try:
        employee_list   = models.EmployeeInfo.objects.filter(status=True).order_by("designation")

        context = {
            "employee_list": employee_list
        }

        return render(request, "employee_list.html", context)
    except:
        return render(request, "employee_list.html")