"""Defines URL patterns for coffee_websites"""

from django.urls import path

from . import views

app_name = 'coffee_websites'

urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
	# Page that shows all beans.
	path('beans/', views.beans, name='beans'),
	# Page for a single bean
	path('beans/<int:bean_id>/', views.bean, name='bean'),
	# Page for a single review
	path('reviews/<int:review_id>/', views.review, name='review'),
	# Page for adding a new review
	path('new_review/<int:bean_id>/', views.new_review, name='new_review'),
	# Page for editing a review
	path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
	# Page for each user and their reviews
	path('users/<str:username>/', views.user_reviews, name='user_reviews'),
]
