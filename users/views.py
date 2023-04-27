from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from first_try.models import Anime
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import UserAnime


class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm 
    next_page = "main"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['errors'] = str(self.get_form().errors)

        return context



class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            UserAnime.objects.get_or_create(user=new_user)
            return HttpResponseRedirect(reverse("login"))
        else:
            for i in form.errors:
                print(form.errors[i][0])

        context = {"form": form,
                "errors":form.errors,}
        return render(request, self.template_name, context)
    


def exit(request):
    logout(request)
    return render(request,"first_try/main.html")