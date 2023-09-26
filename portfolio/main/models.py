import os
from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        # set filename as random string
        filename = "{}.{}".format(instance.id, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


path_and_rename = PathAndRename("about/")
projects_img_rename = PathAndRename("projects/")


class About(models.Model):
    image = models.ImageField(upload_to=path_and_rename)
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    years_of_work = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)
    resume_file = models.FileField(upload_to=path_and_rename)

    def __str__(self):
        return self.name


class Social(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField(max_length=500)
    icon = models.CharField(max_length=100)
    about = models.ForeignKey(About, related_name="socials", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=1000)
    icon = models.CharField(max_length=100)
    about = models.ForeignKey(About, related_name="contacts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return self.title


class Project(models.Model):
    image = models.ImageField(upload_to=projects_img_rename)
    subtitle = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        indexes = [models.Index(fields=["-created"])]

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=20)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.title
