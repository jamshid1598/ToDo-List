from django.contrib import admin

from .models import ToDo_List

# Register your models here.
class TODO_List(admin.ModelAdmin):
    list_display=(
        'item',
        'complated',
    )
    list_display_links=(
        'item',
        'complated',
    )
    ordering=(
        'item',
        'complated',
    )
    fields_serach=(
        'item',
        'complated',
    )
    fieldsets = (
        ('To-Do List', {
            "fields": (
                'item',
                'complated',
            ),
        }),
    )

admin.site.register(ToDo_List, TODO_List)
    