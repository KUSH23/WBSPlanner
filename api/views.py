from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MGroup, MSGroup
from .serializers import MGroupSerializer, MSGroupSerializer
from rest_framework import generics

@csrf_exempt
def mgroup_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        mgroup = MGroup.objects.all()
        serializer = MGroupSerializer(mgroup, many=True)
        return JsonResponse(serializer.data, safe=False)


class MGroupList(generics.ListCreateAPIView):
    queryset = MGroup.objects.all()
    serializer_class = MGroupSerializer


class MGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MGroup.objects.all()
    serializer_class = MGroupSerializer


class MSGroupList(generics.ListCreateAPIView):
    queryset = MSGroup.objects.all()
    serializer_class = MSGroupSerializer