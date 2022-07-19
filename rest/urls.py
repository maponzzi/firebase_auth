from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest import views

from django.urls import include, path


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('auth-token/', obtain_auth_token),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
