from rest_framework.decorators import api_view



def getRoutes(request):
    routes = [
        {
            'Endpoint': '/users/',
            'method': 'GET',
            'body': None,
            'description': 'Returns list of users'
        }
    ]
    return JsonResponse(routes, safe=False)
