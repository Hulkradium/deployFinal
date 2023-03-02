from django.contrib import admin
from .models import Lecturer,Student,Intervention,Severity

# Register your models here.
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Intervention)
admin.site.register(Severity)