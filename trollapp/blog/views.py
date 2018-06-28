
# Author : Aparna
# Project : troll app
# Date :27-06-2018


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from blog.models import *
import random
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse


# Create your views here.


@csrf_exempt
@require_POST
def uploaddata(request):
    gender = request.POST.get('gender')
    file = request.FILES.get("file")
    blog = blogFiles.objects.create(
        image_desc=gender,
        images=file
    )
    blog.save()
    return JsonResponse({"result": "file uploaded"})


@csrf_exempt
@api_view(["GET"])
def getimage(request):
    gender = request.GET.get('gender')
    name = request.GET.get('name')
    if not gender == 'other':
        image_lists = blogFiles.objects.filter(
            image_desc=gender
        ).values()
    else:
        image_lists = blogFiles.objects.filter.values()
    data = random.sample(list(image_lists), 1)
    file_id = data[0].get('id')
    print(file_id)
    result = dict(
        name=name,
        image='http://storiwall.com/troll/viewimage?file_id=' + str(file_id),
        marriage_at=random.randrange(25, 40),
        kids=random.randint(1, 7)
    )

    return Response({"result": result})


@csrf_exempt
@api_view(["GET"])
def viewimage(request):
    file_id = request.GET.get('file_id')
    random_data = blogFiles.objects.get(id=file_id)
    file = random_data.images.open()
    response = HttpResponse(file.read())

    return HttpResponse(response, content_type="image/png")
