from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response

# Create your views here.
class Login(View):
    def get(self, request):
        #Get form object
        return render(request, 'bookraves_user/login.html', {})
