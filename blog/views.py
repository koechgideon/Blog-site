from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Files
from .forms import FileForm
from .cypherCode import Cypher,ValidationError
from django.contrib.auth.models import User

class PostListView(ListView):
    model=Files
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=3

'''class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=4
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model=Post'''

def upload_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                myfile = request.FILES.get('file', None)
                password = request.POST.get('password', None)
                title = request.POST.get('title', None)
                about = request.POST.get('about', None)
                encrypted_file = Cypher().encrypt_file(myfile, password, extension='enc')
                files = Files.objects.create(file=encrypted_file,title=title,about=about)
                files.save()
                return redirect('files_list')
            except ValidationError as e:
                print(e)
            
    else:
        form = FileForm()
    
    return render(request, 'blog/upload.html', {'form': form})

'''class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False'''

def about(request):
  return render(request,'blog/about.html',{'title':'About'})

