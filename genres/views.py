from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from genres.models import genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.

@csrf_exempt
def genre_list_view(request):
    if request.method == 'GET':
        genres_list = genre.objects.all()
        data = []
        for Genre in genres_list:
            data.append(
                {'id': Genre.id, 'name': Genre.name}
            )
        return JsonResponse(data, safe= False)
    
    elif request.method == 'POST':
        datas = json.loads(request.body.decode('utf-8'))
        new_genre = genre(name=datas['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201,
        )
    
@csrf_exempt 
def genre_detail_view(request, pk):
    genree = get_object_or_404(genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genree.id, 'name': genree.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        datas = json.loads(request.body.decode('utf-8'))
        genree.name=datas['name']
        genree.save()
        return JsonResponse({'id': genree.id, 'name': genree.name})
    
    elif request.method == 'DELETE':
        genree.delete()
        return JsonResponse({'message': 'Gênero excluído com sucesso'}, status=204)
