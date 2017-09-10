from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
	"""	
	def get(self,request,**kwargs):
			return render(request,'index.html',context=None)
	"""
	template_name = "index.html"

class AboutPageView(TemplateView):
	template_name = "about.html"
"""
This file defines a view called HomePageView. 
Django views take in a request and return a response. 
In our case, the method get expects a HTTP GET request to the url defined in our urls.py file. 
On a side note, we could rename our method to post to handle HTTP POST requests.
"""



"""

Notice that in the second view, I did not define a get method. 
This is just another way of using the TemplateView class. 
If you set the template_name attribute, a get request to that view will automatically use the defined template. 
Try changing the HomePageView to use the format used in AboutPageView."""