from django.urls import path
from .views import home, about_me, candidacy, faq, contacts, news, news_article, filter_by_category, newsletter,team_member
urlpatterns = [
    path('', home, name="home"),
    path('sobre/', about_me, name="about-me"),
    path('candidatura/', candidacy, name="candidacy"),
    path('perguntas-frequentes/', faq, name="faq"),
    path('contactos/', contacts, name="contacts"),
    path('noticias/', news, name="news"),
    path('noticias/<slug:slug>', news_article, name="news-article"),
    path('noticias/categorias/<slug:slug>', filter_by_category, name="filter-category-new"),
    path('subscrever-newsletter/', newsletter, name="newsletter"),
    path('candidatura/membro-de-equipe/<slug:slug>', team_member, name="team-member-detail"),
]