from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.login,name='login'),
    path('logout',views.logout_view,name='logout'),

    #kategoriler
    path('kategoriler',views.kategorilerList,name='kategorilerlist'),
    path('<int:id>/Kategori-delete',views.Kdelete,name='Kdelete'),
    path('<int:update_id>/Kategori-update',views.Kupdate,name='Kupdate'),
    path('Kcreate/',views.Kcreate,name='Kcreate'),

    #post
    path('list',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:id>/delete',views.delete,name='delete'),
    path('<int:update_id>/update',views.update,name='update'),

    #şikayet
    path('sikayet',views.sikayet,name='sikayet'),
    path('<int:id>/sikayet',views.sikayetdetay,name='sikayetdetay'),
    
    # yorumlar
    path('yorumlar',views.yorumlarlist,name='yorumlarlist'),
    path('<int:delete_id>/yorum-delete',views.yorumdelete,name='yorumdelete'),

    #site setting
    path('ayarlar',views.ayarlar,name='ayarlar'),
]