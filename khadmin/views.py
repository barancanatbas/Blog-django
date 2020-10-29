from django.shortcuts import render,redirect,get_object_or_404
from post.models import Post,SiteSetting,Comment,Kategori,reports
from django.contrib import auth,messages
from .forms import PostForm,kategoriForm,settingForm
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url="login")
def index(request):
    posts = Post.objects.all()
    search = request.GET.get('q')
    if search:
        posts = Post.objects.filter(Q(title__icontains=search)).distinct()
    context ={
        'posts':posts
    }
    return render(request,'kh-admin/index.html',context)

@login_required(login_url="login")
def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.add_message(request, messages.SUCCESS, 'ekleme başarılı :)')
        return redirect('index')
    context = {
        'form':form
    }
    return render(request,'kh-admin/forms.html',context)

    # custom form example

    '''if request.user.is_authenticated and request.user.is_staff:

        kategoriler = Kategori.objects.all()
        context ={
            'kategoriler':kategoriler
        }
    
        if request.method == 'POST' and request.FILES['resim'] or None:
            resim = request.FILES['resim']
            _title= request.POST['title']
            _content = request.POST['content']
            kategori = int(request.POST['kategori'])
            _kategori = Kategori.objects.get(pk = kategori)
            _user = request.user
            _data = Post.objects.create(title=_title,content=_content,user=_user,kategori=_kategori,image=resim.name)
            fs = FileSystemStorage()
            fs.save(resim.name,resim)
            if _data is not None and fs is not None:
                return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Alanları doldurun !')

    else:
        messages.add_message(request, messages.ERROR, 'Bu alana girmek için yetkiniz olmayabilir.')
        return redirect('login')

    return render(request,'kh-admin/create.html',context) '''

@login_required(login_url="login")
def delete(request,id):
    deleteData = Post.objects.filter(pk=id).delete()
    messages.add_message(request, messages.SUCCESS, 'Seçilen post silindi')
    return redirect('index')

@login_required(login_url="login")        
def update(request,update_id):
    #if request.user.is_authenticated and request.user.is_staff:
    obje = get_object_or_404(Post,pk=update_id)
    form = PostForm(request.POST or None, instance=obje)
    if form.is_valid():
        form.save()
        return redirect('index')
    context={
        'form':form
    }
    return render(request,'kh-admin/forms.html',context)
    
def login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('index')
    else:
        if request.method == 'POST':
            kulName = request.POST['kulAdi']
            sifre = request.POST['sifre']
            user = auth.authenticate(username=kulName,password=sifre)
            if user is not None:
                if user.is_staff:
                    auth.login(request,user)
                    return redirect('index')
                else:
                    messages.add_message(request, messages.ERROR, 'admin paneline giriş izniniz yok ')
                    return redirect('login')
            else:
                #boyle bir kullanıcı yok 
                return redirect('login')
        return render(request,'kh-admin/login.html')

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('anasayfa')
  
@login_required(login_url="login")
def kategorilerList(request):
    kategoriler = Kategori.objects.all()
    search = request.GET.get('q')
    if search:
        kategoriler = Kategori.objects.filter(Q(kategoriad__icontains=search)).distinct()
    context={
        'kategoriler':kategoriler
    }
    return render(request,'kh-admin/kategorilerlist.html',context)

@login_required(login_url="login")
def Kdelete(request,id):
    deleteData = Kategori.objects.filter(pk=id).delete()
    if deleteData:
        messages.add_message(request,messages.SUCCESS,'Silme işlemi başarılı ')
        return redirect('kategorilerlist')
    else:
        messages.add_message(request,messages.ERROR,'bir hata oldu ')
        return redirect('kategorilerlist')
    

@login_required(login_url="login")
def Kupdate(request,update_id):
    obje = get_object_or_404(Kategori,pk=update_id)
    form = kategoriForm(request.POST or None ,instance=obje)
    if form.is_valid():
        form.save()
        return redirect('kategorilerlist')
    context = {
        'form':form,
    }
    return render(request,'kh-admin/forms.html',context)

    
@login_required(login_url="login")
def Kcreate(request):
    form = kategoriForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('kategorilerlist')
    context = {
        'form':form
    }
    return render(request,'kh-admin/forms.html',context)


@login_required(login_url="login")
def sikayet(request):
    sikayetler = reports.objects.all()
    context = {
        'sikayetler':sikayetler
    }
    return render(request,'kh-admin/sikayetlist.html',context)
    

@login_required(login_url="login")
def sikayetdetay(request,id):
    report = reports.objects.get(pk=id)
    if report.read == False:
        reports.objects.filter(pk=id).update(read=True)  
    context ={
        'report':report
    }
    #TODO: mail gönderme işlemini dosyaya yazdırma ve ordan okuma orarak çözdüm
    if request.method =='POST':
        title = request.POST['title']
        mesaj = request.POST['mesaj']
        sikayetmail = report.email
        email = EmailMessage(
                title,
                mesaj,
                settings.EMAIL_HOST_USER,
                [sikayetmail],
            )
        email.fail_silently=False
        email.send()
    return render(request,'kh-admin/sikayetincele.html',context)


@login_required(login_url="login")
def yorumlarlist(request):
    yorumlar = Comment.objects.all()
    context = {
        'yorumlar':yorumlar
    }
    return render(request,'kh-admin/yorumlarlist.html',context)
    

@login_required(login_url="login")
def yorumdelete(request,delete_id):
    deletedata = Comment.objects.filter(pk=delete_id).delete()
    if delete:
        messages.add_message(request,messages.SUCCESS,'öğe silindi.')
        return redirect('yorumlarlist')
    else:
        messages.add_message(request,messages.ERROR,'öğe silinmedi.')
        return redirect('yorumlarlist')
    

@login_required(login_url="login")
def ayarlar(request):
    obje = get_object_or_404(SiteSetting,pk=1)
    form = settingForm(request.POST or None,instance=obje)
    context = {
        'form':form
    }
    if form.is_valid():
        form.save()
        context = {
            'form':form
        }
        return render(request,'kh-admin/forms.html',context) 
    return render(request,'kh-admin/forms.html',context)