from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .models import	Short_enURL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent

# Create your views here.




# def short_en_redirect_view(request,shortcode=None,*args,**kwargs):
	
# 	# try:
# 	# 	obj = Short_enURL.objects.get(shortcode=shortcode)
# 	# except:
# 	# 	obj = Short_enURL.objects.all().first()


# 	obj = get_object_or_404(Short_enURL,shortcode=shortcode)
# 	# obj_url=obj.url


# 	# obj_url=None
# 	# qs= Short_enURL.objects.filter(shortcode__iexact=shortcode.upper())
# 	# if qs.exists() and qs.count()==1:
# 	# 	obj=qs.first()
# 	# 	obj_url=obj.url 
# 	return HttpResponseRedirect(obj.url)

def home_view_fbv(request,*args,**kwargs):
	if request.method == "POST":
		print(request.POST)
	return render(request,"shortener/home.html",{})


class HomeView(View):
	def get(self,request,*args,**kwargs):
		the_form = SubmitUrlForm()
		bg_image = 'https://arc-anglerfish-arc2-prod-bonnier.s3.amazonaws.com/public/XQRMY2UEXZE4VACIXD7SUC2GBU.jpg'
		context ={
			"title": "Short.en",
			"form" : the_form,
			"bg_image": bg_image
		}
		return render(request,"shortener/home.html",context)

	def post(self,request,*args,**kwargs):
		form = SubmitUrlForm(request.POST)
		bg_image = 'https://arc-anglerfish-arc2-prod-bonnier.s3.amazonaws.com/public/XQRMY2UEXZE4VACIXD7SUC2GBU.jpg'
		context ={
			"title": "Short.en",
			"form" : form,
			"bg_image": bg_image
		}
		template= "shortener/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = Short_enURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"created": created,
				"bg_image": bg_image
			}	
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"
		
		return render(request,template,context)



class URLRedirectView(View):
	def get(self,request,shortcode=None,*args,**kwargs):
		qs = Short_enURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count()!= 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)


		# obj = get_object_or_404(Short_enURL,shortcode=shortcode)
		# print(ClickEvent.objects.create_event(obj))
		# return HttpResponseRedirect(obj.url)

