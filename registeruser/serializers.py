from rest_framework import serializers
from registeruser.models import AppUser


def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char))+s)
    print(result)    
    return result   


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['name','email','password']
        # extra_kwargs={'password': {'write_only': True}}

    def create(self,validated_data):
            user = AppUser.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            password = encrypt(validated_data['password'],4),

        )
            return user