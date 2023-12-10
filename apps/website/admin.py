from django.contrib import admin
from .models import FrequentQuestion, Team
from .models import NewsCategory, New
from .models import Contact, Galeria, Carrocel

class ListFrequentQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', "question", "author", "published","created_at",]
    list_display_links = ["id", "question", "created_at"]
    list_filter = ["id", "question", "author","created_at"]

    prepopulated_fields = {"slug":("question",)}



class ListTeamAdmin(admin.ModelAdmin):
    list_display = ['id', "name","num_hierarquical", "function", "published", "created_at",]
    list_display_links = ["id", "name","function", "created_at"]
    list_filter = ["id", "name", "function","created_at"]

    prepopulated_fields = {"image_description":("name",)}


class ListNewsCategories(admin.ModelAdmin):
    list_display = ('id', 'title', 'published','author', 'created_at')
    list_display_links = ('id', 'title', 'author',)
    search_fields =('title', 'description', 'author')
    list_filter = ('published', 'created_at', 'updated_at', )
    list_editable = ('published',)
    list_per_page = 10

    prepopulated_fields = {"slug":("title",)}

class ListNews(admin.ModelAdmin):
    list_display = ('id', 'title', 'published','category','author',)
    list_display_links = ('id','title', 'author',)
    search_fields =('title', 'summary', 'content', 'image_thumb','author', 'created_at', 'updated_at',)
    list_filter = ('published', 'category', 'author','created_at','updated_at')
    list_editable = ('published',)
    list_per_page = 10

    prepopulated_fields = {"slug":("title",)}
class ListContacts(admin.ModelAdmin):
    list_display = ('name', 'email','subject', 'created_at')
    list_display_links = ('name','email', )
    search_fields = ('name','email', 'created_at', )
    list_filter = ('name', 'email', 'created_at')
    list_per_page = 10

class ListGaleries(admin.ModelAdmin):
    list_display = ('id', 'title','published', 'created_at',)
    list_display_links = ('id','title', 'created_at',)
    search_fields = ('title','image_description', 'created_at', )
    list_filter = ('title',  'created_at',)
    list_per_page = 10

class ListCarrocel(admin.ModelAdmin):
    list_display = ('id', 'title','published', 'local','created_at',)
    list_display_links = ('id','title', 'local','created_at',)
    search_fields = ('title','local', 'published','created_at', )
    list_filter = ('title',  'local',)
    list_per_page = 10

admin.site.register(FrequentQuestion, ListFrequentQuestionAdmin)
admin.site.register(Team, ListTeamAdmin)
admin.site.register(NewsCategory, ListNewsCategories)
admin.site.register(New, ListNews)
admin.site.register(Contact, ListContacts)
admin.site.register(Galeria, ListGaleries)
admin.site.register(Carrocel, ListCarrocel)