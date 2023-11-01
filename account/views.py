from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import RegistrationForm
from .token import account_activation_token
from .models import UserBase

def account_register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.email = register_form.cleaned_data['email']
            user.set_password(register_form.cleaned_data['password'])
            # user.contact_number(register_form.cleaned_data['contact_number'])
            user.delivery_address(
                register_form.cleaned_data['delivery_address'])
            user.is_active = False
            user.save()

            # send user email for activation
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.doomain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)

    else:
        register_form = RegistrationForm()
        return render(
            request=request, 
            template_name='account/registration/register.html', 
            context={'form': register_form})
    
def account_login(request):
    pass

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        return redirect(
            to='account/dashboard'
        )
    else:
        return render(
            request=request,
            template_name='account/registration/activation_invalid.html'
        )
