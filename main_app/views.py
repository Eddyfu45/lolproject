from django.http.response import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Champion
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def champions_index(request):
    champions = Champion.objects.all()
    return render(request, 'champions/index.html', { 'champions': champions })

def champions_show(request, champion_id):
    champion = Champion.objects.get(id=champion_id)
    return render(request, 'champions/show.html', {'champion': champion})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    champions = Champion.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'champions': champions})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/champions')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
        

class ChampionCreate(CreateView):
    model = Champion
    fields = ['name', 'title', 'lore', 'abilityNameQ', 'abilityDescriptionQ', 'abilityNameW', 'abilityDescriptionW', 'abilityNameE', 'abilityDescriptionE', 'abilityNameR', 'abilityDescriptionR']
    success_url = '/champions'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/champions' + str(self.object.pk))

class ChampionUpdate(UpdateView):
    model = Champion
    fields = ['name', 'title', 'lore', 'abilityNameQ', 'abilityDescriptionQ', 'abilityNameW', 'abilityDescriptionW', 'abilityNameE', 'abilityDescriptionE', 'abilityNameR', 'abilityDescriptionR']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/champions/' + str(self.object.pk))

@method_decorator(login_required, name='dispatch')
class ChampionDelete(DeleteView):
    model = Champion
    success_url ='/champions'