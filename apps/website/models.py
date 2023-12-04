from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Frequent_Question(models.Model):
    question = models.TextField(null=False, blank=False)
    slug = models.SlugField()
    answer = models.TextField(null=False, blank=False)
    author = models.ForeignKey(to=User, on_delete=models.PROTECT, null=False, related_name="frenquent_questions")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id","-created_at"]
    
    def __str__(self) -> str:
        return f"{self.question}"
    
    def get_absolute_url(self):
        return reverse('faqs')


class News_Category(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    summary = models.TextField(null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    image_thumb = models.ImageField(upload_to="website/news_categories/", blank=True)
    image_description = models.CharField(max_length=75, default="Imagem de noticia",blank=True)
    author = models.ForeignKey(to=User, on_delete = models.PROTECT, null=True, related_name='new_category')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('news')

class New(models.Model):
    # type_option =[("DESENVOLVIMENTO WEB", "Desenvolvimento Web"), ("CHAT BOTS", "Chat Bots"),("SOLUCOES DE INTEGRACAO", "Soluções de Integração"), ("SOLUCOES DE IA", "Soluções de Ia COM LLM"),]
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    summary = RichTextField()
    content = RichTextUploadingField()
    category = models.ForeignKey(to=News_Category, on_delete=models.CASCADE, null=False, default='',related_name='new')
    image_thumb = models.ImageField(upload_to="website/news/", blank=True)
    image_description = models.CharField(max_length=75, default="Imagem de noticia",blank=True)
    author = models.ForeignKey(to=User, on_delete=models.PROTECT, null=True, related_name='service')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    # def get_absolute_url(self):
    #     return reverse('news-detail', args=[str(self.id)])

class Team(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    function = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to="website/team/", blank=False)
    image_description = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.name}"
    
# class Contact(models.Model):
    # name = models.CharField(max_length=150)
    # email = models.CharField(max_length=255)
    # subject = models.CharField(max_length=255)
    # message = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    
# class Meeting(models.Model):
#     options = [("AGENDADA", "Agendada"),("CANCELADA", "Cancelada"), ("ESPERANDO RESPOSTA","Esperando Resposta"),("REALIZADA", "Realizada")]
    
#     requester = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default="Anônimo(del)")
#     content = models.TextField(null=False, blank=False)
#     date_meeting = models.DateTimeField(null=False, blank=False)
#     location_meeting = models.CharField(max_length=255, null=True, blank=True)
#     status = models.CharField(max_length=255, choices=options,default='')
#     attendant = models.ForeignKey(to=User, on_delete=models.PROTECT,  related_name="meetings")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self) -> str:
#         return f"{self.requester.first_name}"


    

# class Portfolio(models.Model):    
#     title = models.CharField(max_length=100, null=False, blank=False)
#     summary =  models.CharField(max_length=100, null=False, blank=False)
#     image_thumb = models.ImageField(upload_to="app_site/portfolio/", blank=True)
#     def __str__(self) -> str:
#         return f"{self.title}"
