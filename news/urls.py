from django.urls import path
from django.conf.urls import  url
from django.views.generic import TemplateView
from news.views import scrape, news_list,scrape_malayalam, login, account, register, logout, malayalam_login,english_login,english_india, malayalam_india_login,search
urlpatterns = [
  path('', scrape, name="scrape"),
  path('newslist', news_list, name="home"),
  # path('news_malayalam/', scrape_malayalam, name="scrape_malayalam"),
  path('login', login, name="login"),
  path('account/', account, name = 'account'),
  path('register/', register, name = 'register'),
  path('logout/', logout, name = 'logout'),
  path('malayalam_login', malayalam_login, name="malayalam_login"),
  path('malayalam_india_login', malayalam_india_login, name="malayalam_india_login"),
  path('english_login', english_login, name="english_login"),
  path('english_india', english_india, name="english_india"),
  path('search', search, name="search"),

  
]