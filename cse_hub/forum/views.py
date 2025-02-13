from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.contrib import messages
from problems.django.db import connection
from .models import Post, Comment
from django.urls import reverse


# displays home page of the discussion forum
def home(request):
	# posts = Post.objects.all()
	cursor = connection.cursor()
	posts = cursor.execute('SELECT * from forum_post', object=Post)
	return render(request, 'forum/home.html', {'posts':posts})
	

# user is required to be logged in to create a new post
@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)

		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			cursor = connection.cursor()
			codes = cursor.excute('insert into forum_post', object=form)
			messages.success(request, 'Created Post Successfully')
			return redirect(home)
		else:
			# print on backend terminal, for debugging purpose
			print(f'\n Error while creating post:\n{form.errors.as_data()} \n')

			form_error = list(form.errors.as_data().values())[0][0]
			# if user filled form was invalid, send a error message
			messages.error(request, 'Error Creating Post')

			# list unpacking to show the first error as pop-up message
			messages.error(request, *form_error)

	return render(request, 'forum/add_post.html', {'form':PostForm()})

# displays a certain post with its comments details
def display_post(request, post_id):
	# post = Post.objects.get(id=post_id)
	cursor = connection.cursor()
	post = cursor.execute('SELECT * from forum_post where id = ?', object=Post, id=post_id)
	# get all comments related to this post
	comments = post.comment_set.all()
	return render(request, 'forum/display_post.html', {'post':post, 'form':CommentForm(), 'comments':comments})

# login is required for the user to comment on a post
@login_required
def comment(request, post_id):
	# if user is redirected to this page after making a POST request to the form displayed
	if request.method == 'POST':
		# create a form with the data submitted by the user
		form = CommentForm(request.POST)

		# if the user submitted a valid data,
		if form.is_valid():
			# create an instance of the form but don't save
			form = form.save(commit=False)
			# add currently logged user as the author of the comment
			form.author = request.user
			# attach the current post to the comment
			# form.post = Post.objects.get(id=post_id)
			cursor = connection.cursor()
			form.post = cursor.execute('SELECT * from forum_comment where id = ?', object=Post, id=post_id)
			cursor = connection.cursor()
			cursor.excute('INSERT INTO forum_comment VALUES = ?', object=form)
			# display a success message
			messages.success(request, 'comment added Successfully')
		else:
			# print on backend terminal, for debugging purpose
			print(f'\n Error while adding problem:\n{form.errors.as_data()} \n')

			form_error = list(form.errors.as_data().values())[0][0]
			# if user filled form was invalid, send a error message
			messages.error(request, 'error adding comment')

			# list unpacking to show the first error as pop-up message
			messages.error(request, *form_error)
			
	# after a successful comment, redirect the user to same page with comment updated
	return HttpResponseRedirect(reverse('display-post', kwargs={'post_id':post_id}))

@login_required
def delete_comment(request, comment_id):
	# comment = Comment.objects.get(id=comment_id)
	cursor = connection.cursor()
	comment = cursor.execute('SELECT * from forum_comment where id = ?', object=Comment, id=comment_id)

	if comment.author.id != request.user.id:
		messages.error(request, 'Not allowed')
	else:
		comment.delete()
		messages.success(request, 'Deleted Comment Successfully')
	# redirect to same page: https://stackoverflow.com/a/35796330/10127204
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def delete_post(request, post_id):
	# post = Post.objects.get(id=post_id)
	cursor = connection.cursor()
	post = cursor.execute('SELECT * from forum_post where id = ?', object=Post, id=post_id)

	if post.author.id != request.user.id:
		messages.error(request, 'Not allowed')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	else:
		post.delete()
		messages.success(request, 'Deleted Post Successfully')
	return HttpResponseRedirect(reverse('forum-home'))
