from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ShopPostForm
from .models import ShopPost
from django.views.generic import FormView
from .form import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
 
class IndexView(ListView):
    template_name ='index.html'
    queryset = ShopPost.objects.order_by('-posted_at')
    paginate_by = 9
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sold_out_items = self.request.session.get('sold_out_items', [])
        context['sold_out_items'] = sold_out_items
        return context
 
@method_decorator(login_required, name='dispatch')
class CreateShopView(CreateView):
    form_class = ShopPostForm
    template_name = "post_shop.html"
    success_url = reverse_lazy('shop:post_done')
 
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
 
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
 
class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sold_out_items = self.request.session.get('sold_out_items', [])
        context['sold_out_items'] = sold_out_items
        return context
 
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = ShopPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories
 
class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9
 
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = ShopPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list
 
class DetailView(DetailView):
    template_name = 'detail.html'
    model = ShopPost
 
 
class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9
 
    def get_queryset(self):
        queryset = ShopPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset
 
class ShopDeleteView(DeleteView):
    model = ShopPost
    template_name = 'shop_delete.html'
    success_url = reverse_lazy('shop:mypage')
 
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
 
 
@method_decorator(login_required, name='dispatch')
class PurchaseView(TemplateView):
    template_name = 'purchase.html'
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        record = get_object_or_404(ShopPost, pk=pk)
        context['record'] = record
        return context
 
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        record = get_object_or_404(ShopPost, pk=pk)
       
        sold_out_items = request.session.get('sold_out_items', [])
        if pk not in sold_out_items:
            sold_out_items.append(pk)
            request.session['sold_out_items'] = sold_out_items
 
        return redirect('shop:purchase_success', pk=record.pk)
 
class PurchaseSuccessView(TemplateView):
    template_name = 'purchase_success.html'
   
class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9
   
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = ShopPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories
 
class ContactView(FormView):
    template_name ='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('shop:contact')
     
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' .format(name, email, title, message)
        from_email = 'spr2440031@stu.o-hara.ac.jp'
        to_list = ['spr2440031@stu.o-hara.ac.jp']
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        message.send()
        messages.success(
          self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
 
 