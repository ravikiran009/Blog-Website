from django import forms
from .models import Post,Category,Comment

choices = Category.objects.all().values_list('name','name') # Query set

choice_list = [('---------','---------')] # list

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your title here'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your title tag here'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','type':'hidden','id':'author'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Write your thoughts here...'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control','placeholder':'Write what you want to show on all posts page...'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your title here'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control','placeholder':'Your title tag here'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Write your thoughts here...'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control','placeholder':'Write what you want to show on all posts page...'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder' : 'Enter new Category'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','name')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','value':'','type':'hidden','id':'commentname'}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Write your comment here...'}),
        }