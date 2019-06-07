# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import reg
from django.contrib import admin

# Register your models here.

class register(admin.ModelAdmin):
    list_display = ['id', 'lastname', 'username' ,'email', 'timestamp', 'updated', 'is_active']
    list_editable = ['lastname', 'is_active']
    search_fields = ['username', 'email']
    date_hierarchy = 'timestamp'
    readonly_fields = ['timestamp', 'updated']
    prepopulated_fields = {"slug": ("username",)}

    class meta:
        model = reg

admin.site.register(reg, register)

