from django.shortcuts import render
from .models import Details
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def search(request):
    if (request.method == 'POST') :
        search_person = request.POST.get('search').capitalize()
        return_person = Details.objects.filter(name__contains = search_person)
        return render(request, 'search_person.html', {'person_details' : return_person, 'search_person': search_person})

def post_details(request, people):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('amount') and request.POST.get('input_items'):
            post = Details()
            post.name = request.POST.get('name')
            post.amount = request.POST.get('amount')
            post.item = request.POST.get('input_items')
            post.save()
            return render(request, 'main_view.html', {'people': people})

def delete_person(request):
    print(request.POST.get('person.name'))

@login_required(login_url='login')
def main_view(request):
    people = Details.objects.order_by('bought_date')

    if request.POST.get('delete'):
        delete_person(request)
    else:
        search(request)
        post_details(request, people)

    return render(request, 'main_view.html', {'people': people})





