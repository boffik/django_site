# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class InfoSlideAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InfoSlide._meta.fields]

    class Meta:
        model = InfoSlide

admin.site.register(InfoSlide, InfoSlideAdmin)

admin.site.register(InfoList)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feedback._meta.fields]

    class Meta:
        model = Feedback

admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(FeedbackForms)
# Register your models here.
