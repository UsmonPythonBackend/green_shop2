from django.shortcuts import render, redirect
from django.views import View
from blog.models import BlogNews
from .helpers import Pagination


class BlogView(View):
    def get(self, request, *args, **kwargs):
        blogs = BlogNews.get_queryset()
        page = int(request.GET.get('page', 1))
        pages = Pagination.page_pagination(blogs, 1, page)
        context = {'pages': pages, 'page': page, "previous_page": page - 1, "next_page": page + 1,
                   "next_page2": page + 2}
        return render(request, "blog.html", context)


class BlogDetailView(View):
    def get(self, request, id):
        blog = BlogNews.objects.get(id=id)
        return render(request, "blog-detail.html", {"product": blog})
