from braces import views

class RamaisLoginRequired(views.LoginRequiredMixin, views.SuperuserRequiredMixin):
	login_url = "/autentica/loga/"