#from django.contrib.auth.models import maniapp
from django.http import request
from django.shortcuts import render
from .models import Posts
from .serializers import PostSerializer
#from rest_framework.views import APIView
#from rest_framework import status
from rest_framework import generics
from django.contrib import messages
from rest_framework.response import Response
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from rest_framework import authentication, permissions
#from django.contrib.auth.models import User
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets
#from rest_framework import permissions
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
        return render(request,'index.html')
        
"""class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    PostSerializer"""

"""class PostsView(generics.RetrieveAPIView):
        serializer_class = PostSerializer
        queryset = Posts.objects.all()
       

       def get_queryset(self):
            return self.request.Posts.objects.all()

        def get(self,request,*args,**kwargs):
                queryset = self.get.queryset()
                serializer = PostSerializer(queryset,many = True)
                return Response(serializer.data)"""

class PostsView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

        

    """def post(request):
        if request.method=="POST":
            fname=request.POST.get('fname')
            lname=request.POST.get('lname')
            email=request.POST.get('email')
            password=request.POST.get('password')
            repassword=request.POST.get('repassword')
            if Posts.objects.filter(email=email).exists():
                messages.warning(request,"email is already exists")
            else:
                if password!=repassword:
                    messages.info(request,'passwords are not same')
                    return redirect('post')
                elif fname=="" or password=="":
                    messages.info(request,'fields are empty')
                    return redirect('post')
                else:
                    Posts.save()"""
                    #return redirect('welcome')

"""class ListUsers(APIView):
    
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        
        Return a list of all users.
        
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })"""

"""class PostsView(APIView):
    def get(self,request,pk=None, format=None):
        id = pk
        if id is not None:
            posts = Posts.objects.get(id=id)
            serializer = PostSerializer(posts)
            return Response(serializer.data)

        posts = Posts.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)            

    def post(self,request,format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id = pk
        posts = Posts.objects.get(pk=id)
        serializer = PostSerializer(posts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        id = pk
        posts = Posts.objects.get(pk=id)
        serializer = PostSerializer(posts,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        id = pk
        posts = Posts.objects.get(pk=id)
        posts.delete()
        return Response({'msg':'Data Deleted'})"""