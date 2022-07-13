from django.contrib import admin

from mainapp.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'university', 'is_active',)
    list_filter = ('university', 'is_active',)
    search_fields = ['lastname', ]
