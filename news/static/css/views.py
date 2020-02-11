from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
def scrape(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://indianexpress.com/"
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"other-article"})

  for artcile in News:
    main = artcile.find_all('a')[0]
    link = main['href']
    print(link)
    image_src = str(main.find('img')['src'])
    print(image_src)
    title = artcile.find('h3').text
    print(title)
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.image = image_src
    new_headline.save()
  return redirect("../")
def scrape_malayalam(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://indianexpress.com/"
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"other-article"})

  for artcile in News:
    main = artcile.find_all('a')[0]
    link = main['href']
    print(link)
    image_src = str(main.find('img')['src'])
    print(image_src)
    title = artcile.find('h3').text
    print(title)
    new_headline = Headline()
    new_headline.title = title
    new_headline.url = link
    new_headline.image = image_src
    new_headline.save()
  return redirect("../")
def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)