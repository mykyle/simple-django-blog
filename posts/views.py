from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import *
from posts.forms import *
from django.contrib import messages

def post_home(request):
    return HttpResponse("<h3>welcome to the home url</h3>")

def post_show(request):
    # queryset=get_object_or_404(Post, id=1)
    queryset=Post.objects.all()
    context={"title":"Showing",
    "object_list":queryset}
    return render_to_response('post/index.html',context)
def post_details(request, pk):
    instance=get_object_or_404(Post, id=pk)

    variables=RequestContext(request, {"instance":instance,
    "title":instance.title,})
    return render_to_response('post/details.html',variables)
def post_create(request):
    # if request.method=='POST':
        # print (request.POST)
        # print (request.POST.get("title"))
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "created successfully")
    else:
        messages.info(request, "problem occured successfully")
    context=RequestContext(request,{"form":form,
    "title":"create form"})
    return render_to_response('post/form_create.html',context)

def post_update(request, pk):
    instance=get_object_or_404(Post, id=pk)
    form=PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.error(request, "Not updated successfully")
        return HttpResponseRedirect("/post/post_show")
    variables=RequestContext(request, {"instance":instance,
    "title":instance.title,
    "form":form,
    })
    return render_to_response("post/form_create.html",variables)
def post_value(request,pk):
        queryset=get_object_or_404(Post, id=pk)
        context=RequestContext(request,{"title":"Showing",
        "object_list":queryset,})
        return render_to_response('post/value.html',context)
