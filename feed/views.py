from django.views.generic import TemplateView

# FROM models.py IMPORT CLASS NAME 'Post'
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

# CHECK  OUT  ccbv.co.uk
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    # THESE 'my_thing' & 'posts' ARE USED IN home.html
        context['my_thing'] = "Hello world :), this is dynamic"
    # FROM models.py, USING CLASS NAMED 'Post'
        context['posts'] = Post.objects.all()
        return context