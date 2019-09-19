import re
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav, UserLeavingMessage, UserAddress
from goods.serializers import GoodsSerializer
from MxShop.settings import REGEX_MOBILE

class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ['id', 'goods']

class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]
        fields = ['user', 'goods', 'id']

class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")
    class Meta:
        model = UserLeavingMessage
        fields = ['id', 'user', 'message_type', 'subject', 'message', 'file', 'add_time']

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M")
    signer_mobile = serializers.CharField(max_length=11)

    def validate_signer_mobile(self, signer_mobile):
        """
        验证手机号
        """
        # 验证手机号码是否非法
        if not re.match(REGEX_MOBILE, signer_mobile):
            raise serializers.ValidationError("手机号非法")
        return signer_mobile

    class Meta:
            model = UserAddress
            fields = ['id', 'user', 'province', 'city', 'district', 'address', 'signer_name', 'add_time', 'signer_mobile']
