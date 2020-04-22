from django.urls import path
from django.conf.urls import  url
from django.views.generic import TemplateView
from news.views import scrape, news_list,scrape_malayalam,\
  login, account, register, logout, malayalam_login,english_login,\
  english_india, malayalam_india_login,search,search_news,search_view,scrape_malayalam_movie,\
  malayalam_movie_login,scrape_malayalam_tech,malayalam_tech_login,malayalam_sports_login,\
  scrape_malayalam_sports,english_tech_scrape,english_tech_login,english_sports_scrape,\
  english_sports_login,english_movie_scrape,english_movie_login
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
  path('malayalam_movie_login', malayalam_movie_login, name="malayalam_movie_login"),
  path('malayalam_tech_login', malayalam_tech_login, name="malayalam_tech_login"),
  path('malayalam_sports_login', malayalam_sports_login, name="malayalam_sports_login"),
  path('english_login', english_login, name="english_login"),
  path('english_india', english_india, name="english_india"),
  path('english_tech_login', english_tech_login, name="english_tech_login"),
  path('english_sports_login', english_sports_login, name="english_sports_login"),
  path('english_movie_login', english_movie_login, name="english_movie_login"),
  path('search', search, name="search"),
  path('search_news', search_news, name="search_news"),
  path('search_view', search_view, name="search_view"),

  
]