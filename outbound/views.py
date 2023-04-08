from django.shortcuts import render,redirect

# Create your views here.
def out_bound(request):
    print("hello out_bound")
    return redirect('/')
