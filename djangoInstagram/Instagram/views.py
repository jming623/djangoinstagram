from django.shortcuts import render
from rest_framework.views import APIView

class Iu(APIView):
    def get(self, request):
        print('GET으로 호출')
        return render(request, "instagram/iu.html")

class Sub(APIView):
    def get(self, request):
        print('GET으로 호출')
        return render(request, "instagram/main.html")

    def post(self, request):
        print('POST로 호출')
        return render(request, "instagram/main.html")

