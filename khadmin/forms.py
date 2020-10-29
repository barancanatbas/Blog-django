from django import forms
from post.models import Post,Kategori,SiteSetting

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'kategori',
        ]
class kategoriForm(forms.ModelForm):
    class Meta():
        model = Kategori
        fields = [
            'kategoriad',
        ]

class settingForm(forms.ModelForm):
    class Meta():
        model = SiteSetting
        fields = [
            'SiteTitle',
            'SiteMainTitle',
            'SiteImage',
            'SiteDescription',
            'email_host',
            'email_port',
            'email_host_user',
        ]