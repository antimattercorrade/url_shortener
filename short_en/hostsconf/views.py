# from django.http import HttpResponseRedirect
# from django.conf import settings
# from django.shortcuts import render

# # DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL")

# def wildcard_redirect(request, path=None):
# 	# new_url=' '
# 	# return HttpResponseRedirect(new_url)
# 	if request.method == "POST":
# 		print(request.POST)
# 	return render(request, 'shortener/success.html', {})