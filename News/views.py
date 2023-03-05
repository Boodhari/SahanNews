from django.shortcuts import render
from .models import Category,Post
from django.core.paginator import Paginator

# Create your views here.
def Homeview(request):
    cts =Category.objects.order_by('-id')
    Lp = Post.objects.order_by('-id')
    ps = Post.objects.order_by('-id') [:6]
    paginator = Paginator(Lp ,2)
    page= request.GET.get('page')
    postss=paginator.get_page(page)
    context={
        'cats':cts,
        'posts':ps,
        'postss':postss,
    }
   

    return render(request,'News/index.html',context)

