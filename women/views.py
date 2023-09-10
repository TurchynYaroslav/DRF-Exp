
from django.forms import model_to_dict
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerPost
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class WomenAPIListPagination(PageNumberPagination):
    page_size = len(Women.objects.all())
    page_size_query_param = 'page_size'
    max_page_size = 100


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenAPIListPagination
    renderer_classes = [JSONRenderer]

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['indent'] = 2
        return context


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )
