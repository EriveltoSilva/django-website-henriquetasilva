from django.contrib import admin
from .models import Frequent_Question, Team

class Frequent_QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', "question", "author", "published","created_at",]
    list_display_links = ["id", "question", "created_at"]
    list_filter = ["id", "question", "author","created_at"]

    prepopulated_fields = {"slug":("question",)}



class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "function", "created_at",]
    list_display_links = ["id", "name","function", "created_at"]
    list_filter = ["id", "name", "function","created_at"]

    prepopulated_fields = {"image_description":("name",)}
    
admin.site.register(Frequent_Question, Frequent_QuestionAdmin)
admin.site.register(Team, TeamAdmin)