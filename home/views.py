from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.
def home(request):
    new = Post.objects.all()
    recent = Post.objects.filter(published=True).order_by('-timestamp')[0:6]   
    longer = Post.objects.filter(longer_feature=True)
    mypost = {'featured':recent, 'featured_two':longer}
    return render(request, 'home/home.html',mypost)

def contact(request):
    messages.success(request,'Fill This Form To Contact Me. ')
    if request.method=='POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        # print(name,email,phone,content)
        if len(name)<3 or len(email)<4 or len(phone)<10 or len(content)<10:
            messages.error(request, 'Please Fill The Form Correctly !!')
        else:
            contact = Contact(name=name,phone=phone,email=email,content=content)
            contact.save()
            messages.success(request,f'{name} Thank You For Contacting Us. Your Message Has Been Sent Succesfully. ')
       
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    allPosts
    params = {'allPosts':allPosts}
    return render(request,'home/search.html')