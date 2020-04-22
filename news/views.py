#!/usr/bin/python
# -*- coding: utf_8 -*-
import unicodedata
from django.shortcuts import render
import os
# Create your views here.
import requests
import re
from django.shortcuts import render, redirect
from datetime import  date
import datetime
from bs4 import BeautifulSoup as BSoup
from news.models import Headline, Malayalam_Headline, Search
from news.models import Users
requests.packages.urllib3.disable_warnings()
import time
def scrape(request):
    date_english = date.today()
    headline_existing = Headline.objects.all()
    check_date=Headline.objects.filter(date=date_english).exists()
    print(check_date)
    if headline_existing:
        if not  check_date:
            # date_english = date.today()
            # a = c.date
            # print(a)
            # print('----')
            # print(date_english)
            # if a != date_english:
                session = requests.Session()
                session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
                url = "https://indianexpress.com/section/cities/"
                content = session.get(url, verify=False).content
                soup = BSoup(content, "html.parser")
                News = soup.find_all('div', {"class": "articles"})

                for artcile in News:

                    main = artcile.find_all('a')[0]
                    link = main['href']
                    print(link)
                    try:
                        image_src = str(main.find('img')['data-lazy-src'])
                        print(image_src)
                    except:
                        pass

                    title = artcile.find('h2').text
                    print(title)
                    content = artcile.find('p').text

                    new_headline = Headline()
                    new_headline.title = title
                    new_headline.url = link
                    new_headline.language = 1
                    new_headline.category = 1
                    new_headline.image = image_src
                    new_headline.content = content

                    # new_headline.date = date_english
                    new_headline.save()
                return scrape_malayalam(request)

        print('db not empty')

        return news_list(request)
    else:
        print('empty')
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://indianexpress.com/section/cities/"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News = soup.find_all('div', {"class": "articles"})

        for artcile in News:
            main = artcile.find_all('a')[0]
            link = main['href']
            print(link)
            try:
                image_src = str(main.find('img')['data-lazy-src'])
                print(image_src)
            except:
                pass
            title = artcile.find('h2').text
            print(title)

            content = artcile.find('p').text

            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.language = 1
            new_headline.category = 1
            new_headline.image = image_src
            new_headline.content = content
            # new_headline.check = 'eng' + str(date.today())
            # new_headline.date = date_english
            new_headline.save()
        return scrape_malayalam(request)
    return news_list(request)
def scrape_malayalam(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.manoramaonline.com/news/latest-news.html"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class": "story-content-blk"})

    for artcile in News:
        main = artcile.find_all('a')[0]
        link = main['href']
        #         print(link)
        image_src = 'https://www.manoramaonline.com/' + str(main.find('img')['data-src-mobile'])
        #         print(image_src)
        titles = artcile.find_all('a')[1]
        title = titles['title']
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 2
        new_headline.category = 1
        new_headline.image = image_src
        new_headline.content = content

        new_headline.save()


    return scrape_malayalam_movie(request)

def scrape_malayalam_movie(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.manoramaonline.com/movies/movie-news.html"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class": "story-content-blk"})

    for artcile in News:
        main = artcile.find_all('a')[0]
        link = main['href']
        #         print(link)
        image_src = 'https://www.manoramaonline.com/' + str(main.find('img')['data-src-mobile'])
        #         print(image_src)
        titles = artcile.find_all('a')[1]
        title = titles['title']
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 2
        new_headline.category = 3
        new_headline.image = image_src
        new_headline.content = content

        new_headline.save()


    return scrape_malayalam_tech(request)
def scrape_malayalam_tech(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.manoramaonline.com/technology/technology-news.html"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class": "story-content-blk"})

    for artcile in News:
        main = artcile.find_all('a')[0]
        link = main['href']
        #         print(link)
        image_src = 'https://www.manoramaonline.com/' + str(main.find('img')['data-src-mobile'])
        #         print(image_src)
        titles = artcile.find_all('a')[1]
        title = titles['title']
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 2
        new_headline.category = 4
        new_headline.image = image_src
        new_headline.content = content

        new_headline.save()


    return scrape_malayalam_sports(request)

def scrape_malayalam_sports(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.manoramaonline.com/sports/local-sports.html"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class": "story-content-blk"})

    for artcile in News:
        main = artcile.find_all('a')[0]
        link = main['href']
        #         print(link)
        image_src = 'https://www.manoramaonline.com/' + str(main.find('img')['data-src-mobile'])
        #         print(image_src)
        titles = artcile.find_all('a')[1]
        title = titles['title']
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 2
        new_headline.category = 5
        new_headline.image = image_src
        new_headline.content = content

        new_headline.save()


    return scrape_malayalam_india(request)
