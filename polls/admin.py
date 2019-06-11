from django.contrib import admin

# Register your models here.

from .models import ImgTxtPair , Choice


admin.site.register(ImgTxtPair)

admin.site.register(Choice)


