from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.decorators import login_required	
from .forms import ReviewForm,UserCreationForm
from .models import UserDetails
from django.contrib.auth import login
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

def Registration(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			RegForm = form.save(commit=False)
			RegForm.set_password(form.cleaned_data['password1'])
			RegForm.save()
			login(request,RegForm)
			return redirect('/home')
	else:
		form = UserCreationForm()
	return render(request,"Register.html",{"form":form})

def delete(request,id):
	review = UserDetails.objects.get(id=id, user=request.user)
	if request.method == 'POST':
		review.delete()
		return redirect('/reviews')
	return render(request,'delete.html',{'review':review})

def edit(request,id):
	review = UserDetails.objects.get(id=id , user=request.user)
	if request.method=='POST':
		form = ReviewForm(request.POST,request.FILES,instance=review)
		if form.is_valid():
			EditReview = form.save(commit=False) 
			EditReview.user = request.user 
			EditReview.save()
			return redirect('/reviews')
	else:
		form = ReviewForm(instance=review)
	return render(request,'edit.html',{'form':form})





