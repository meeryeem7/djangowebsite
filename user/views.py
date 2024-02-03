from django.shortcuts import render,redirect
from .forms import UserRegisterFrom,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST' :
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f"your account has been created for {username}")
            return redirect("blog-home")
    else:
        form = UserRegisterFrom()
    return render(request,"user/register.html", {"form":form})

@login_required()
def profile(request):
    if request.method == 'POST' :
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'user/profile.html',context)

