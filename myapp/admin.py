from django.contrib import admin
from .models import Chemistry

class ChemistryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('About a Course',      {'fields': ['course','course_number','titile','book_number']}),
        ('Experiment',      {'fields': ['experiment_number', 'experiment_name']}),
        ('Chemicals used',      {'fields': ['chemical_name', 'chemical_properties', 'ghs_sign']}),
        ('Desertion',      {'fields': ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w' ]}),
        ('Reactions',      {'fields': ['reactions']}),
    ]
    list_display = ('id','experiment_number', 'experiment_name')
    #list_display_links = ()
    #search_fields = ()

admin.site.register(Chemistry, ChemistryAdmin)