from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Comments, Profile, Post
from django.views import View
from django.utils import timezone
from .forms import PostForm, CommForm

# Create your views here.
def index(request):
    return render(request, "index.html")    

def AboutUs(request):
    return render(request, "About-Us.html")

def FAQ(request):
    return render(request, "FAQ.html")

def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('Register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Register')
        
        if len(username)>10:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('Register')
        
        if password != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Register')       
        
        user = User.objects.create_user(username, email, password)
        user.save
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model)
        new_profile.save()
       
        
        return redirect("index")
        
    else:
        return render(request, "Register.html")



# Login and Logout views

def login(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("feed")
        else:
            messages.error(request, "Invalid Username or Password. Please try again!")
            return redirect("login")
    
    else:
        return render(request, "Log-In.html")


def logout_view(request):
    logout(request)
    return redirect("/")



class News_feed_list(LoginRequiredMixin, View):
    # getting all onjects in post model and display in newest-last order
    def get(self, request, *args, **kwargs):
        feed = Post.objects.all().order_by("-created_at")
        form = PostForm
        
        #check if post liked by user, def var to be used in html to determine button
        liked = False
        for post in feed:
            if post.likes == request.user:
                liked == True
            else:
                liked == False
                
        
            
        context = {   
            "feed_list": feed,
            "form": form,
            "liked": liked
        }
        
        return render(request, "feed.html", context)
    
    # POST function to get all info from form, validating and adding to db, then populate feed with new post
    def post(self, request, *args, **kwargs):
        feed = Post.objects.all().order_by("-created_at")
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.creator = request.user
            new_post.save()
        
        context = {   
            "feed_list": feed,
            "form": form,
        }
        
        return render(request, "feed.html", context)
    
    def __str__(self):
        return self.name
        
# Function for post likes. Add or remove if user is in the liked list of a post        
def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)        
    else:       
        post.likes.add(request.user)
            
    return redirect("feed")

# Class for going on the post`s page when clicking on it (or comm)
class post_detail(LoginRequiredMixin, View):
    def get(self, request,pk, *args, **kwargs):
        detailed_post = Post.objects.get(pk=pk)
        comments = Comments.objects.filter(post=detailed_post).order_by("-created_at")
        comm_form = CommForm
        
        context = {
            "detailed_post": detailed_post,
            "comments":comments,
            "comm_form": comm_form,
        }
        return render(request, "post_detail.html", context)
    
    def post(self, request,pk, *args, **kwargs):
        detailed_post = Post.objects.get(pk=pk)
        comments = Comments.objects.filter(post=detailed_post).order_by("-created_at")
        comm_form = CommForm(request.POST)
        
        if comm_form.is_valid():
            new_comm = comm_form.save(commit=False)
            new_comm.creator = request.user
            new_comm.post = detailed_post
            new_comm.save()
        
        context = {  
            "detailed_post": detailed_post, 
            "comments": comments,
            "comm_form": comm_form,
        }
        
        return render(request, "post_detail.html", context)
    
    
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comments
    template_name = "comment_delete.html"
    
    
    def get_success_url(self):
        return reverse_lazy("feed")

    
# profile

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
           profile = Profile.objects.get(pk=pk)
           user = profile.user
           username = user.username
           posts = Post.objects.filter(creator=user).order_by("-created_at")
           context = {
               "user":user,
               "username":username,
               "profile":profile,
               "posts": posts
           }
           
           return render (request, "profile.html", context)
       

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "profile_update.html"
    fields = ["bio", "profileimg"]
    
    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse("profile", kwargs={"pk": pk})
       
class PasswordUpdate(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "password_update.html"
    
    
    def get_success_url(self):
           
           return reverse("password_success")

def passsword_success(request):
    return render(request, "password_success.html")
       
       
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    
    def get_success_url(self):
           
           return reverse_lazy("feed")
    
    