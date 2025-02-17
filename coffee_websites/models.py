from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bean(models.Model):
	"""A bean the user can choose to review"""
	name = models.CharField(max_length=200)

	def __str__(self):
		"""Return a string representation of the model"""
		return self.name

class Review(models.Model):
	"""A bean the user can choose to review"""
	bean = models.ForeignKey(Bean, on_delete=models.CASCADE)
	rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model"""
		return self.title
