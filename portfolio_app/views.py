from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio


def index(request):
    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    #Visits
    #visits before next deploy
    history_views = 0
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1 if history_views == 0 else num_visits + 1 + history_views


    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context)