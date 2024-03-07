from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations

# Create your views here.



def hello(request):
    return HttpResponse("Hello world")


def about(request):
    return HttpResponse("Thius is my nnew applciation")

def news(request):
    return HttpResponse("thi sis for news")

def places(request):

    dest1 = Destinations('Kerala', 1, 200)
    dest2 = Destinations('Goa', 2, 300)
    dest3 = Destinations('Manali', 3, 400)
    dest4 = Destinations('Mumbai', 4, 500)

    dests = [dest1, dest2, dest3, dest4]

    # return render(request, 'cities.html', {'dests': dests})
    return render(request, 'landing.html')

def submit_sales(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        
        # Here you can process the form data as needed, such as saving it to the database
        
        # For now, let's just return a simple response
        return HttpResponse("Sales application submitted successfully!")
    else:
        return HttpResponse("Method not allowed")