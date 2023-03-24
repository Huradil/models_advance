from django.db import models
from datetime import date


class AbstractPerson(models.Model):
    name=models.CharField(max_length=20)
    birth_date=models.DateField()

    def get_age(self):
        today=date.today()
        age=self.birth_date.year-today.year
        return age

    class Meta:
        abstract=True


class Employee(AbstractPerson):
    position=models.CharField(max_length=20)
    salary=models.IntegerField()
    work_experience=models.DateField()


class Password(models.Model):
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE)
    inn=models.CharField(max_length=16)
    id_card=models.CharField(max_length=9)

    def get_gender(self):
        if self.inn.startswith('1'):
            return "Male"
        return "Female"



class WorkProject(models.Model):
    project_name=models.CharField(max_length=30)
    members=models.ManyToManyField(Employee,related_name='work_projects',through='Membership')


class Membership(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    WorkProject=models.ForeignKey(WorkProject,on_delete=models.CASCADE)
    date_joined=models.DateField()


class Client(AbstractPerson):
    address=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=12)


class VIPClient(Client):
    vip_status_start=models.DateField()
    donation_amount=models.IntegerField()


