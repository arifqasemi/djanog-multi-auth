from django.shortcuts import render,redirect
from .forms import CustomerSignUpForm,ManagerSignUpForm
# Create your views here.
from django.views.generic import FormView
from .models import User
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')

class HomeView(View):
    def get(self, request):
        return render(request, "app/home.html")
    
class ManagerRegisterView(FormView):
    form_class = ManagerSignUpForm
    model = User
    template_name = "app/manager_register.html"
    success_url = "login"
    def form_valid(self, form):
        instance = form.save()
        # messages.success(self.request, 'Your account has been created. Please log in.') 
        return super().form_valid(form)
    
class CustomerRegisterView(FormView):
    form_class = CustomerSignUpForm
    model = User
    template_name = "app/customer_register.html"
    success_url = "login"
    def form_valid(self, form):
        instance = form.save()
        return super().form_valid(form)



def LoginView(request):
    error_message = None 
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Invalid username or password. Please try again."
        else:
            error_message = "Form validation failed. Please check your input."

    else:
        form = LoginForm
    return render(request,'app/login.html',{'form':form,'error_message': error_message})
