from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Bean, Review
from .forms import ReviewForm


# Create your views here.
def index(request):
	"""The home page for Coffee Site"""
	return render(request, 'coffee_websites/index.html')

def beans(request):
	"""Show all beans"""
	query = request.GET.get('q')
	if query:
		beans = Bean.objects.filter(name__icontains=query)
	else:
		beans = Bean.objects.all().annotate(avg_rating=Avg("review__rating"))

	# beans = Bean.objects.annotate(avg_rating=Avg("review__rating"))
	context = {'beans': beans, 'query': query}
	return render(request, 'coffee_websites/beans.html', context)

def bean(request, bean_id):
	"""Show a single bean and all its reviews"""
	bean = Bean.objects.get(id=bean_id)
	## uncomment for final site 
	# bean = get_object_or_404(Bean, id=bean_id)
	reviews = bean.review_set.order_by('-date_added')
	context = {'bean': bean, 'reviews': reviews}
	return render(request, 'coffee_websites/bean.html', context)

def review(request, review_id):
	"""Show a single review"""
	review = Review.objects.get(id=review_id)
	bean = review.bean
	context = {'bean': bean, 'review': review}
	return render(request, 'coffee_websites/review.html', context)

def user_reviews(request, username):
    user = get_object_or_404(User, username=username)
    reviews = Review.objects.filter(owner=user).order_by('-date_added')  # Get reviews in descending order

    context = {'user_profile': user, 'reviews': reviews}
    return render(request, 'coffee_websites/user_reviews.html', context)

# def user_page(request, user_id):
# 	"""Show all the reviews that a single user has left"""

# 	# Show only reviews made by current user
# 	reviews = Review.objects.filter(owner=request.user).order_by('data_added')

# 	# Show only reviews made by requested user
# 	reviews = Review.objects.filter(owner=user_id).order_by('data_added')

@login_required
def new_review(request, bean_id):
	"""Add a new review for a particular bean."""
	bean = Bean.objects.get(id=bean_id)

	if request.method != 'POST':
		# No data submitted, create a blank form
		form = ReviewForm()
	else:
		# POST data submitted; process data
		form = ReviewForm(data=request.POST)
		if form.is_valid():
			new_review = form.save(commit=False)
			# Set the bean of the review to the correct bean before saving
			new_review.bean = bean
			# Set the owner of the review to the user making it
			new_review.owner = request.user
			new_review.save()
			return redirect('coffee_websites:bean', bean_id=bean_id)

	# Display a blank or invalid form
	context = {'bean': bean, 'form': form}
	return render(request, 'coffee_websites/new_review.html', context)

@login_required
def edit_review(request, review_id):
	"""Edit an existing review"""
	review = Review.objects.get(id=review_id)
	bean = review.bean

	# Make sure the review belongs to the current user
	if review.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Initial request; pre-fill form with current entry
		form = ReviewForm(instance=review)
	else:
		# POST data submitted; process data
		form = ReviewForm(instance=review, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('coffee_websites:bean', bean_id=bean.id)

	context = {'review': review, 'bean': bean, 'form': form}
	return render(request, 'coffee_websites/edit_review.html', context)


