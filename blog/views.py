from django.shortcuts import render
from blog.models import Post, Comment
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)
# Create your views here.

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        comment = request.POST['comment']
        Comment.objects.create(
            post=post,
            content=comment,
        )
    print(post)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)

def post_add(request):
    #print(request.POST)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        thumbnail = request.FILES['thumbnail']
        post = Post.objects.create(title=title, content=content, thumbnail=thumbnail)
        #print(title, content)
        return redirect(f'/posts/{post.id}')
    return render(request, 'post_add.html')