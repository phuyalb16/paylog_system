from django.shortcuts import render
from .models import MakeNotes
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def note_view(request):
    my_notes = MakeNotes.objects.all()
    if request.method == 'POST':
        if request.POST.get('entered_note'):
            post = MakeNotes()
            post.note = request.POST.get('entered_note')
            post.save()
        elif request.POST.get('delete_note'):
            pk_value= request.POST.get('delete_note')
            MakeNotes.objects.filter(id=pk_value).delete()
    return render(request, 'note.html', {'my_notes': my_notes})


