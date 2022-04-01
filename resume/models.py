from django.db import models


class ProfileSkills(models.Model):
    p_skill = models.CharField(max_length=20)
    def __str__(self):
        return self.p_skill

class Header(models.Model):
    profile_pic = models.ImageField(upload_to='images')
    profile_name = models.CharField(max_length=20)
    profile_skills = models.ForeignKey(ProfileSkills, on_delete=models.CASCADE)
    p_phone = models.CharField(max_length=15)
    p_email = models.EmailField()
    def __str__(self):
        return self.profile_name


class About(models.Model):
    myself = models.TextField(max_length=2000)
    def __str__(self):
        return self.myself

class Skill(models.Model):
     s_name = models.CharField(max_length=50)
     s_percentage = models.IntegerField()
     def __str__(self):
         return  self.s_name

class Education(models.Model):
    degree_title = models.CharField(max_length=50)
    degree_name = models.CharField(max_length=50)
    university_name = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
    obtained_marks = models.FloatField()
    total_marks = models.FloatField()
    project = models.TextField(default=False)
    def __str__(self):
        return  self.degree_name


class Experience(models.Model):
     institution = models.CharField(max_length=50)
     work_as = models.CharField(max_length=50)
     start_date = models.DateField()
     end_date = models.DateField()
     desc = models.TextField(max_length=500)
     def __str__(self):
         return  self.work_as



class Certification(models.Model):
     short_form = models.CharField(max_length=30)
     full_name = models.CharField(max_length=100)
     start_date = models.DateField()
     end_date = models.DateField()
     desc = models.TextField(max_length=1000)
     def __str__(self):
         return  self.short_form


class Address(models.Model):
     address = models.TextField(max_length=500)
     phone = models.TextField(max_length=20)
     email = models.EmailField()
     def __str__(self):
         return  self.address


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.TextField(max_length=50)
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.email

class MyProject(models.Model):
    p_name = models.CharField(max_length=50)
    p_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.p_name




