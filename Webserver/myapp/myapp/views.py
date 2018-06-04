from django.http import HttpResponse
from . import signTime
from django.views.decorators.csrf import csrf_exempt

def index (request):

    return HttpResponse("This is not a website")

def post (request):

    if request.method == 'POST':

        return HttpResponse("nice")

    else:

        return HttpResponse("wrong request jackass")

@csrf_exempt
def getSign(request):

    if request.method == 'POST':
        return HttpResponse(signTime.getSig(request.body))

    else:
        return HttpResponse("This is an api endpoint, use a post request in the right format")