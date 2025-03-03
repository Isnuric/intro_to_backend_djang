from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница → редирект на /threads
def home_redirect(request):
    return redirect('thread_list')

# Список Thread'ов
def thread_list(request):
    threads = Thread.objects.all()
    form = ThreadForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('thread_list')
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

# Детали Thread + его посты
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.thread = thread
        post.save()
        return redirect('thread_detail', id=id)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

# Удаление Thread
def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

# Редактирование Thread
def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    form = ThreadForm(request.POST or None, instance=thread)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('thread_detail', id=id)
    return render(request, 'post/thread_edit.html', {'form': form})

# Удаление Post
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

# Редактирование Post
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    form = PostForm(request.POST or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('thread_detail', id=thread_id)
    return render(request, 'post/post_edit.html', {'form': form})
