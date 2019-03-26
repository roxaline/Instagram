from django.http  import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('Welcome to insta-app')