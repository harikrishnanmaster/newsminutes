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
from news.models import Headline, Malayalam_Headline
from news.models import Users
requests.packages.urllib3.disable_warnings()
import time
def scrape(request):



  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://indianexpress.com/"
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  News = soup.find_all('div', {"class": "other-article"})
  # date_english = date.today()
  for artcile in News:
      main = artcile.find_all('a')[0]
      link = main['href']
      print(link)
      # image_src = str(main.find('img')['src'])
      # print(image_src)
      title = artcile.find('h3').text
      print(title)
      date_english = date.today()
      # print(date_english)
      headline_existing = Headline.objects.all()

      # print(headline_existing)
      for c in headline_existing:
          a=c.date
          print (a)
          print('new')
          print(date_english)
          if a!=date_english:

            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.image = image_src
      # new_headline.date = date_english
            new_headline.save()

      # return True
      return redirect("english_login")
def scrape_malayalam(request):
  Malayalam_Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.manoramaonline.com/news.html"
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"image-block"})
  for artcile in News:
    try:
    	main = artcile.find('a')
    except:
        pass
    try:
        link = main['href']

    except:
        pass

    try:
        image_src =  str(main.find('img')['src'])

    except:
        pass

    try:
        title = main['title']

    except:
        pass

    new_headline = Malayalam_Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.image = image_src
    new_headline.save()

  return redirect("malayalam_login")
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

           return render(request, "news/home.html")

   else:
       return render(request, "news/login.html")


def malayalam_login(request):

   headlines = Headline.objects.all()[::-1]
   context = {
        'object_list': headlines,
    }


   return render(request, "news/home_malayalam.html", context)
def english_login(request):




   headlines = Headline.objects.all()[::-1]
   context = {
        'object_list': headlines,
    }


   return render(request, "news/home_english.html", context)
def news_list(request):
    headline_existing = Headline.objects.all()
    if headline_existing:
        print('db not empty')

    else:
        print('empty')
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://indianexpress.com/"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News = soup.find_all('div', {"class": "other-article"})

        for artcile in News:
            main = artcile.find_all('a')[0]
            link = main['href']
            print(link)
            image_src = str(main.find('img')['src'])
            print(image_src)
            title = artcile.find('h3').text
            print(title)
            date_english = date.today()
            # print(date_english)
            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.language = 1
            new_headline.category = 1
            new_headline.image = image_src
            # new_headline.date = date_english
            new_headline.save()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url_india = "https://indianexpress.com/section/india/"
        content = session.get(url_india, verify=False).content
        soup = BSoup(content, "html.parser")

        News = soup.find_all('div', {"class": "articles"})
        for artcile in News:
            main = artcile.find_all('a')[0]
            link = main['href']
            #     print(link)
            images = main.find_all('img', {'src': re.compile('.jpg')})
            for image in images:
                #         print(image['src']+'\n')
                image_src = image['src']
                print(image_src)
            title = artcile.find('p').text
            print(title)
            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.language = 1
            new_headline.category = 2
            new_headline.image = image_src
            new_headline.save()
        session = requests.Session()
        session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
        url = "https://www.manoramaonline.com/news.html"
        content = session.get(url, verify=False).content
        soup = BSoup(content, "html.parser")
        News_malayalam = soup.find_all('div', {"class": "image-block"})
        for artcile in News_malayalam:
            try:
                main = artcile.find('a')
            except:
                pass
            try:
                link = main['href']

            except:
                pass

            try:
                image_src = str(main.find('img')['src'])

            except:
                pass

            try:
                title = main['title']

            except:
                pass

            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.language = 2
            new_headline.category = 1
            new_headline.image = image_src
            new_headline.save()
    # date_english = date.today()
    # b=headline_existing.date
    # print(b)
    for c in headline_existing:
        date_english = date.today()
        a = c.date
        print(a)
        print('----')
        print(date_english)
        if a != date_english:

            session = requests.Session()
            session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
            url = "https://indianexpress.com/"
            content = session.get(url, verify=False).content
            soup = BSoup(content, "html.parser")
            News = soup.find_all('div', {"class": "other-article"})

            for artcile in News:
                main = artcile.find_all('a')[0]
                link = main['href']
                print(link)
                image_src = str(main.find('img')['src'])
                print(image_src)
                title = artcile.find('h3').text
                print(title)
                date_english = date.today()
                # print(date_english)
                new_headline = Headline()
                new_headline.title = title
                new_headline.url = link
                new_headline.image = image_src
                new_headline.language = 1
                new_headline.category = 1
                # new_headline.date = date_english
                new_headline.save()
            session = requests.Session()
            session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
            url_india = "https://indianexpress.com/section/india/"
            content = session.get(url_india, verify=False).content
            soup = BSoup(content, "html.parser")

            News = soup.find_all('div', {"class": "articles"})
            for artcile in News:
                main = artcile.find_all('a')[0]
                link = main['href']
                #     print(link)
                images = main.find_all('img', {'src': re.compile('.jpg')})
                for image in images:
                    #         print(image['src']+'\n')
                    image_src = image['src']
                    print(image_src)
                title = artcile.find('p').text
                print(title)
                new_headline = Headline()
                new_headline.title = title
                new_headline.url = link
                new_headline.language = 1
                new_headline.category = 2
                new_headline.image = image_src
                new_headline.save()
            session = requests.Session()
            session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
            url = "https://www.manoramaonline.com/news.html"
            content = session.get(url, verify=False).content
            soup = BSoup(content, "html.parser")
            News = soup.find_all('div', {"class": "image-block"})
            for artcile in News:
                try:
                    main = artcile.find('a')
                except:
                    pass
                try:
                    link = main['href']

                except:
                    pass

                try:
                    image_src = str(main.find('img')['src'])

                except:
                    pass

                try:
                    title = main['title']

                except:
                    pass

                new_headline = Headline()
                new_headline.title = title
                new_headline.url = link
                new_headline.language = 2
                new_headline.category = 1
                new_headline.image = image_src
                new_headline.save()
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }

    return render(request, "news/home_english.html", context)
def account(request):
    return render(request,"news/register.html")
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

    request.session['name'] = name
    request.session['email'] = email
    request.session['password'] = password

    user = Users.objects.all()
    for c in user:
        if c.name == name or c.email == email:
            return render(request,"news/register.html")


    else:

        dr = Users(
            name=name,
            email=email,
            password=password,

        )
        dr.save()
        return render(request,"news/login.html")
def logout(request):

    return render(request,"news/login.html")
def english_india(request):
    # headline_existing = Headline.objects.all()
    # for c in headline_existing:
    #     if c.date or c.date_india:
    #         pass

    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request,"news/english_india.html",context)