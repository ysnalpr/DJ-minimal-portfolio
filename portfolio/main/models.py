from django.db import models


class About(models.Model):
    image = models.ImageField(upload_to="media/about")
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    years_of_work = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)
    resume_file = models.FileField(upload_to="media/about")

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
