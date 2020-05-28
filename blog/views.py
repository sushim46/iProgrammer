from django.shortcuts import render, HttpResponse
from blog.models import Post
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.filter(published=True).order_by('-timestamp')
    # print(allPosts)
    # allPosts2 = allPosts[::-1]  
    # print(allPosts2)
    context = {'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug)[0]
    print(post)
    context = {'post':post}
    return render(request,'blog/blogPost.html',context)