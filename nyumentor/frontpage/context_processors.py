# -*- coding: utf-8 -*-

from frontpage.forms import StyledSearchForm
from frontpage_users.forms import MyAuthenticationForm

def main_proc(request):
	authentication_form = MyAuthenticationForm
	form = StyledSearchForm()
	login_form = authentication_form(request)
	return {
		'search_form':form,
		'login_form': login_form
	}