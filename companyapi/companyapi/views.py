from django.http import HttpResponse, JsonResponse




def home_page(request):
    print("Home page requested")
    friends=[ 
        'Rupesh',
        'Gargi', 
        'Vanishri'
    ]
    # return HttpResponse("<h1>This is home page</h1>")
    return JsonResponse(friends, safe= False)