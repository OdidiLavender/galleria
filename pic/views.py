from email.mime import image
from django.shortcuts import get_object_or_404, render,HttpResponse
from .models import Image
from django.db.models import Q


# Create your views here.
def index(request):
    image=Image.objects.all()
    ctx = {'image': image}
    return render(request,'index.html',ctx)

def detail_view(request,id):
    obj=get_object_or_404(Image,id=id)
    return render(request,'detail.html',{'image':obj})

def search(request):
    query=None
    result=[]
    if request.method == 'GET':
            query=request.GET.get('search')
            result=Image.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))
    return render(request,'search.html',{'query':query,'result':result})    