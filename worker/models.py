from django.db import models

# Create your models here.
class Registration(models.Model):
	"""docstring for Login"""
	WorkerId=models.IntegerField(default=1)
	FirstName=models.CharField(max_length=20)
	EmailId=models.CharField(max_length=50)
	PhNo=models.IntegerField(max_length=10)
	Password=models.CharField(max_length=20)

	def __str__(self):
		return self.WorkerId+" "+self.FirstName+" "+self.EmailId+" "+self.PhNo+" "+self.Password+" "+"<br>"
		
		