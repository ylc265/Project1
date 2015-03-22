# -*- coding: utf-8 -*-

from frontpage.forms import SearchForm
from frontpage_users.forms import MyAuthenticationForm

def main_proc(request):
	authentication_form = MyAuthenticationForm
	form = SearchForm()
	login_form = authentication_form(request)
	return {
		'form':form,
		'login_form': login_form
	}