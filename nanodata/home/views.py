from django.shortcuts import render

def index(request):

	return render(request, "home/index.html", {'user':request.user, 'error':'error'})

