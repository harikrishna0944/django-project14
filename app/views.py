from django.shortcuts import render

# Create your views here.
def staticimage(request):
    return render(request,"staticimage.html")