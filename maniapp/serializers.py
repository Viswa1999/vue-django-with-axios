from rest_framework import serializers

from .models import Posts

"""class maniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'description', 'status')"""
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ("fname","lname","email","password","repassword")

    def  validate(self,attrs):
    	email = attrs.get('email','')
    	if  Posts.objects.filter(email=email).exists():
    		raise serializers.ValidationError(
    			{'email':('Email is already in use')})
    	return super().validate(attrs)
