from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'index.html')

def movie_list(request):
    travel = Post.objects.all()
    ctx = {'travel': travel}
    return render(request, 'travel/list.html', ctx)

def movies_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        if title and director and genre and description:
            Post.objects.create(
                title = title,
                director = director,
                genre = genre,
                description = description,
            )
            return redirect('travel:list')
    return render(request, 'travel/form.html')

def movies_detail(request, pk):
    travel = get_object_or_404(Post, pk=pk)
    ctx = {'travel': travel}
    return render(request, 'travel/detail.html', ctx)

def movies_update(request, pk):
    travel = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        if title and director and genre and description:
            travel.title = title
            travel.director = director
            travel.genre = genre
            travel.description = description
            travel.save()
            return redirect(travel.get_detail_url())
    ctx = {'travel': travel}
    return render(request, 'travel/form.html', ctx)

def movies_delete(request, pk):
    movies = get_object_or_404(Post, pk=pk)
    movies.delete()
    return redirect('travel:list')






