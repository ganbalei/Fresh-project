"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
#from django.urls import path, include
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static
#from MxShop.settings import MEDIA_ROOT
#from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset, UserViewSet
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, basename='goods')
# 配置category的url
router.register(r'categorys', CategoryViewSet, basename='categorys')

router.register(r'codes', SmsCodeViewset, basename='codes')

router.register(r'users', UserViewSet, basename='users')

router.register(r'userfavs', UserFavViewset, basename='userfavs')

router.register(r'messages', LeavingMessageViewset, basename='messages')

router.register(r'address', AddressViewset, basename='address')

router.register(r'shopcarts', ShoppingCartViewset, basename='shopcarts')

router.register(r'orders', OrderViewset, basename='orders')

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),

   #url(r'^mddia/(?<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^', include(router.urls)),
    #drf自带的token认证模式
    #url(r'^api-token-auth/', views.obtain_auth_token),
    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),

    url(r'docs/', include_docs_urls(title='慕学生鲜')),
]
#上传的文件能够通过url打开
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)