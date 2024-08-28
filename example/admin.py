from django.contrib import admin
from .models import Quiz, Question, Alternative, Answer

class AlternativeInline(admin.TabularInline):
    model = Alternative
    extra = 4  # Número de alternativas que queremos por padrão

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AlternativeInline]

admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Alternative)
admin.site.register(Answer)
