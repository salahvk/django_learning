from django.shortcuts import render
from .models import MovieInfo
from .forms import MovieForm

# Create your views here.
def create(request):
    frm = MovieForm()
    if request.POST :
        title =request.POST.get('title')
        print(title)
        # year  =request.POST.get('year')
        poster  =request.FILES.get('poster')
        print(poster)
        # movie_obj = MovieInfo(title=title,year = year,description =desc)
        # movie_obj.save()
        frm = MovieForm(request.POST,request.FILES)
        print(request.POST)
        if frm.is_valid() :
          frm.save()
    else :
          frm = MovieForm()

    return render(request,'create.html',{'frm':frm})

def edit(request,pk):
    instance_to_beEdited = MovieInfo.objects.get(pk=pk)
    if request.POST:
         print(request.POST)
         frm = MovieForm(request.POST,instance=instance_to_beEdited)
         if frm.is_valid :
            frm.save()
    else :
        frm = MovieForm(instance=instance_to_beEdited)
        print('edit func')
        
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})

def list(request):
    movie_set = MovieInfo.objects.all()
    print("+++++++++++++++++++++")
    print(movie_set)
    print(MovieInfo.objects.get(id=1).title)
    # print(MovieInfo.objects.get(id=2))
    print("_______________**********")
    return render(request,'list.html',{'movies':movie_set})

def menu(request):
    return render(request,'menu.html')