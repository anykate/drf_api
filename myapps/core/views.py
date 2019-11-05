from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})


# def api_index_view(request):
#     data = {
#         'first_name': 'Aniket',
#         'last_name': 'Aryamane',
#         'age': 41
#     }
#     return JsonResponse(data)

class APIIndexView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'first_name': 'Aniket',
            'last_name': 'Aryamane',
            'age': 41
        }
        return Response(data)
