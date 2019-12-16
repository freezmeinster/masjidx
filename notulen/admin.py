from django.contrib import admin
from .models import Notes, Assignment, NotesTask


class AssignmentInline(admin.TabularInline):
    model = Assignment

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline,]


@admin.register(NotesTask)
class NotesTaskAdmin(admin.ModelAdmin):
    pass



