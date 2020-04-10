from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language

class ToolsAndTech(models.Model):
    tools_and_tech = models.CharField(max_length=50)

    def __str__(self):
        return self.tools_and_tech

class Course(models.Model):
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.course

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    certificate_photo = models.ImageField()
    source = models.CharField(max_length=50)

    def __str__(self):
        return self.title