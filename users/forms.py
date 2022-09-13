from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import UserProfile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic','bio','website_url','facebook_url','instagram_url','twitter_url','pinterest_url']
        widgets = {
                # 'profile_pic' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your title here'}),
                'bio' : forms.Textarea(attrs={'class':'form-control','placeholder':'Your bio here'}),
                'website_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Website url if any'}),
                'facebook_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Facebook profile url if any'}),
                'instagram_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Instagram profile url if any'}),
                'twitter_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Twitter profile url if any'}),
                'pinterest_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Pinterest profile url if any'}),
            }

class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic','bio','website_url','facebook_url','instagram_url','twitter_url','pinterest_url']
        widgets = {
                # 'profile_pic' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your title here'}),
                'bio' : forms.Textarea(attrs={'class':'form-control','placeholder':'Your bio here'}),
                'website_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Website url if any'}),
                'facebook_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Facebook profile url if any'}),
                'instagram_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Instagram profile url if any'}),
                'twitter_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Twitter profile url if any'}),
                'pinterest_url' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your Pinterest profile url if any'}),
            }

class SignUPForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = {'username','first_name','last_name','email','password1','password2'}

        def __init__(self,*args,**kwargs):
            super(SignUPForm,self).__init__(*args,**kwargs)

            self.fields['username'].widget.attrs['class']='form-control'
            self.fields['password1'].widget.attrs['class']='form-control'
            self.fields['password2'].widget.attrs['class']='form-control'

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = {'username','first_name','last_name','email','password'}
