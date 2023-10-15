from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import Post,Category,Comment,Profile
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from cee.settings import EMAIL_HOST_USER





# def home(request):
#     return render(request,'home.html',{})

# def blogpost(request):
#     return render(request,'blogpost.html',{})

class Homeview(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Homeview,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)

        post = self.object

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"]=cat_menu
        context["total_likes"] = total_likes
        context["liked"]=liked
        context["comment_form"] = CommentForm()  # Create an instance of the form

        author_profile = get_object_or_404(Profile, user=post.author)
        context["page_user"] = author_profile

        
        return context

class AddPostView(CreateView):
    model=Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','author')

# class AddCommentView(CreateView):
#     model=Comment
#     form_class = CommentForm
#     template_name = 'add_comment.html'
#     success_url = reverse_lazy('home')
#     # fields = '__all__'
#     # fields = ('title','author')
#     def form_valid(self,form):
#         form.instance.post_id = self.kwargs['pk']
#         return super().form_valid(form)

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def get_success_url(self):
        # Redirect to the article detail page where the comment was added
        return reverse('article-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']  # Assign the post_id
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        # Initialize the form and context here if needed
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # Process form submission and add the comment
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    

class AddCategoryView(CreateView):
    model=Category
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title','author')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'Update_post.html'
    # fields = ['title','title_tag','body']
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'


from django.views.generic import ListView
from .models import Post, Category

class Categoryview(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-post_date']

    def get_queryset(self):
        cats = self.kwargs['cats']  # Retrieve the 'cats' parameter from URL
        category = cats.replace('-', ' ')
        return Post.objects.filter(category=category)

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["cats"] = self.kwargs['cats'].title().replace('-', ' ')
        return context


# def Categoryview(request, cats):
#     category_posts = Post.objects.filter(category=cats.replace('-',' '))
#     return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})

class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryListView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

# def CategoryListView(request):
#     cat_menu_list = Category.objects.all()
#     return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
    
class AboutView(ListView):
    model = Post
    template_name = 'about.html'
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AboutView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
# def AboutPage(request):
#     return render(request, 'about.html', {})


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context


# def BlogPage(request):
#     return render(request, 'blog.html', {})

from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Post, Category

class ContactView(ListView):
    model = Post
    template_name = 'contact.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('fname')  # Change to match the form field IDs
        name1 = request.POST.get('lname')  # Change to match the form field IDs
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        

        
        email_message = f'Name: {name} {name1}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'
        recipient_list = email

        # send_mail(
        #      subject,
        #      email_message,
        #      EMAIL_HOST_USER,
        #      ["kaybernard449@gmail.com"]
        # )

        message_back = f"Thank you for reaching out to Pharmasage Solutions! We have received your message and appreciate your inquiry.\n\nOur team is reviewing it and will respond soon.\n\nThank you for your patience, and we look forward to connecting with you shortly.\n\nBest regards,\nDr. Sarah Naserian\nPharmasage Solutions"

        # send_mail(
        #      "Thank you for contacting us!",
        #      message_back,
        #      EMAIL_HOST_USER,
        #      [email]
        # )

        # Redirect to a thank you page or back to the contact form
        return self.get(request, *args, **kwargs)