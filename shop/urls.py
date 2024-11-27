from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateShopView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('shop/<int:category>/', views.CategoryView.as_view(), name='shop_cat'),
    path('user-list/<int:user>/', views.UserView.as_view(), name='user_list'),
    path('shop-detail/<int:pk>/', views.DetailView.as_view(), name='shop_detail'),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('shop/<int:pk>/delete/', views.ShopDeleteView.as_view(), name='shop_delete'),
    path('shop/<int:pk>/buy/', views.PurchaseView.as_view(), name='shop_buy'),
    path('purchase-success/<int:pk>/', views.PurchaseSuccessView.as_view(), name='purchase_success'),
    path('shops/<int:category>',views.CategoryView.as_view(),name = 'shops_cat'),
    path('contact/', views.ContactView.as_view(), name='contact' ),
]