from django.shortcuts import redirect, render
# View에 Model(Post 게시글) 가져오기
from .models import Post

def index(request):
    return render(request, 'main/index.html')

def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlists = Post.objects.all().order_by('-postname')
    num_count = postlists.count()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴 
    return render(request, 'main/blog.html', {'postlists':postlists, 'num_count':num_count})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.FILES.get('mainphoto'):
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.FILES['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto='white.jpg',
            )
        # new_article=Post.objects.create(
        #         postname=request.POST['postname'],
        #         contents=request.POST['contents'],
        #         mainphoto=request.FILES['mainphoto'],
        #     )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

def edit(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/edit.html', {'post':post})

def update(request, pk):
    post = Post.objects.get(pk=pk)
    post.postname = request.POST['postname']
    if request.FILES.get('mainphoto'):
        post.mainphoto = request.FILES.get('mainphoto')
    post.contents = request.POST['contents']
    post.save()
    return redirect('posting', post.pk)