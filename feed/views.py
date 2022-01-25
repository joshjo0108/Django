# Go check ccbv.co.uk

from django.views.generic import TemplateView, DetailView, FormView

from .forms import PostForm

# FROM models.py IMPORT CLASS NAME 'Post'
from .models import Post

class HomePageView(TemplateView):
    # THIS IS THE ATTRIBUTE OF TemplateView
    template_name = "home.html"

# CHECK  OUT  ccbv.co.uk
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    # THESE 'my_thing' & 'posts' ARE USED IN home.html
        context['my_thing'] = "Hello world :), this is dynamic"
    # FROM models.py, USING CLASS NAMED 'Post'
        context['posts'] = Post.objects.all()
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post


class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        print("form.cleaned_data['text']")
        print("form.cleaned_data['image']")
        #  CREATE NEW POST
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        #  IF IT IS VALID, THEN RETURN TO HOME PAGE
        return super().form_valid(form)

