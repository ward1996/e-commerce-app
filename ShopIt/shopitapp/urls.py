from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import ItemList, ItemCreate, ItemDelete, ItemDetail, UserLogin, Register, UserList, OrderCreate
from django.conf import settings
from django.conf.urls.static import static
'''
urlpatterns = [
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

'''

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login' ),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', ItemList.as_view(), name='home'),
    path('add-item/', ItemCreate.as_view(), name='create_item'),
    path('delete-item/<int:pk>/', ItemDelete.as_view(),name='delete_item' ),
    path('item-detail/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('item-detail/<int:pk>/', OrderCreate.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
