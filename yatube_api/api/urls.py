from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')

router_for_comments = DefaultRouter()  # Роутер для комментов
router_for_comments.register('comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/', include(router_for_comments.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='api_token'),
]
