from django.contrib.auth.mixins import LoginRequiredMixin

class RamaisLoginRequired(LoginRequiredMixin):
	login_url = "/autentica/loga/"