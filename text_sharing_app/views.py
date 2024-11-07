from django.shortcuts import render, redirect, get_object_or_404
from .forms import TextForm
from .models import SharedText
from markdown2 import markdown

# Create your views here.
def create_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)

        if form.is_valid():
            shared_text = form.save()
            return redirect('view_text', slug=shared_text.slug)
    else:
        form = TextForm()

    return render(request, 'create_text.html', {
        'form': form,
    })

def view_text(request, slug):
    shared_text = get_object_or_404(SharedText, slug=slug)
    rendered_content = markdown(shared_text.content)

    return render(request, 'view_text.html', {
        'rendered_content': rendered_content,
        'shared_text': shared_text,
    })

def edit_text(request, slug):
    shared_text = get_object_or_404(SharedText, slug=slug)

    if request.method == 'POST':
        form = TextForm(request.POST, instance=shared_text)

        if form.is_valid():
            form.save()
        
            return redirect('view_text', slug=shared_text.slug)
    else:
        form = TextForm(instance=shared_text)

    return render(request, 'edit_text.html', {
        'form': form,
        'shared_text': shared_text,
    })