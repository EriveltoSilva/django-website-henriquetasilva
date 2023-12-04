from django.shortcuts import render
from .models import Frequent_Question, Team
# Create your views here.
def home(request):
    return render(request, "website/home.html", {})
def about_me(request):
    return render(request, "website/about_me.html", {})
def candidacy(request):
    team_members = Team.objects.all()

    return render(request, "website/candidacy.html", {"team_members":team_members})
def faq(request):
    faqs = Frequent_Question.objects.filter(published=True)
    return render(request, "website/faq.html", {"faqs":faqs})

def news(request):
    return render(request, "website/news.html", {})
def contacts(request):
    return render(request, "website/contacts.html", {})