def scrape_malayalam_india(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.manoramaonline.com/news/india.html"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class": "story-content-blk"})

    for artcile in News:
        main = artcile.find_all('a')[0]
        link = main['href']
        #         print(link)
        image_src = 'https://www.manoramaonline.com/' + str(main.find('img')['data-src-mobile'])
        #         print(image_src)
        titles = artcile.find_all('a')[1]
        title = titles['title']
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 2
        new_headline.category = 2
        new_headline.image = image_src
        new_headline.content = content

        new_headline.save()


    return english_india_scrape(request)

def english_india_scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url_india = "https://indianexpress.com/section/india/"
    content = session.get(url_india, verify=False).content
    soup = BSoup(content, "html.parser")

    News = soup.find_all('div', {"class": "articles"})
    for artcile in News:
        image_src = ""
        main = artcile.find_all('a')[0]
        link = main['href']
        #     print(link)
        images = main.find_all('img', {'src': re.compile('.jpg')})
        for image in images:
            #         print(image['src']+'\n')
            image_src = image['src']
            print(image_src)
        title = artcile.find('h2').text
        print(title)
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 1
        new_headline.category = 2
        new_headline.image = image_src
        new_headline.content = content
        # new_headline.check = 'eng' + str(date.today())
        new_headline.save()

    return english_tech_scrape(request)
def english_tech_scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url_india = "https://indianexpress.com/section/tech-news-technology/"
    content = session.get(url_india, verify=False).content
    soup = BSoup(content, "html.parser")

    News = soup.find_all('div', {"class": "articles"})
    for artcile in News:
        image_src = ""
        main = artcile.find_all('a')[0]
        link = main['href']
        #     print(link)
        images = main.find_all('img', {'src': re.compile('.jpg')})
        for image in images:
            #         print(image['src']+'\n')
            image_src = image['src']
            print(image_src)
        title = artcile.find('h2').text
        print(title)
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 1
        new_headline.category = 4
        new_headline.image = image_src
        new_headline.content = content
        # new_headline.check = 'eng' + str(date.today())
        new_headline.save()

    return english_sports_scrape(request)
def english_sports_scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url_india = "https://indianexpress.com/section/sports/"
    content = session.get(url_india, verify=False).content
    soup = BSoup(content, "html.parser")

    News = soup.find_all('div', {"class": "articles"})
    for artcile in News:
        image_src = ""

        main = artcile.find_all('a')[0]
        link = main['href']
        #     print(link)
        images = main.find_all('img', {'src': re.compile('.jpg')})
        for image in images:
            #         print(image['src']+'\n')
            image_src = image['src']
            print(image_src)
        title = artcile.find('h2').text
        print(title)
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 1
        new_headline.category = 5
        new_headline.image = image_src
        new_headline.content = content
        # new_headline.check = 'eng' + str(date.today())
        new_headline.save()

    return english_movie_scrape(request)

def english_movie_scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url_india = "https://indianexpress.com/section/entertainment/bollywood/box-office-collection/"
    content = session.get(url_india, verify=False).content
    soup = BSoup(content, "html.parser")

    News = soup.find_all('div', {"class": "articles"})
    for artcile in News:
        image_src = ""
        main = artcile.find_all('a')[0]
        link = main['href']
        #     print(link)
        images = main.find_all('img', {'src': re.compile('.jpg')})
        for image in images:
            #         print(image['src']+'\n')
            image_src = image['src']
            print(image_src)
        title = artcile.find('h2').text
        print(title)
        content = artcile.find('p').text

        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.language = 1
        new_headline.category = 3
        new_headline.image = image_src
        new_headline.content = content
        # new_headline.check = 'eng' + str(date.today())
        new_headline.save()

    return news_list(request)


def login(request):

   username = "wellcomes"
   password = "password"
   username = request.POST.get(
       'username'
       , '')
   password = request.POST.get(
       'password'
       , '')
   request.session['username'] = username
   request.session['password'] = password
   user = Users.objects.all()

   for c in user:
       if c.name == username and c.password == password:
           username = request.session['username']
           user_language = c.language
           headlines = Headline.objects.all()[::-1]
           userlists = Users.objects.all()[::-1]
           date_today = date.today()
           context = {
               'object_list': headlines,
               'user_language': user_language,
               'date_today': date_today,
           }

           return render(request, "news/user_view.html",context)

   else:

       return render(request, "news/index.html")


def malayalam_login(request):

   headlines = Headline.objects.all()[::-1]
   date_today = date.today()
   context = {
        'object_list': headlines,
       'date_today': date_today,
    }


   return render(request, "news/home_malayalam.html", context)
def malayalam_india_login(request):

   headlines = Headline.objects.all()[::-1]
   date_today = date.today()
   context = {
        'object_list': headlines,
       'date_today': date_today,
    }


   return render(request, "news/home_malayalam_india.html", context)

