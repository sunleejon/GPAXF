from django.urls import path, re_path

from App import views

urlpatterns = [
    path('home/', views.home, name='home'),
    #re_path('marketwithparams/(?P<typeid>\d+)/(?P<childcid>\d+)/', views.market_with_params, name='market_with_params'),
    re_path('marketwithparams/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)/', views.market_with_params, name='market_with_params'),
    path('market/', views.market, name="market"),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
    path('learn', views.learn),

    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('checkuser/', views.checkuser, name="checkuser"),
    path('logout/', views.logout, name='logout'),
    path('activate/', views.activate, name='activate'),

    path('addtocart/', views.add_to_cart, name="add_to_cart"),
    path('changecartstate/', views.change_cart_state, name="change_cart_state"),
    path('subshopping/', views.sub_shopping, name="subshopping"),
    path('allselect/', views.all_select, name="allselect"),
    path('makeorder/', views.make_order, name='makeorder'),
    path('orderdetail/', views.order_detail, name="prderdetail"),
    path('orderlistnotpay/', views.order_list_not_pay, name='orderlistnotpay'),
    path('payed/', views.payed, name='payed'),

    path('alipay', views.alipay, name='alipay'),
    path('checkpayed', views.check_payed, name='chenck_payed'),

]