from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name','employee_email','employee_contact','employee_address','employee_image']

        # def clean_employee_image(self):
        #     pimage = self.cleaned_data.get("employee_image")
        #     if image:
        #         max_size = 2 * 1024 * 1024  
        #         if image.size > max_size:
        #             raise forms.ValidationError("File size should not exceed 2MB.")
        #     return image
    
    
