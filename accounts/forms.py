from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.password_validation import validate_password


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='User Name')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User Name or Password    is wrong!")
        return super(LoginForm, self).clean()




class RegisterForm(forms.ModelForm):
    pos = (('1', 'Planning Engineer'), ('2', 'Manager'), ('3', 'General Manager'), ('4', 'Tendering Specialist'),
           ('5', 'Project Coordinator'), ('6', 'General Coordinator'),
           ('7', 'Busines Development Specialist'), ('8', 'Bidding Engineer'), ('9', 'Academics'),)

    username = forms.CharField(max_length=100, label='User Name')
    position = forms.Select(choices = pos)
    password1 = forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    password2 = forms.CharField(max_length=100, label='Password again', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The passwords don't match!")
        return password2

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            instance.groups.add(Group.objects.get(name='New Member'))






########
#########
############# Turkish ########


class LoginFormTr(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Şifre', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı Adı veya Şifre yanlış")
        return super(LoginFormTr, self).clean()



class RegisterFormTr(forms.ModelForm):
    pos = (('1', 'Planning Engineer'), ('2', 'Manager'), ('3', 'General Manager'), ('4', 'Tendering Specialist'),
           ('5', 'Project Coordinator'), ('6', 'General Coordinator'),
           ('7', 'Busines Development Specialist'), ('8', 'Bidding Engineer'), ('9', 'Academics'),)

    username = forms.CharField(max_length=100, label='Kulllanıcı Adı')
    first_name = forms.CharField(max_length=100, label='Ad')
    last_name = forms.CharField(max_length=100, label='Soyad')
    email = forms.CharField(max_length=100, label='E-mail')
    position = forms.Select(choices = pos)
    password1 = forms.CharField(widget=forms.PasswordInput,validators=[validate_password], label='Şifre')
    password2 = forms.CharField(max_length=100, label='Şifre Tekrar', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler Eşleşmiyor")
        return password2

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            instance.groups.add(Group.objects.get(name='New Member'))