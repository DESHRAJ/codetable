from django.db import models
import uuid
import string
import random
# Create your models here.

def id_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase  + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

class CodeSubmission(models.Model):
	'''
	To store the codesubmissions made by users
	'''
	DEFAULT_CODE = "print 'Hello World'"
	id = models.CharField(max_length = 6, primary_key=True, default=id_generator, editable=False)
	code = models.TextField(default = DEFAULT_CODE)
	language = models.CharField(max_length = 40, default = 'PYTHON')
	created_at = models.DateTimeField(auto_now_add = True)

