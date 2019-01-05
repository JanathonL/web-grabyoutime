from django.contrib.auth.forms import UserCreationForm
from django import forms
from timer.models import User
from timer import models
from pagedown.widgets import PagedownWidget

class RegForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "username", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            self.add_error(u"email", u'Email addresses must be unique.')
        return email

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Comfirm Password'

## form to create group
class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group 
        exclude = ('create_date','manager','members') 

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'ui input'
        self.fields['detail'].widget = PagedownWidget(show_preview=True, template= 'pagedown.html')

## form to create project 
class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.GroupProject 
        exclude = ('create_date','creator','belong','status','start_date',
            'finish_date','members', 'spend_time','is_begin') 
        widgets = {
            'deadline': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'ui input'
        self.fields['estimate_time'].widget.attrs['class'] = 'ui input'
        self.fields['detail'].widget = PagedownWidget(show_preview=True, template= 'pagedown.html')

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label = "firstname", max_length=20)
    last_name = forms.CharField(label = "lastname", max_length=20)
    email = forms.EmailField(label = "Email", max_length=100)
    phone = forms.CharField(label = "Telephone", max_length = 20)
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'phone']
    

class MessageForm(forms.Form):
    content = forms.CharField(label='content')

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20, help_text='please enter your username')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
