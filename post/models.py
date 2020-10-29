from django.db import models
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250,verbose_name="başlık")
    content = RichTextUploadingField(verbose_name="içerik",null=True,blank=True)
    publising_date = models.DateTimeField(auto_now_add=True,verbose_name="yayınlanma tarihi")
    user = models.ForeignKey('auth.User',verbose_name='yazar',related_name='posts',on_delete=models.CASCADE)
    kategori = models.ForeignKey('post.Kategori',verbose_name='kategori',related_name='kategoris',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return "{}/update".format(self.id)
    def get_delete_url(self):
        return "{}/delete".format(self.id)
    def get_detail_url(self):
        return "{}/detail".format(self.id)

class Kategori(models.Model):
    kategoriad = models.CharField(max_length=250,verbose_name='kategoriad')

    def __str__(self):
        return self.kategoriad
    def get_delete_url(self):
        return "{}/Kategori-delete".format(self.id)
    def get_update_url(self):
        return "{}/Kategori-update".format(self.id)

class SiteSetting(models.Model):
    SiteTitle = models.CharField(max_length=200,verbose_name='Site Başlığı')
    SiteMainTitle = models.CharField(max_length=300,verbose_name='site ana başlık',null=True)
    SiteImage = models.ImageField(null=True,blank=True,verbose_name='Site Fotoğrafı')
    SiteDescription = models.TextField(verbose_name='Site Açıklama')
    SiteChangeDate = models.DateTimeField(verbose_name='değiştirme zamanı ',auto_now_add=True)
    email_host = models.CharField(max_length=100,null=True,blank=True)
    email_port = models.IntegerField(null=True,blank=True)
    email_host_user = models.CharField(max_length=100,null=True,blank=True)
    email_host_password = models.CharField(max_length=200,null=True,blank=True)

class Comment(models.Model):
    post = models.ForeignKey('post.Post',verbose_name='post',related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="İsim")
    comment = models.TextField(verbose_name="yorum")
    comment_date_time = models.DateTimeField(auto_now_add=True)

    def get_delete_url(self):
        return "{}/yorum-delete".format(self.id)

class bilgilendirme(models.Model):
    resim = models.ImageField(verbose_name='tanıtım resim',null=True,blank=True)
    yazi = RichTextUploadingField(verbose_name="yazi",null=True,blank=True)
    telefon = models.CharField(max_length=12,null=True)
    email= models.CharField(max_length=30,null=True)
    instagram = models.CharField(max_length=200,null=True)
    facebook = models.CharField(max_length=200,null=True)

class reports(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField()
    read = models.BooleanField(default=False,null=True)
    datetime = models.DateTimeField(auto_now_add=True,verbose_name='gönderme tarihi')

    def get_incele_url(self):
        return "{}/sikayet".format(self.id)
