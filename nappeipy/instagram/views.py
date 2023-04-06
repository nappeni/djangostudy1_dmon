from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# post_list = ListView.as_view(model=Post, paginate_by=10)
# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q':q,
#     })

# @method_decorator(login_required, name="dispatch")
class PostlistView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostlistView.as_view()

# post_detail = DetailView.as_view(model=Post, queryset=Post.objects.filter(is_public=True))
# def post_detail(request:HttpResponse, pk:int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#
#     return render(request, 'instagram/post_detail.html', {
#         'post':post
#     })

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            # login 하지 않았을 경우,
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

def archives_year(request,year):
    return HttpResponse(f"{year}년 archives")