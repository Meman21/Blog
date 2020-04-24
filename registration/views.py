from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse




# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created. You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html', {'form':form})


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST, 
        request.FILES,instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated')
            return redirect('profile')
    else: 
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'profile.html',context)


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject= f'Message from{form.cleaned_data["name"]}'
            sender = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            recipients = ['hanifi21@icloud.com']
            try:
                send_mail(subject,message,sender,recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            messages.success(request, f'Succes ... Your email has been sent')
            # return HttpResponse('Succes ... Your email has been sent')
            return redirect('contact')
    return render(request, 'contact.html', {'form': form})

    
