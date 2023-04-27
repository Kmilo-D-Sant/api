from post.ApiPrueba.views import PostApiViewSet
from django.urls import path
    
urlpatterns = [
    path('', PostApiViewSet.as_view(), name='prueba')
]