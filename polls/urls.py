from django.urls import path
from . import views

urlpatterns = [
    path('allpopup', views.all_popup_view, name='allpopup'),
    path('nhanqua', views.nhan_qua_view, name='nhanqua'),
    path('dangkithongtin',views.dang_ki_thong_tin,name = 'dangkithongtin'),
    path('trangchu',views.trang_chu,name = 'trangchu'),
    path('thele',views.the_le,name = 'thele'),
    path('kiemtra',views.kiem_tra,name = 'kiemtra'),
    path('home',views.home,name = 'home'),
    path('test',views.test,name = 'test')
]
