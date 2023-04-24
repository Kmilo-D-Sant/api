from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.ApiPrueba.serializers import PostSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()