from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'index.html')

def movie_list(request):
    movies = Post.objects.all()
    ctx = {'movies': movies}
    return render(request, 'movies/list.html', ctx)

def movies_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        release = request.POST.get('release')
        if title and director and genre and release:
            Post.objects.create(
                title = title,
                director = director,
                genre = genre,
                release = release,
            )
            return redirect('movies:list')
    return render(request, 'movies/form.html')

def movies_detail(request, pk):
    movies = get_object_or_404(Post, pk=pk)
    ctx = {'movies': movies}
    return render(request, 'movies/detail.html', ctx)

def movies_update(request, pk):
    movies = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        release = request.POST.get('release')
        if title and director and genre and release:
            movies.title = title
            movies.director = director
            movies.genre = genre
            movies.release = release
            movies.save()
            return redirect(movies.get_detail_url())
    ctx = {'movies': movies}
    return render(request, 'movies/form.html', ctx)

def movies_delete(request, pk):
    movies = get_object_or_404(Post, pk=pk)
    movies.delete()
    return redirect('movies:list')






