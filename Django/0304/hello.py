def blog(request):
    db = Blog.objects.all()
    db2 = Blog.objects.all().order_by('-id')[:3]
    form = BlogForm()
    context = {
        'db': db,
        'db2': db2, # 추가하고 싶을 때 1
    }
    context['form'] = form # 추가하고 싶을 때 2
    return render(request, 'blog/blog.html', context)