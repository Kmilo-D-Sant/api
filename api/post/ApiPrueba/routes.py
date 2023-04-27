from post.ApiPrueba.views import PostApiViewSet
from django.urls import path
    
urlpatterns = [
    path('api/', PostApiViewSet.as_view(), name='prueba')
]