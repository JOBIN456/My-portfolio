from django.db import models

# Create your models here.
class Links(models.Model):
    git=models.URLField(max_length=300,blank=True)
    linkedin=models.URLField(max_length=300,blank=True)
    email=models.EmailField(max_length=300,blank=True)
    phone=models.CharField(max_length=13,blank=True)
    name=models.TextField(max_length=200,blank=False)
    image=models.ImageField(upload_to='images/')
    position=models.TextField(max_length=200,blank=False)
    detail=models.TextField(max_length=700,blank=False)
    cv=models.FileField(upload_to='pdf/')
    about=models.TextField(max_length=800,blank=False)

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    skill=models.TextField(max_length=100,blank=False)
    skill_image=models.ImageField(upload_to='images/')


    def __str__(self):
        return self.skill


class Projects(models.Model):
    project_name=models.TextField(max_length='200',blank=False)
    Front_end=models.TextField(max_length='200',blank=False)
    Back_end=models.TextField(max_length='200',blank=False)
    Framework=models.TextField(max_length='200',blank=False)
    Database=models.TextField(max_length='200',blank=False)
    project_url=models.URLField(max_length=500,blank=False)

    def __str__(self):
        return self.project_name



    