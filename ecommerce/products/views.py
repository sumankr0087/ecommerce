from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
 
class ProductView(APIView):

    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name=category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response({'data':serializer.data, 'count':len(serializer.data)})
    
    