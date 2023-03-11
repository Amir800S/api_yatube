from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = 'api'

router_v01 = DefaultRouter()
router_v01.register('posts', PostViewSet, basename='posts')
router_v01.register('groups', GroupViewSet, basename='groups')
router_v01.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router_v01.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='api_token'),
]
