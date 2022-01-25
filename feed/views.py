# Go check ccbv.co.uk

from django.contrib import messages
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
    # THESE 'my_thing' & 'posts' ARE USED IN "home.html"
        context['my_thing'] = "Hello world :), this is dynamic"
    # FROM models.py, USING CLASS NAMED 'Post'
    # OR FROM feed/migrations/0001_initial.py -> IN operations IN fields={id & text}
    # GET ALL THE Post objects AND ORDER THEM BY ID DESCENDING ORDER (NEWEST AT THE VERY TOP)
    # THESE 'posts' & 'posts' ARE USED IN "home.html"
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post


class AddPostView(FormView):
    template_name = "new_post.html"
    # FROM forms.py
    form_class = PostForm
    success_url = "/"

#  CHECK OUT IN ccbv.co.uk -> FormView
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print("form.cleaned_data['text']")
        print("form.cleaned_data['image']")
        #  CREATE NEW POST
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        # self.request IS COMING FROM def dispatch() WITHIN THIS CLASS
        messages.add_message(self.request, messages.SUCCESS, 'Your Post was successful')
        #  IF IT IS VALID, THEN RETURN TO HOME PAGE
        return super().form_valid(form)

