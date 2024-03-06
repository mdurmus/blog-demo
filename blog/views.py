from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # model = Post Bütün datayi göster demek bu satir ile 
    # asagidaki iki satir ayni isi yapiyor.
    queryset = Post.objects.all()
    template_name = "post_list.html"
