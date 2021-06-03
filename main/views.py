from django.shortcuts import render
from django.http import HttpResponse
from main import models

from django.http import HttpResponseRedirect

from django.views import View

from main import forms

import requests

import logging
logger = logging.getLogger(__name__)


def index(request):
    all_cats = models.Category.objects.filter(active=True).order_by('order')
    return render(request, 'main/index.html', {
        'categories': all_cats
    })


def about(request):
    all_cats = models.Category.objects.filter(active=True).order_by('order')
    return render(request, 'main/about.html', {
        'categories': all_cats
    })


def gallery(request):
    all_cats = models.Category.objects.filter(active=True).order_by('order')
    images = models.Photo.objects.filter(active=True)

    return render(request, 'main/gallery.html', {
        'categories': all_cats,
        'images': images
    })


def services(request):
    all_cats = models.Category.objects.filter(active=True).order_by('order')
    return render(request, 'main/services.html', {
        'categories': all_cats
    })

class ContactView(View):

    def get(self, request):

        all_cats = models.Category.objects.filter(active=True).order_by('order')
        return render(request, 'main/contact.html', {
            'categories': all_cats
        })

    def post(self, request):
        
        form = forms.ContactForm(request.POST)
        # check whether it's valid:
        logger.error(form)
        if form.is_valid():

            message = request.POST.get('message')
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            phone = request.POST.get('phone')
            order = request.POST.get('order', 0)
            date = request.POST.get('date', 0)
            subject = request.POST.get('subject')

            order_text = 'да' if order else 'нет'
            date_text = date if order else 'нет'


            text = f"""Новое сообщение от: {name} {surname}\n\nТелефон: {phone}\nТема: {subject}\n\nТекст: {message}.\n\nЗаказ: {order_text}.\nКогда: {date}"""

            requests.get(f'https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendMessage')
            
            method = 'sendMessage'
            token = '1232693876:AAHBDydt1CoLCML5tOZ27vcQUl7HWHoOonI'
            response = requests.post(
                url=f'https://api.telegram.org/bot{token}/{method}',
                data={'chat_id': -1001187030961, 'text': text}
            )
            
            return HttpResponseRedirect('/')

        else:

            return HttpResponseRedirect('/contact')


class CategoryListView(View):

    def get(self, request, category):

        try:
            category = models.Category.objects.get(slug=category)
        except models.Category.DoesNotExist as e:
            logger.error(e)

            return render(request, 'main/404.html')

        images = models.Photo.objects.filter(category=category)
        logger.error(images.count())
        logger.error(images)

        data = {
            'images': images,
            'count': images.count(),
            'cat': category
        }

        return render(request, 'main/gallery.html', data)


class NewsView(View):

    def get(self, request):

        news = models.Announcement.objects.all()

        data = {
            'news': news
        }

        return render(request, 'main/news.html', data)

    
class SingleNewsView(View):

    def get(self, request, slug):
        
        try:
            news = models.Announcement.objects.get(slug=slug)
        except models.Announcement.DoesNotExist as e:
            logger.error(e)

            return render(request, 'main/404.html')

        data = {
            'post': news
        }

        return render(request, 'main/article.html', data)
