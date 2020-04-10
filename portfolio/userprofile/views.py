from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Language, Course, Certificate, ToolsAndTech

# class HomeView(TemplateView):
#     template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         return context

def index(request):
    languages = Language.objects.all() 
    courses = Course.objects.all()
    certificates = Certificate.objects.all()
    tools_and_tech = ToolsAndTech.objects.all()

    context = {
        'languages': languages,
        'courses': courses,
        'certificates': certificates,
        'tools_and_tech': tools_and_tech
    }
    return render(request, 'index.html', context)


