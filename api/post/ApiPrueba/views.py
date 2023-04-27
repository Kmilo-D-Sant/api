from post.models import Post
from post.ApiPrueba.serializers import PostSerializer
from django.http.response import JsonResponse
from django.views import View

class PostApiViewSet(View):
    def get(self, request):
        return JsonResponse({'mensaje': "funciona"})