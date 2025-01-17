from django.shortcuts import render
from django.contrib import messages
from .models import Messages

def home(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        content = request.POST.get('content')

        try:
            message = Messages(
                first_name=first_name,
                last_name=last_name,
                content=content
            )
            message.save()
            messages.success(request, 'Your message has been successfully saved!')
        except Exception as e:
           
            messages.error(request, 'Error saving message: {}'.format(e))

    return render(request, 'portfolio/index.html')

def blog_detail1(request):
    return render(request,'portfolio/blog_detail1.html')

def blog_detail2(request):
    return render(request,'portfolio/blog_detail2.html')

def blog_detail3(request):
    return render(request,'portfolio/blog_detail3.html')
