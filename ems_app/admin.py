# ems_app/admin.py

from django.contrib import admin
from .models import Domain, EmployeeUser, InternUser, Module,InternAnswer

admin.site.register(Domain)
admin.site.register(EmployeeUser)
admin.site.register(InternUser)
admin.site.register(Module)
admin.site.register(InternAnswer)

