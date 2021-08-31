# Create your views here.
from math import ceil

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from more_itertools import chunked

from Blog.forms import TagForm, PostForm
from Blog.models import Post, Tag


class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        tags = Tag.objects.annotate(posts_count=Count("posts")).order_by("-posts_count")
        popular_tags = tags[:5]
        return render(request, 'blog/index.html', context={"posts": posts,
                                                           "tags": popular_tags})


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


def tag_list(request):
    tags = Tag.objects.annotate(posts_count=Count("posts")).order_by("-posts_count")
    half_page = len(tags) / 2
    tags1, tags2 = chunked(tags, ceil(half_page))
    return render(request, 'blog/tags_list.html', context={'tags1': tags1,
                                                           'tags2': tags2})


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_create.html', context={'form': bound_form})
