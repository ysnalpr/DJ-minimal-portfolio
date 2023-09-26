from django.contrib import admin
from .models import Contact, Social, About, Project, Skill


class SocialInline(admin.TabularInline):
    model = Social


class ContactInline(admin.TabularInline):
    model = Contact


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["name", "job_title"]
    inlines = [SocialInline, ContactInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "link"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["title", "level"]
