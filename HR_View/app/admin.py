from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(employees)
admin.site.register(Appointment_Letters)
admin.site.register(test_store_files)
admin.site.register(Interns)