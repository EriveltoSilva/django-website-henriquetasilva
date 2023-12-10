from django.db.models import Q
from django.db import models
from django.contrib import messages
from .emails import send_email_contact
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import FrequentQuestion, Team, Contact, Carrocel, Galeria, New, NewsCategory, Comment

# Create your views here.

def filter_by_category(request, slug):
    category = get_object_or_404(NewsCategory, slug=slug)
    carrocel = Carrocel.objects.filter(Q(local="NOTICIAS"))
    news = New.objects.filter(published=True,category=category)

    return render(request, "website/news.html", {"page_name":"news","carrocel":carrocel, "news":news})


def news_article(request, slug):
    new = get_object_or_404(New, slug=slug)

    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        if comment == None or comment=="":
            messages.error(request, f"O comentário está vázio")
        elif name == None or name=="":
            messages.error(request, f"O seu nome não foi inserido.")
        elif email == None or email=="":
            messages.error(request, f"O seu email não foi inserido.")
        else:
            messages.success(request, f"Comentário Públicado")
            comment = Comment(new=new, email=email,name=name, content=comment)
            comment.save()

    categories = NewsCategory.objects.filter(published=True)
    recent_news = New.objects.filter(published=True)[:10]
    comments = Comment.objects.order_by('-created_at').filter(published = True, new=new).annotate(num_comments = models.Count('new'))
    num_comments = len(comments)

    return render(request, "website/news-single.html", {"page_name":"news", "num_comments":num_comments,"new": new, "categories":categories, "comments":comments, "recent_news":recent_news}) 

def news(request):
    carrocel = Carrocel.objects.filter(Q(local="NOTICIAS"))
    news = New.objects.filter(published=True)

    return render(request, "website/news.html", {"page_name":"news","carrocel":carrocel, "news":news})

def home(request):
    carrocel = Carrocel.objects.filter(local="HOME")
    image_about = Carrocel.objects.filter(local="SOBRE")[0]
    galeria = Galeria.objects.filter(published=True)[:10]
    news = New.objects.filter(published=True)[:10]

    return render(request, "website/home.html", {"page_name":"home", "carrocel":carrocel, "image_about":image_about, "galeria":galeria, "news": news})

def candidacy(request):
    carrocel = Carrocel.objects.filter(local="CANDIDATURA")
    team_members = Team.objects.all()
    return render(request, "website/candidacy.html", {"page_name":"candidacy","carrocel":carrocel,"team_members":team_members, "page_name":"candidacy"})


def about_me(request):
    image = Carrocel.objects.filter(local="SOBRE")[0]
    return render(request, "website/about_me.html", {"page_name":"about_me", "image":image})
    

def faq(request):
    faqs = FrequentQuestion.objects.filter(published=True)
    return render(request, "website/faq.html", {"faqs":faqs, "page_name":"faqs"})

def contacts(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        send_email_contact(name=name, email=email, subject=subject, message=message)
        messages.success(request, f"Email Enviado com Sucesso! Entraremos em contacto o mais breve possível")
        return render(request, 'website/contacts.html', {"page_name":"contacts", "message":messages})

    return render(request, "website/contacts.html", {"page_name":"contacts"})