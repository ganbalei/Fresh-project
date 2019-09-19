from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import UserFav, UserLeavingMessage, UserAddress
from .serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, AddressSerializer
from utils.permissions import IsOwnerOrReadOnly

class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取用户收藏列表
    create:
        收藏商品
    delete:
        取消收藏
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    lookup_field = 'goods_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializer
        return UserFavSerializer

class LeavingMessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言功能
    """
    serializer_class = LeavingMessageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)

class AddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
