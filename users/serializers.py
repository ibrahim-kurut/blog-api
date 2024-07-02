from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Create Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    # 1- To validate the email and make it required
    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all(), message="This email is already in use.")])
    
    # 2- The password is not displayed in the response
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)
    
    # Make first and last name required
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 're_password')
        read_only_fields = ('id',)

    # 3- Verify that passwords match
    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"message": "Password fields didn't match."})
        return attrs

    # 4-  Create user
    def create(self, validated_data):
        # Remove re_password field before saving from dict validated_data
        validated_data.pop('re_password')

        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        # hash password
        user.set_password(password)
        user.save()

        return user


# get all user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

