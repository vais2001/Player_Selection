# admin.py
from django.contrib import admin
from .models import Skill, Player

class SkillAdmin(admin.ModelAdmin):
    list_display = ['skillname' ,'value']

admin.site.register(Skill, SkillAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']

admin.site.register(Player, PlayerAdmin)
