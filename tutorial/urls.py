from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

#Wire up our API using automatic URL routing.
# Additionally, wwe include login urls for the browsable API.

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
"""
Because we're using viewsets instead of views, we can automatically generate the URL conf for our
API, by simply registering the viewsets with a router.

Again, if we need more control over the API URLs we can simply drop down to using regular class-
based views, and writing the URL conf explicitly.

Finally, we're including default login and logout views for use with the browsable API. That's optional,
but useful if your API requires authentication and you want to use the browsable API.
"""