def malayalam_movie_login(request):

   headlines = Headline.objects.all()[::-1]
   date_today = date.today()
   context = {
        'object_list': headlines,
       'date_today': date_today,
    }



   return render(request, "news/home_malayalam_movie.html", context)

def malayalam_tech_login(request):

   headlines = Headline.objects.all()[::-1]
   date_today = date.today()
   context = {
        'object_list': headlines,
       'date_today': date_today,
    }



   return render(request, "news/home_malayalam_tech.html", context)


def malayalam_sports_login(request):
    headlines = Headline.objects.all()[::-1]
    date_today = date.today()
    context = {
        'object_list': headlines,
        'date_today': date_today,
    }

    return render(request, "news/home_malayalam_sports.html", context)
def english_login(request):




   headlines = Headline.objects.all()[::-1]
   date_today = date.today()
   context = {
        'object_list': headlines,
        'date_today': date_today,
    }


   return render(request, "news/home_english.html", context)
def english_tech_login(request):

   headlines = Headline.objects.all()[::-1]
   date_today = date.today()
   context = {
        'object_list': headlines,
        'date_today': date_today,
    }


   return render(request, "news/home_english_tech.html", context)
def english_sports_login(request):

   headlines = Headline.objects.all()[::-1]
   date_today = date.today()
   context = {
        'object_list': headlines,
        'date_today': date_today,
    }


   return render(request, "news/home_english_sports.html", context)


def english_movie_login(request):
    headlines = Headline.objects.all()[::-1]
    date_today = date.today()
    context = {
        'object_list': headlines,
        'date_today': date_today,
    }

    return render(request, "news/home_english_movie.html", context)
def news_list(request):

    headlines = Headline.objects.all()[::-1]
    date_today = date.today()
    context = {
        'object_list': headlines,
        'date_today': date_today,

    }

    return render(request, "news/home_english.html", context)
def account(request):
    return render(request,"news/index_register.html")
def search(request):
    headlines = Headline.objects.all()[::-1]
    date_today = date.today()
    context = {
        'object_list': headlines,
        'date_today': date_today,

    }
    return render(request,"news/search.html",context)
def search_news(request):
    headlines = Headline.objects.all()

    search_delete = Search.objects.all().delete()
    print('sdggdsgds')
    search_category = request.POST['search_category']
    search_lang = request.POST['search_lang']
    search_title = request.POST.get('search_title')
    search_date = request.POST['search_date']

    for headline in headlines:
        if headline.language==search_lang:
            # print('a')
            if headline.category==search_category:
                title = headline.title
                url = headline.url
                image = headline.image
                content = headline.content
                # print('a')
                # print(headline.date)
                # print(search_date)

                if str(headline.date) == search_date:
                    if search_title in headline.title:
                        title = headline.title
                        url = headline.url
                        image = headline.image
                        content = headline.content
                        category = headline.category
                        language = headline.language
                        # print(title)
                        # print(url)
                        # print(language)
                        # print(category)
                        # print(image)
                        # print(headline.content)
                        # print('a')
                        new_search = Search()

                        new_search.title = title
                        new_search.url = url
                        new_search.language = language
                        new_search.category = category
                        new_search.image = image
                        new_search.content = content
                        # new_headline.check = 'eng' + str(date.today())
                        new_search.save()
    headlines = Headline.objects.all()[::-1]
    date_today = date.today()
    context = {
        'object_list': headlines,
        'date_today': date_today,

    }



    return search_view(request)
def search_view(request):

    headlines = Headline.objects.all()[::-1]
    object_search = Search.objects.all()
    for a in object_search:
        print(a.title)
    date_today = date.today()
    context = {
        'object_list': headlines,
        'object_search': object_search,

    }
    return render(request, "news/search_news.html", context)

def register(request):
    name = "wellcomes"
    commentid = "password"
    comment = "coHHJ"
    name = request.POST.get(
        'name'
        , '')
    email = request.POST.get(
        'email'
        , '')
    password = request.POST.get(
        'password'
        , '')

    language = request.POST['language']

    request.session['name'] = name
    request.session['email'] = email
    request.session['password'] = password
    request.session['language'] = language

    user = Users.objects.all()
    for c in user:
        if c.name == name or c.email == email:
            return render(request,"news/index_register.html")


    else:

        dr = Users(
            name=name,
            email=email,
            password=password,
            language=language,

        )
        dr.save()
        return render(request,"news/index.html")
def logout(request):

    return render(request,"news/index.html")
def english_india(request):
    # headline_existing = Headline.objects.all()
    # for c in headline_existing:
    #     if c.date or c.date_india:
    #         pass

    headlines = Headline.objects.all()[::-1]
    date_today = date.today()
    context = {
        'object_list': headlines,
        'date_today': date_today,

    }
    return render(request,"news/english_india.html",context)