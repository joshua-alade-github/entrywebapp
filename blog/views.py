from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from itertools import chain
from users.models import Follow, User, Profile, Message
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    )

from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
    }

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    return render(request, 'blog/home.html', context)

def get_post_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Post.objects.filter(
            Q(title__icontrains =q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'search_posts.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Post.objects.filter(title__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, resultsCount = self.results.count(), **kwargs)

class SearchUserView(LoginRequiredMixin, TemplateView):
    template_name = 'search_profiles.html'
    context_object_name = 'profiles'
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Profile.objects.filter(username__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, resultsCount = self.results.count(), **kwargs)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return []
        else:
            my_profile = Profile.objects.get(user=self.request.user)
            users = [follow_user.follow_user for follow_user in Follow.objects.filter(user=self.request.user)]
            posts = []
            qs = None
            for u in users:
                p = Profile.objects.get(user=u)
                p_posts = p.profiles_posts()
                posts.append(p_posts)
            my_posts = my_profile.profiles_posts()
            posts.append(my_posts)
            if len(posts)>0:
                qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.date_posted)
            return qs

@login_required
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats).annotate(likes_count=Count('likes')).order_by('-date_posted__date', '-likes_count')
    page = request.GET.get('page', 1)

    paginator = Paginator(category_posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/categories.html', {'cats': cats, 'category_posts': posts})

@login_required
def CategoryListView(request):
    categories = []
    category_list = Post.CATEGORY_TYPES
    for category in category_list:
        categories.append(category[0])
    return render(request, 'blog/categories_list.html', {'categories': categories})

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    def get_object(self, **kwargs):
        id = get_object_or_404(User, username=self.kwargs.get('username')).id
        profile = Profile.objects.get(id=id)
        return profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        profile = self.get_object()
        Check_following = Follow.objects.filter(user=self.request.user)
        if Check_following.filter(follow_user=profile.user).exists():
            followed = True
        else:
            followed = False
        context['profile'] = profile
        context['followed'] = followed
        return context

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        this_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = this_post.total_likes()
        context["total_likes"] = total_likes
        my_profile = Profile.objects.get(user=self.request.user)
        if my_profile.user in this_post.likes.all():
            liked = True
        else:
            liked = False
        context['liked'] = liked
        if this_post in my_profile.view_later.all():
            view_later = True
        else:
            view_later = False
        context['view_later'] = view_later
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'post_type', 'video_path', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def follow_unfollow_profile(request):
    if request.method =="POST":
        Check_following = Follow.objects.filter(user=request.user)
        id = request.POST.get('profile_id')
        other_user = User.objects.get(id=id)

        if Check_following.filter(follow_user=other_user).exists():
            Follow.objects.filter(follow_user=other_user).delete()
        else:
            Follow.objects.create(user=request.user, follow_user=other_user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles-list')

@login_required
def LikePostView(request, pk):
    postID = request.POST.get('liked_posts_id')
    post = get_object_or_404(Post, id=postID)
    my_profile = Profile.objects.get(user=request.user)
    if my_profile.user in post.likes.all():
        post.likes.remove(request.user)
        my_profile.liked_posts.remove(post)
    else:
        post.likes.add(request.user)
        my_profile.liked_posts.add(post)
    return HttpResponseRedirect(reverse('post-detail', args=[int(pk)]))

@login_required
def ViewLaterView(request, pk):
    postID = request.POST.get('nview_posts_id')
    post = get_object_or_404(Post, id=postID)
    my_profile = Profile.objects.get(user=request.user)
    if post in my_profile.view_later.all():
        my_profile.view_later.remove(post)
    else:
        my_profile.view_later.add(post)
    return HttpResponseRedirect(reverse('post-detail', args=[int(pk)]))

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'blog/profiles_list.html'
    context_object_name = 'profiles'

    paginate_by = 10

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

class FollowingListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'blog/following_list.html'
    context_object_name = 'profiles'

    paginate_by = 10

    def get_queryset(self):
        my_profile = Profile.objects.get(user=get_object_or_404(User, username=self.kwargs.get('username')))
        users = [follow_user.follow_user for follow_user in Follow.objects.filter(user=my_profile.user)]
        profiles = []
        for u in users:
            profiles.append(Profile.objects.get(user=u))
        return profiles

    def get_object(self, **kwargs):
        id = get_object_or_404(User, username=self.kwargs.get('username')).id
        profile = Profile.objects.get(id=id)
        return profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        profile = self.get_object()
        Check_following = Follow.objects.filter(user=self.request.user)
        if Check_following.filter(follow_user=profile.user).exists():
            followed = True
        else:
            followed = False
        context['profile'] = profile
        context['followed'] = followed
        return context

class FollowersListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'blog/followers_list.html'
    context_object_name = 'profiles'

    paginate_by = 10

    def get_queryset(self):
        my_profile = Profile.objects.get(user=get_object_or_404(User, username=self.kwargs.get('username')))
        users = [user.user for user in Follow.objects.filter(follow_user=my_profile.user)]
        profiles = []
        for u in users:
            profiles.append(Profile.objects.get(user=u))
        return profiles

    def get_object(self, **kwargs):
        id = get_object_or_404(User, username=self.kwargs.get('username')).id
        profile = Profile.objects.get(id=id)
        return profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        profile = self.get_object()
        Check_following = Follow.objects.filter(user=self.request.user)
        if Check_following.filter(follow_user=profile.user).exists():
            followed = True
        else:
            followed = False
        context['profile'] = profile
        context['followed'] = followed
        return context

class LikedListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'blog/liked_posts_list.html'
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        user = self.get_object()
        return user.liked_posts.all()

    def get_object(self, **kwargs):
        id = get_object_or_404(User, username=self.kwargs.get('username')).id
        profile = Profile.objects.get(id=id)
        return profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        profile = self.get_object()
        Check_following = Follow.objects.filter(user=self.request.user)
        if Check_following.filter(follow_user=profile.user).exists():
            followed = True
        else:
            followed = False
        context['profile'] = profile
        context['followed'] = followed
        return context

class ViewLaterListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'blog/view_later_posts_list.html'
    context_object_name = 'posts'

    paginate_by = 10

    def get_queryset(self):
        user = self.get_object()
        return user.view_later.all()

    def get_object(self, **kwargs):
        id = get_object_or_404(User, username=self.kwargs.get('username')).id
        profile = Profile.objects.get(id=id)
        return profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        profile = self.get_object()
        Check_following = Follow.objects.filter(user=self.request.user)
        if Check_following.filter(follow_user=profile.user).exists():
            followed = True
        else:
            followed = False
        context['profile'] = profile
        context['followed'] = followed
        return context

@login_required
def Inbox(request):
	messages = Message.get_messages(user=request.user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Message.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0

	context = {
		'directs': directs,
		'chat_messages': messages,
		'active_direct': active_direct,
		}

	template = loader.get_template('blog/direct.html')

	return HttpResponse(template.render(context, request))

@login_required
def UserSearch(request):
	query = request.GET.get("q")
	context = {}

	if query:
		users = User.objects.filter(Q(username__icontains=query))

		#Pagination
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)

		context = {
				'users': users_paginator,
			}

	template = loader.get_template('blog/search_user.html')

	return HttpResponse(template.render(context, request))

@login_required
def Directs(request, username):
	user = request.user
	messages = Message.get_messages(user=user)
	active_direct = username
	directs = Message.objects.filter(user=user, recipient__username=username)
	directs.update(is_read=True)
	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0

	context = {
		'directs': directs,
		'chat_messages': messages,
		'active_direct':active_direct,
	}

	template = loader.get_template('blog/direct.html')

	return HttpResponse(template.render(context, request))


@login_required
def NewConversation(request, username):
	from_user = request.user
	body = ''
	try:
		to_user = User.objects.get(username=username)
	except Exception as e:
		return redirect('usersearch')
	if from_user != to_user:
		Message.send_message(from_user, to_user, body)
	return redirect('inbox')

@login_required
def SendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')

	if request.method == 'POST':
		to_user = User.objects.get(username=to_user_username)
		Message.send_message(from_user, to_user, body)
		return redirect('inbox')
	else:
		HttpResponseBadRequest()

def checkDirects(request):
	directs_count = 0
	if request.user.is_authenticated:
		directs_count = Message.objects.filter(user=request.user, is_read=False).count()

	return {'directs_count':directs_count}
