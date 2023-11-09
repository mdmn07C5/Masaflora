from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import RegistrationForm, UserEditForm
from .token import account_activation_token
from .models import UserBase


def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.user_name = register_form.cleaned_data['user_name']
            user.email = register_form.cleaned_data['email']
            user.set_password(register_form.cleaned_data['password'])
            user.contact_number = register_form.cleaned_data['contact_number']
            user.is_active = False
            user.save()

            # send user email for activation
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')

    else:
        register_form = RegistrationForm()
        return render(
            request=request,
            template_name='account/registration/register.html',
            context={'form': register_form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect(
            to='account:dashboard'
        )
    else:
        return render(
            request=request,
            template_name='account/registration/activation_invalid.html'
        )


@login_required
def dashboard(request):
    return render(
        request=request,
        template_name='account/user/dashboard.html',)

@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if not user_form.is_valid():
            print(user_form.errors)
        if user_form.is_valid():
            print('EE BOI')
            user_form.save()

    else:
        user_form = UserEditForm(instance=request.user)

    return render(
        request=request,
        template_name='account/user/edit_details.html',
        context={'user_form': user_form}
    )
        