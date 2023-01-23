from django.shortcuts import render
from .models import item, order
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.urls import reverse_lazy
# Create your views here.
'''def home(request):
    items = item.objects.all().values()

    context = {'item' : items }
    return render(request, 'home.html',context )
'''
class UserLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')




class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(Register, self).form_valid(form)


class ItemList(LoginRequiredMixin, ListView):
    model = item
    fields = '__all__'
    context_object_name = 'items'
    template_name = 'index.html'
    

    def get_login_url(self) -> str:
        login_url = reverse_lazy('login')
        return str(login_url)

   

class ItemDetail(LoginRequiredMixin, DetailView):
    model = item
    template_name = 'item_detail.html'
    context_object_name = 'item_detail'


class ItemCreate(LoginRequiredMixin, CreateView):
    model = item
    context_object_name = 'create_item'
    template_name = 'create_item.html'
    fields = ['item_name','description', 'item_price', 'quantity','item_image']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = item
    context_object_name = 'delete'
    template_name = 'delete_item.html'
    success_url = reverse_lazy('home')

class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'myprofile.html'
    fields = '__all__'
    context_object_name = 'users'
    login_url = reverse_lazy('home')

class OrderCreate(LoginRequiredMixin, CreateView):
    model = order
    template_name = 'item_detail.html'
    fields = ['ordered']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.item = self.instance.item
        return super(OrderCreate, self).form_valid(form)
