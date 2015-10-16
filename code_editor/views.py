from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import View
from code_editor.models import CodeSubmission
from django.http import HttpResponseRedirect 
# Create your views here.

class IndexView(TemplateView):
	template_name = "index.html"

class CodeView(View):
	def get(self, request):
		code_obj = CodeSubmission.objects.create()
		code_obj.save()
		return HttpResponseRedirect('/code/%s' %(code_obj.id))

class CodeEditor(View):
	def get(self, request, code_id=None):
		template_name = 'code_editor.html'
		code_obj = get_object_or_404(CodeSubmission, pk=code_id)
		return render(request, template_name,)

	def post(self, request, code_id = None):
		return HttpResponse()
