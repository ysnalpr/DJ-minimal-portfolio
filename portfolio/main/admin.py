from django.contrib import admin
from .models import Contact, Social, About


class SocialInline(admin.StackedInline):
    model = Social


class ContactInline(admin.StackedInline):
    model = Contact


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["name", "job_title"]
    inlines = [SocialInline, ContactInline]
