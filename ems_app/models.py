# ems_app/models.py

from django.contrib.auth.models import User
from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=255,default=1)
    def __str__(self):
        return self.name
class Module(models.Model):
    name = models.CharField(max_length=255)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    question = models.TextField()
    image = models.ImageField(upload_to='topic_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class EmployeeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, related_name='employeeuser')
    name = models.CharField(max_length=255,default=1)
    phone=models.CharField(max_length=10,default=1)
    email=models.EmailField(default=1)
    def __str__(self):
        return self.name

class InternUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1, related_name='internuser')
    username = models.CharField(max_length=255,default=1)
    phone=models.CharField(max_length=10,default=1)
    email=models.EmailField(default=1)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.username
    
class InternAnswer(models.Model):
    intern_user = models.ForeignKey(InternUser, on_delete=models.CASCADE, related_name='intern_answer')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    answer_text = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intern_user.username}'s answer for {self.module.name}"