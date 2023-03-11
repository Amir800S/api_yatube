from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOfObject
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет Поста."""
    permission_classes = (IsAuthenticated, IsOwnerOfObject)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет Группы."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет Комментов."""
    permission_classes = (IsAuthenticated, IsOwnerOfObject)
    serializer_class = CommentSerializer

    def get_post(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id', ))
        return post

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
