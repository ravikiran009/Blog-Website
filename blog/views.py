from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,UpdateForm,CategoryForm,AddCommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.
def Home(request):
    return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = "all_posts.html"
    ordering = ['-date']
    # ordering = ['-id']

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView,self).get_context_data(*args,**kwargs)
        p = get_object_or_404(Post,id=self.kwargs['pk'])
        liked = False
        if p.likes.filter(id=self.request.user.id).exists():
            liked = True
        total_likes = p.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"]=total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = "add_comment.html"
    success_url = reverse_lazy('allposts')
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCommentView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "edit_post.html"
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('allposts')
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request,cat):
    category_posts = Post.objects.filter(category=cat)
    return render(request,'categories.html',{'category_name':cat.title(),'category':category_posts})

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    categories = Category.objects.all()
    return render(request,'category_list.html',{'category_list':categories})

def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))
