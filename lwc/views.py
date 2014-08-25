from django.shortcuts import render


def testhome(request):
	context = {}
	template = "donotuse.html"
	return render(request, template, context)


# def home2(request):
# 	context = {}
# 	template = "home2.html"
# 	return render(request, template, context)