from django.shortcuts import render
import os, sys
import json
from django.http import JsonResponse

sys.path.append(os.getcwd()+'/home/bin')
from dna_converters import *


from home.models import TeamMember

def index(request):
	return render(request, "home/index.html", {'user':request.user, 'error':'error'})

def text_encode(request):
	converters = Converters()
	m = [method for method in dir(converters) if callable(getattr(converters, method))]
	conv_methods = [x for x in m if x[0]!='_']
	
	data = {'conv_methods': conv_methods}
	return render(request, "home/text_encode.html", {'user':request.user, 'data':data})

def rencontres(request):
	return render(request, "home/rencontres.html", {'user':request.user, 'error':'error'})

def team(request):
	# print('hello')
	people = TeamMember.objects.all()
	# print(people, 'hello')
	return render(request, "home/team.html", {'user':request.user, 'people':people})

def partners(request):
	return render(request, "home/partners.html", {'user':request.user, 'error':'error'})


# converters = Converters()
# def index(request):
# 	# print(request.session.keys())
# 	m = [method for method in dir(converters) if callable(getattr(converters, method))]
# 	conv_methods = [x for x in m if x[0]!='_']
	
# 	data = {'conv_methods': conv_methods}

# 	return render(request, "geneit/index.html", {'data': data})

def post_text(request):
	converters = Converters()
	data = request.body.decode('utf-8')
	received_json_data = json.loads(data)
	method = received_json_data['params']['method']

	result = ''

	invert_op = getattr(converters, method, None)
	if callable(invert_op):
		result = invert_op(received_json_data)


	data = {'data': result}
	return JsonResponse(data)

