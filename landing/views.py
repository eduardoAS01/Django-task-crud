from django.shortcuts import render,HttpResponse

# Create your views here.
def landing_page(request):
    return render(request,'landing/landing.html')