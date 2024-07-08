
from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import viewsets, status, permissions
from .models import Task, TaskList, Comment
from .serializers import TaskSerializer, TaskListSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAdminUser, IsStandardUser, IsAssignedUserOrAdmin
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAssignedUserOrAdmin | IsAdminUser]

    def perform_create(self, serializer):
        # Automatically assign the task to the user creating it
        serializer.save(assigned_to=self.request.user)


class TaskView(APIView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)

    def post(self, request):
        user_object = User.objects.all()

        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated, IsAssignedUserOrAdmin | IsAdminUser]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAssignedUserOrAdmin | IsAdminUser]
