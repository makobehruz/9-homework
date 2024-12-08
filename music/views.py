from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'index.html')

def movie_list(request):
    music = Post.objects.all()
    ctx = {'music': music}
    return render(request, 'music/list.html', ctx)

def movies_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        date = request.POST.get('date')
        if title and director and genre and date:
            Post.objects.create(
                title = title,
                director = director,
                genre = genre,
                date = date,
            )
            return redirect('music:list')
    return render(request, 'music/form.html')

def movies_detail(request, pk):
    music = get_object_or_404(Post, pk=pk)
    ctx = {'music': music}
    return render(request, 'music/detail.html', ctx)

def movies_update(request, pk):
    music = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        date = request.POST.get('date')
        if title and director and genre and date:
            music.title = title
            music.director = director
            music.genre = genre
            music.date = date
            music.save()
            return redirect(music.get_detail_url())
    ctx = {'music': music}
    return render(request, 'music/form.html', ctx)

def movies_delete(request, pk):
    music = get_object_or_404(Post, pk=pk)
    music.delete()
    return redirect('music:list')






