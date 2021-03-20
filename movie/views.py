from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def index(request):
    movies = Movie.objects.all()
    return render(request,"index.html",{'movies':movies})

@login_required
@permission_required('view movie')
def create(request):
    form = MovieForm(request.POST or None , request.FILES or None)
    if form.is_valid():
         form.save()
         return redirect('index')
    return render(request,'create.html',{'form':form})

@login_required
def show(request, id):
    movies = Movie.objects.get(pk = id)
    return render(request,'show.html',{'movie':movies})   
@login_required
@permission_required('movie.Movie',raise_exception=True)
def update(request,id):
    movies = Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None , request.FILES or None,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'edit.html',{'form':form ,'movie':movies})

    
@login_required
@permission_required
def delete(request, id):
    movies = Movie.objects.get(pk= id)
    movies.delete()
    return redirect('index')
    
