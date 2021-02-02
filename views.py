from django.shortcuts import render,redirect
from register.models import registermodel
from .forms import registerform
from django.contrib.auth.models import User
from login.forms import loginform

# Create your views here.




def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phno = form.cleaned_data['phno']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']





            reg=registermodel()
            reg.modelname=name
            reg.modelphno=phno
            reg.modelemail=email
            reg.modelusername = username
            reg.modelpassword=password
            reg.modelconfirmpassword=confirmpassword


            if password == confirmpassword:
                try:
                    user = User.objects.get(modelusername=username)
                    context = {'form': form,
                           'error': 'The username you entered has already been taken. Please try another username.'}
                    return render(request, 'siteusers/signup.html', context)
                except User.DoesNotExist:
                    user = User.objects.create_user(username, modelpassword=confirmpassword, email=emailvalue)
            reg.save()





            return redirect('login')



    else:
        form=registerform()
        return render(request,'register/register.html',{'form':form})


