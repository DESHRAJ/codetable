from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import View
from code_editor.models import CodeSubmission
from django.http import HttpResponseRedirect, HttpResponse
import json

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
		return render(request, template_name, {'code_obj':code_obj})
		
	def post(self, request, code_id = None):
		try:
			code_obj = get_object_or_404(CodeSubmission, pk=code_id)
			new_code = request.POST.get('code','')
			lang = request.POST.get('lang',None)
			CodeSubmission.objects.filter(id = code_id).update(code = new_code, language = lang)
			status =  {'status': True}
		except Exception as e:
			status =  {'status': False}
		return HttpResponse(json.dumps(status), content_type="application/json")

