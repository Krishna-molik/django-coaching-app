from django.shortcuts import render,HttpResponse,redirect
from .forms import ReviewForm
from .models import UserDetails

# Create your views here.
def home(request):
	# return HttpResponse("Hello World")
	return render(request,"index.html")		

def Course(request):
	return render(request,"courses.html")

def review(request):
	UserReview = UserDetails.objects.all()
	context = {'UserReview':UserReview}
	return render(request,"review.html",context)

def review_forms(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST, request.FILES)
		if form.is_valid():
			Review = form.save(commit=False)
			Review.user = request.user
			Review.save()
			return redirect('/reviews')
	else:
		form = ReviewForm()
	return render(request,'Review_create.html',{'form':form})






