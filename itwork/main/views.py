# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from main.models import *
from .forms import FeedbackForm, SubscribeForm


def main(request):
    if request.method == "POST":
        print(request.path)
        if request.path == '/feedback':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                print('form save')
                form.save()
        elif request.path == '/subscribe':
            form = SubscribeForm(request.POST)
            print('get form')
            if form.is_valid():
                post = form.save(commit=False)
                print('get post')
                post.message = 'From subscribe form'
                post.save()
                print('post save')
        return redirect('/')

    else:
        slides = InfoSlide.objects.all().filter(is_active='True')
        lists = InfoList.objects.all()
        form = FeedbackForm()
        slide_form = FeedbackForms.objects.all().filter(active='True')[0]
        slide_left = 'side-left went-left'
        slide_right = 'side-right went-right'
        social_links = Social_links.objects.all()
        return render(request, 'index.html', locals())
