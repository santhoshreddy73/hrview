
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
User._meta.get_field('email')._null= True




##db tabel to store employee details
class employees(models.Model):
    name=models.CharField(max_length=400)
    temporary_role=models.CharField(max_length=200,null=True,blank=True)
    role=models.CharField(max_length=200)
    join_date=models.DateField(null=True,blank=True)
    annual_package=models.IntegerField(null=True)
    address=models.TextField(blank=False)
    appointmentletter_issued_on=models.DateTimeField(null=True,blank=True)
    termination_letter_issued=models.DateTimeField(null=True,blank=True)
    notice_period=models.CharField(null=True,blank=True,max_length=10)
    service_agreement_issued_date=models.DateTimeField(null=True,blank=True)
    letter_of_intent_issued_date=models.DateTimeField(null=True,blank=True) 
    penaulty=models.IntegerField(null=True,blank=True)
    traning_period=models.IntegerField(null=True,blank=True)
    offer_letter_issued_datetime=models.DateTimeField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    def __str__(self):
        return self.name
#custom user



#table to store the details of employe hike:i used manyToone  here because 1 employee can have many hike soo..
class Employees_hike (models.Model):

    employee=models.ForeignKey(employees,on_delete=models.CASCADE)
    hike=models.IntegerField()
    hike_letter_issued_date=models.DateTimeField(null=True,blank=True)
    hike_duration_start_year=models.DateField(null=True,blank=True)
    hike_duration_end_year=models.DateField(null=True,blank=True)
    path=path=models.CharField(max_length=400,null=True,blank=True) 

    def __str__(self):
        return self.employee.name+'hike worth'+str(self.hike)


#table to store all the activities
class records(models.Model):
    user=models.CharField(max_length=200)
    record=models.TextField()
    date=models.DateTimeField()

#table to records to the downloads triggered by the users
class download_records(models.Model):
    user=models.CharField(max_length=200)
    downloads=models.TextField()
    date=models.DateTimeField()

class Interns(models.Model):
    name=models.CharField(max_length=400)
    role=models.CharField(max_length=400)
    joinied_date=models.DateField()
    leaving_date=models.DateField()
    internship_letter_issue_date=models.DateTimeField()
    email=models.EmailField(null=True,blank=True)

class Appointment_Letters(models.Model):
    employee=models.OneToOneField(employees,on_delete=models.CASCADE)
    path=models.CharField(max_length=400,null=True,blank=True)
    

class Termination_Letters(models.Model):
    employee=models.OneToOneField(employees,on_delete=models.CASCADE)
    path=models.CharField(max_length=400,null=True,blank=True)
    

class Intent_Letters(models.Model):
    employee=models.OneToOneField(employees,on_delete=models.CASCADE)
    path=models.CharField(max_length=400,null=True,blank=True)
   

class Hike_letters(models.Model):
    employee=models.ForeignKey(employees,on_delete=models.CASCADE)
    path=models.CharField(max_length=400,null=True,blank=True)
    Created=models.DateTimeField(null=True,blank=True)
   

class Service_letters(models.Model):
    employee=models.OneToOneField(employees,on_delete=models.CASCADE)
    path=models.CharField(max_length=400,null=True,blank=True)
    

class test_store_files(models.Model):
    file=models.FileField()

class Intenship_certificates(models.Model):
    intern=models.OneToOneField(Interns,on_delete=models.CASCADE)
    path=models.CharField(max_length=400,null=True,blank=True)
    

class Offer_Letters(models.Model):
    employee=models.OneToOneField(employees,on_delete=models.CASCADE)
    path=models.CharField(max_length=400,null=True,blank=True)
    