from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PostSblawat, Komentarz
from .serializers import PostSblawatSerializer

def post_list(request):
    posts = PostSblawat.objects.all().order_by('-created_at')
    najnowsze_posty = PostSblawat.objects.order_by('-created_at')[:5]
    popularne_posty = PostSblawat.objects.order_by('-views')[:5]

    return render(request, 'blog_sblawat/post_list.html', {
        'posts': posts,
        'najnowsze_posty': najnowsze_posty,
        'popularne_posty': popularne_posty
    })

def post_detail(request, pk):
    post = get_object_or_404(PostSblawat, pk=pk)
    post.views += 1
    post.save()

    komentarze = post.komentarze.all()

    return render(request, 'blog_sblawat/post_detail.html', {
        'post': post,
        'komentarze': komentarze
    })

def polub_post(request, pk):
    post = get_object_or_404(PostSblawat, pk=pk)
    post.likes_count += 1
    post.save()
    return redirect('post_detail', pk=pk)

def dodaj_komentarz(request, pk):
    post = get_object_or_404(PostSblawat, pk=pk)
    
    if request.method == 'POST':
        autor = request.POST.get('autor')
        tresc = request.POST.get('tresc')

        if autor and tresc:
            Komentarz.objects.create(post=post, autor=autor, tresc=tresc)

    return redirect('post_detail', pk=pk)

class PostSblawatListAPIView(APIView):
    def get(self, request):
        posts = PostSblawat.objects.all()
        serializer = PostSblawatSerializer(posts, many=True)
        return Response(serializer.data)
