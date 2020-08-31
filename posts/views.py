from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, FormMixin
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from posts.models import Post, PostAttachment
from posts.forms import PostCreateForm, PostFilterForm
from posts.utility import POST_CREATE_VIEW, POST_LIST_VIEW, POST_VIEW_CONTEXT_NAME

# -------------
# Create your views here.

# test_view, requires refactoring


def posts_view(request):
    return render(request, 'posts/_posts_base.html')


class PostCreateView(FormView):
    form_class = PostCreateForm
    template_name = POST_CREATE_VIEW
    success_url = '/posts/'

    def form_valid(self, form):
        valid_response = super(PostCreateView, self).form_valid(form)

        # handling post creation
        post_text = form.cleaned_data.get('post_text')
        post = Post(post_text=post_text)
        post.author = self.request.user
        Post.save(post)

        # handling post images saving
        attachments = self.request.FILES.getlist('post_attachments')
        if len(attachments) > 0:
            self._save_attachments(attachments, post)

        return valid_response

    # helper method post images
    def _save_attachments(self, attachments_list, post):
        for f in attachments_list:
            img_attachment = PostAttachment(post=post)
            img_attachment.attachment_img = f
            PostAttachment.save(img_attachment)


class PostListView(ListView, FormMixin):
    form_class = PostFilterForm
    model = Post
    template_name = POST_LIST_VIEW
    context_object_name = POST_VIEW_CONTEXT_NAME
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            filter = self.request.session.get('post_filter')

            #requires refactoring
            if filter:
                if filter == 'oldest':
                    self.object_list = self.model.oldest_posts()
                elif filter == 'newwest':
                    self.object_list = self.model.newwest_posts()
                elif filter == 'lastday':
                    self.object_list = self.model.lastday_posts()
            else:
                self.object_list = self.model.objects.all().order_by('-created')
            #----------------------

        context = super(PostListView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        posts_filter = self.request.GET.get('post_filter_choice', None)

        if posts_filter:
            request.session['post_filter'] = posts_filter
            self.queryset = None

        context = self.get_context_data(form=self.form)

        return self.render_to_response(context)
