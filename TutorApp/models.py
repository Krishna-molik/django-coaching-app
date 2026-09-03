from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.
class UserDetails(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(max_length=350)
	MobileNo = models.CharField(max_length=10, validators=[
		RegexValidator(
			regex=r'^[6-9]\d{9}$',
			message = "Enter a valid 10-digit mobile number"
			)
		]
		)
	Photo = models.ImageField(upload_to='media/', blank=True, null = True)

	def __str__(self):
		return f"{self.user.username}"

	class Meta:
		verbose_name='UserDetail' #singular matlab sirf ek record 
		verbose_name_plural='UserDetails' #plural matlab bohot saari list ke liye

#another alternate way of MobileNo but for this we have to use django.core.validators import MinValueValidator,MaxValueValidator
# MobileNo = forms.IntegerField( 
# 	validators=[
# 	MinValueValidators(1000000000), # 10 digit max
# 	MaxValueValidators(9999999999)  # 10 digit min
# 	]	
# 	) 





