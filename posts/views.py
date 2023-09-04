from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from . import models
from accounts.models import Profile
from .forms import PostForm
from .models import Post
from django.views import generic
from django.views.generic.edit import CreateView

def AllView(request):
    if request.user.is_authenticated is None:
        return redirect('login')
    try:
        posts = models.Post.objects.order_by('-created_data')
        print(list(posts))
    except:
        posts = None
    finally:
        return render(request, 'home.html', context={"posts": posts})
    # try:
    #     profile = Profile.objects.get(user=request.user)
    # except:
    #     profile = Profile.objects.create(user=request.user)
    #     profile.save()
    # for user in profile.follows.all():
    #     posts.append(models.Post.objects.filter(user=user))
    # return render(request, 'home.html', context={"posts": posts})

def post_list_and_create(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same page after creating a post

    else:
        form = PostForm()
    return render(request, 'home.html', {'posts': posts, 'form': form})



class CreatePostView(CreateView):
    model = Post
    template_name = 'posts/post-create.html'
    fields = ['image', 'description', 'user']
    success_url = reverse_lazy('home')


def PostDetailView(request, pk):
    if request.user.is_authenticated is None:
        return redirect('login')
    else:
        post = models.Post.objects.get(pk=pk)
        return render(request, 'posts/post-detail.html', context={'post': post})


def EditView(request):
    if request.user.is_authenticated is None:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = PostForm()
            if form.is_valid():
                form = PostForm(request.POST)
            return render(request, 'posts/post-edit.html', context={"form": form})


class DeleteView(generic.edit.DeleteView):
    model = models.Post
    success_url = reverse_lazy('home')
    template_name = 'posts/post-delete.html'


def LikeView(request, pk):
    post = get_object_or_404(models.Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('about', args=[str(pk)]))
