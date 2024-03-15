from rest_framework import serializers

from users.models import Transaction, User, Subscribe
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ('user',)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        return token


class UserSerializer(serializers.ModelSerializer):
    # <Your other UserSerializer stuff here>

    def create(self, validated_data):
        """
        Необходимо сделать чтобы создавался экземпляр Subscribe и отключить это поле в заполнении
        :param validated_data:
        :return:
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    model = Subscribe

    class Meta:
        model = Subscribe
        fields = '__all__'
