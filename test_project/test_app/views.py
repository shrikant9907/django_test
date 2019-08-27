from django.shortcuts import render
from django.http import HttpResponse
from .models import SitePages

# Create your views here.
def PageView(request):
#	if request.method == "POST":
    form = SitePages(request)
    if form.is_valid():
        form.save()
        return render(request,"pages/page.html")
