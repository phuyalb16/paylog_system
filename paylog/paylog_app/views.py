from django.shortcuts import render
from .models import Details
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='login')
def search(request):
    if (request.method == 'POST') and request.POST.get('search'):
        search_person = request.POST.get('search').capitalize()
        return_person = Details.objects.filter(name__contains = search_person)
        return render(request, 'search_person.html', {'person_details' : return_person, 'search_person': search_person})
    elif (request.method == 'POST') and request.POST.get('del_pd'):
        search_person = request.POST.get('username').capitalize()
        delete_person(request.POST.get('del_pd'))
        return_person = Details.objects.filter(name__contains=search_person)
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

def delete_person(pk_value):
    people = Details.objects.filter(id=pk_value).delete()

@login_required(login_url='login')
def main_view(request):
    people = Details.objects.order_by('bought_date')

    if request.POST.get('delete'):
        pk_value = request.POST.get('delete')
        delete_person(pk_value)
    if request.POST.get('search'):
        search(request)
    else:
        post_details(request, people)

    return render(request, 'main_view.html', {'people': people})

@login_required(login_url='login')
def all_users(request):
    customers = Details.objects.values('name').distinct()
    paginator = Paginator(customers, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    users = paginator.get_page(page)
    if request.POST.get('search'):
        return search(request)
    return render(request, 'all_users.html', {'users': users})

