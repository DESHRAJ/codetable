from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from code_editor.models import CodeSubmission
# Create your views here.

class IndexView(TemplateView):
	template_name = "index.html"

class CodeView(View):
	def get(self, request):
		obj = CodeSubmission.objects.create()
		obj.save()
		return HttpResponseRedirect('/code/%s' %())