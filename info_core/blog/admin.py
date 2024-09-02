from django.contrib import admin
from blog.models import Publication, Category, Hashtag, ContactClient
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['title', 'created_date']
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name']

@admin.register(Hashtag)
class HashtagAdmin(TranslationAdmin):
    list_display = ['name']

@admin.register(ContactClient)
class ContactClient(admin.ModelAdmin):
    list_display = ['name']
