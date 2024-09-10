from django.http import JsonResponse

# Create your views here.

def tarefa(request):
    if request.method == 'GET':
        tarefa = {'id': 1234, 'atividade': 'Estudar para o curso Backend'}
        return JsonResponse(tarefa)

