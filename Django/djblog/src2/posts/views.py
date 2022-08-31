# from socket import IOCTL_VM_SOCKETS_GET_LOCAL_CID
from django.shortcuts import render
from .models import Post
from .forms import Postform    
# Create your views here.
def post_list(request):
    objects=Post.objects.all()
    return render(request,'posts.html',{'posts':objects})

def post_detail(request,id):
    single=Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':single})

def new_post(request):
    if request.method=='POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        print('in else')
        form=Postform()
    return render(request,'new.html',{'form':form})

def edit_post(request,id):
    single=Post.objects.get(id=id)
    if request.method=='POST':
        form=Postform(request.POST,request.FILES,instance=single)
        if form.is_valid():
            form.save()
    else:
        print('in else')
        form=Postform(instance=single)
    return render(request,'new.html',{'form':form})
