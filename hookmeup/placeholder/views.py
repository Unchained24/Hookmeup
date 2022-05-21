from django.http import request
from django.shortcuts import redirect, render

# Create your views here.


def home(request):

    if ("agree" in request.POST):
        agree = request.POST.get('agree')
        print(agree)
        if agree == "on":
            return redirect("https://wa.link/abafxn")

    return render(request, 'placeholder/index.html')

def rules(request):

    return render(request, 'placeholder/rules.html')