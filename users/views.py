from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUPForm,EditProfileForm,ProfilePageForm,EditProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import DetailView,UpdateView,CreateView
from blog.models import UserProfile

# Create your views here.

class CreateProfileView(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_profilepage.html'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(UpdateView):
    model = UserProfile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('allposts')


class ShowProfileView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'
    def get_context_data(self, *args,**kwargs):
        context = super(ShowProfileView,self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(UserProfile,id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class UserRegisterView(generic.CreateView):
    form_class = SignUPForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_credentials.html"
    success_url = reverse_lazy('allposts')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy('allposts')



