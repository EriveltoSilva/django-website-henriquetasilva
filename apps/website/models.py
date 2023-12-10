from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class FrequentQuestion(models.Model):
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


class NewsCategory(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField()
    description = models.TextField(null=False, blank=False)
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
    category = models.ForeignKey(to=NewsCategory, on_delete=models.CASCADE, null=False, default='',related_name='new')
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

    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["email", "name",]

    def __str__(self) -> str:
        return f"{self.email}"
    


    
class Galeria(models.Model):    
    image = models.ImageField(upload_to="website/galeria/", blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    image_description =  models.CharField(max_length=255, default="")
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at",]
    
    def __str__(self) -> str:
        return f"{self.title}"
    
class Carrocel(models.Model):
    choice_page = (("HOME","HOME"), ("SOBRE", "SOBRE"), ("CANDIDATURA", "CANDIDATURA"), ("NOTICIAS", "NOTICIAS"))
    image = models.ImageField(upload_to="website/galeria/", blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    local = models.CharField(max_length=25,choices=choice_page, null=False, blank=False)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at",]

    def __str__(self) -> str:
        return f"{self.title}"
    
class Comment(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=125, null=False, blank=False)
    content = models.TextField(max_length=255, null=False, blank=False)
    published = models.BooleanField(default=True)
    new = models.ForeignKey(to=New, on_delete=models.CASCADE, related_name='post_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Comentário do {self.name}"
    
class NewletterAssinature(models.Model):
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.email}"
    

class Team(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(default="")
    # function = models.CharField(max_length=200, default="")
    num_hierarquical= models.IntegerField(null=False, blank=False, default=0)
    image = models.ImageField(upload_to="website/team/", blank=False)
    image_description = models.CharField(max_length=100, default="")
    content = RichTextUploadingField(default="")
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["num_hierarquical","name"]

    def __str__(self) -> str:
        return f"{self.name}"