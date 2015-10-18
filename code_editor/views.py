from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from random import randint

from code_editor.models import CodeSubmission
from codetable.settings import HE_CLIENT_SECRET
from languages import LANGUAGES

import json
import urllib
import StringIO
import gzip

# Create your views here.
COMPILE_URL = 'https://api.hackerearth.com/v3/code/compile/'
RUN_URL = 'https://api.hackerearth.com/v3/code/run/'

class IndexView(TemplateView):
	"""
	Base View
	"""
	template_name = "index.html"

class CodeView(View):
	"""
	For creating the new workspace/codespace
	"""
	def get(self, request):
		code_obj = CodeSubmission.objects.create()
		code_obj.save()
		return HttpResponseRedirect('/code/%s' %(code_obj.id))

class CodeEditor(View):
	"""
	For compiling and running code using HACKEREARTH APIs
	"""
	def get(self, request, code_id=None):
		template_name = 'code_editor.html'
		code_obj = get_object_or_404(CodeSubmission, pk=code_id)
		return render(request, template_name, {'code_obj':code_obj, 'languages': LANGUAGES})
		
	def post(self, request, code_id = None):
		try:
			code_obj = get_object_or_404(CodeSubmission, pk=code_id)
			source = request.POST.get('code','')
			lang = request.POST.get('lang',None)
			post_data = {
				'client_secret': HE_CLIENT_SECRET,
				'async': 0,
				'source': source,
				'lang': lang,
				'time_limit': 5,
				'memory_limit': 262144,
				'id': randint(0,1000000),
				# 'callback': 'http://localhost:8000/receive-hackerearth-response/'
			}
			post_data = urllib.urlencode(post_data)
			response = urllib.urlopen(RUN_URL, post_data)
			# See if the response is gzipped or not 
			if response.info().get('Content-Encoding') == 'gzip':
				buf = StringIO.StringIO( response.read())
				gzip_f = gzip.GzipFile(fileobj=buf)
				content = gzip_f.read()
			else:
				content = response.read()
			# Update the code written by user in the database table
			CodeSubmission.objects.filter(id = code_id).update(code = source, language = lang)
			return HttpResponse(json.dumps(content), content_type="application/json")
		except Exception as e:
			return HttpResponse(json.dumps(e), content_type="application/json")
		# Return the response after making the API call 

class SaveCurrentCode(View):
	"""
	For saving the code written on the go
	"""
	def post(self, request, code_id = None):
		"""
		Method to save the code instantly as there is some change in the code.
		"""
		try:
			code_obj = get_object_or_404(CodeSubmission, pk=code_id)
			new_code = request.POST.get('code','')
			lang = request.POST.get('lang',None)
			CodeSubmission.objects.filter(id = code_id).update(code = new_code, language = lang)
			status =  {'status': True}
		except Exception as e:
			status =  {'status': False}
		return HttpResponse(json.dumps(status), content_type="application/json")

