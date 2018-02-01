from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    # 1. 브라우저에서 요청
    # 2. 요청이 runserver로 실행중인 서버에 도착
    # 3. runserver는 요청을 Django code로 전달
    # 4. Django code중 config.urls 모듈이 해당 요청을 받음
    # 5. config.urls 모듈은 ''(admin/를 제외한 모든 요청)을 blog.urls 모듈로 전달
    # 6. blog.urls 모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 연결된 함수(view)를 실행
    # 7-1. settings모듈의 TEMPLATES 속성 내의 DIRS 목록에서 blog/post_list.html 파일의 내용을 가져옴
    # 7-2. 가져온 내용을 적절히 처리(렌더링, render()함수)하여 리턴
    # 8. 함수의 실행 결과를 브라우저로 다시 전달

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )
    # 위 return 코드와 같음
    # return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    if request.method == 'POST':  # 요청의 종류가 무엇인지 확인 가능. post일때
        title = request.POST['title']  # post 받은 내용은 QueryDic이라는 딕셔너리 형태로 넘어 옴.
        content = request.POST['content']
        post = Post.objects.create(
            author=request.user,  # admin으로 로그인 한 상태에서만 사용 가능 -> 지금 사용자라는 의미
            title=title,
            content=content,
        )
        return redirect('post-detail', pk=post.pk)
    else:  # get일때
        return render(request, 'blog/post_add.html')


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'blog/post_list.html')
