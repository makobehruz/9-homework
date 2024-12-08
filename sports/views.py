from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'index.html')

def movie_list(request):
    sports = Post.objects.all()
    ctx = {'sports': sports}
    return render(request, 'sports/list.html', ctx)

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
            return redirect('sports:list')
    return render(request, 'sports/form.html')

def movies_detail(request, pk):
    sports = get_object_or_404(Post, pk=pk)
    ctx = {'sports': sports}
    return render(request, 'sports/detail.html', ctx)

def movies_update(request, pk):
    sports = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        date = request.POST.get('date')
        if title and director and genre and date:
            sports.title = title
            sports.director = director
            sports.genre = genre
            sports.date = date
            sports.save()
            return redirect(sports.get_detail_url())
    ctx = {'sports': sports}
    return render(request, 'sports/form.html', ctx)

def movies_delete(request, pk):
    sports = get_object_or_404(Post, pk=pk)
    sports.delete()
    return redirect('sports:list')






