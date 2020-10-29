from django.shortcuts import render,redirect
from .models import Post,SiteSetting,Comment,Kategori,bilgilendirme
from .forms import reportsForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    posts = Post.objects.all()
    kategoriler = Kategori.objects.all()
    bilgiler = bilgilendirme.objects.get(pk=1)
    gelenkategori= request.GET.get('k')
    if gelenkategori:
        posts = Post.objects.filter(kategori__kategoriad__contains =gelenkategori)

    paginator = Paginator(posts, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj':page_obj,
        'kategoriler':kategoriler,
        'bilgiler':bilgiler
    }
    return render(request,'post/index.html',context)

def anasayfa(request):
    bilgiler = bilgilendirme.objects.get(pk=1)
    context = {
        'bilgiler':bilgiler
    }
    return render(request,'post/anasayfa.html',context)

def detail(request,id):
    post = Post.objects.get(pk=id)
    context={
        'post':post
    }
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['comment']
        yorum = Comment(post=post,name=name,comment=comment)
        yorum.save()

    return render(request,'post/detail.html',context)

def report(request):
    form = reportsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('anasayfa')
    context ={
        'form':form
    }
    return render(request,'post/form.html',context)

def sendemail(self):
    email = EmailMessage(
                'Subject here',
                'Here is the message.',
                settings.EMAIL_HOST_USER,
                ['barancanatbas102@gmail.com'],
            )
    email.fail_silently=False
    email.send()