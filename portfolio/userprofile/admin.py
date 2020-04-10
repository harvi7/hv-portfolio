from django.contrib import admin

from .models import Language, Course, Certificate, ToolsAndTech

admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Certificate)
admin.site.register(ToolsAndTech)
