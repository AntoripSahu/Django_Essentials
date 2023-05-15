from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = "notes/notes_list.html" # Specify your own template

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes' : all_notes})

class NotesDetailView(DetailView):
    try: 
        model = Notes
        context_object_name = "note"
        template_name = "notes/notes_detail.html"
    except Notes.DoesNotExist:
        template_name = request, 'notes/notes_error.html'

# def detail(request, pk):
#     try: 
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         # raise Http404("Note doesn't exist")
#         return render(request, 'notes/notes_error.html', {})
#     return render(request, 'notes/notes_detail.html', {'note' : note})
# Create your views here.
