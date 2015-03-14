from django.shortcuts import render
from frontpage_users.forms import UserForm, UserProfileForm 
from frontpage.views import index
from django.contrib.auth import authenticate, login 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout

def register(request):

	registered = False 

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user 

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
			return index(request)

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
			'frontpage_users/register.html',
			{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			# if there's a user object 
			if user.is_active:
				# user might not be active
				login(request, user) # log into session
				return HttpResponseRedirect('/frontpage/')
			else:
				return HttpResponse("Your account is disabled")

		else:
			print("Invalid login details:{0}, {1}".format(username, password))
			return HttpResponse("Invalid Login details.")

	else:
		return render(request, 'frontpage_users/login.html', {})

def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/frontpage/')
