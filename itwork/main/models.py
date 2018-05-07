# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models


class InfoSlide(models.Model):
    name = models.CharField(max_length = 20, blank = False, default = 'Slide')
    title = models.CharField(max_length = 40, blank = False, null = False)
    menu_title = models.CharField(max_length = 40, blank = False, null = False, default='Menu entry')
    body = RichTextField()
    is_active = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Инфо-слайд'
        verbose_name_plural = 'Инфо-слайды'

    def __str__(self):
        return self.name


class InfoList(models.Model):
    slide = models.ForeignKey('InfoSlide', on_delete=models.CASCADE,)
    name = models.CharField(max_length = 20, blank = False, default = '')
    image = models.FileField(upload_to='static_dev/uploads/')
    text = models.TextField()

    class Meta:
        verbose_name = 'Список к слайду'
        verbose_name_plural = 'Списки к слайдам'

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length = 100, blank = False, null=False)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Сообщение пользователя'
        verbose_name_plural = 'Сообщения пользователей'

    def __str__(self):
        return 'Message_' + str(self.id)

class FeedbackForms(models.Model):
    slide = models.ForeignKey('InfoSlide', on_delete=models.CASCADE,)
    name = models.CharField(max_length = 30)
    active = models.BooleanField(default="False")

    class Meta:
        verbose_name = 'Форма на слайде'

    def __str__(self):
        return self.name
