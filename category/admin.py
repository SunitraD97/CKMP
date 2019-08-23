from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    '''fieldsets = [
        ('About a Course',      {'fields': ['course','course_number','titile','book_number']}),
        ('Experiment',      {'fields': ['experiment_number', 'experiment_name']}),
        ('Chemicals used',      {'fields': ['chemical_name', 'chemical_properties', 'ghs_sign']}),
        ('Desertion',      {'fields': ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w' ]}),
        ('Reactions',      {'fields': ['reactions']}),
    ]'''
    list_display = ('id','name', 'ppe_sign')
    #list_display_links = ()
    #search_fields = ()

admin.site.register(Category,CategoryAdmin)