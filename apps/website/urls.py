from django.urls import path
from .views import home, about_me, candidacy, faq, contacts, news
urlpatterns = [
    path('', home, name="home"),
    path('sobre/', about_me, name="about-me"),
    path('candidatura/', candidacy, name="candidacy"),
    path('perguntas-frequentes/', faq, name="faq"),
    path('contactos/', contacts, name="contacts"),
    path('noticias/', news, name="news"),
]