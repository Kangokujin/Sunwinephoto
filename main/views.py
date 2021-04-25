from django.shortcuts import render
from django.http import HttpResponse
from main import models

from django.views import View

import logging
logger = logging.getLogger(__name__)


def index(request):
    all_cats = models.Category.objects.all()
    return render(request, 'main/index.html', {
        'categories': all_cats
    })


def about(request):
    return render(request, 'main/about.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def blog(request):
    return render(request, 'main/blog.html')


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

        return render(request, 'main/single.html', data)
