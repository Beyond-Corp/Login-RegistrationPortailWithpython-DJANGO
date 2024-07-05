from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    return render(request, 'auth/index.html')


def signup(request):
    # Vérifie si la méthode de la requête est POST ou GET ou autre chose (comme PUT, DELETE, etc.) et exécute le code en conséquence pour chaque méthode.
    if request.method == 'POST':
        # Récupère les données du formulaire
        uname = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Vérifie si les mots de passe ne correspondent pas
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('signupP')  # Redirige vers la page d'inscription

        # Vérifie si le nom d'utilisateur existe déjà
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists')
            return redirect('signupP')  # Redirige vers la page d'inscription

        # Vérifie si l'email existe déjà
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signupP')  # Redirige vers la page d'inscription

        # Crée un nouvel utilisateur avec les informations fournies
        myuser = User.objects.create_user(uname, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()  # Sauvegarde l'utilisateur dans la base de données

        messages.success(request, 'Your account has been created')  # Affiche un message de succès
        return redirect('signinP')  # Redirige vers la page de connexion

    # Affiche le formulaire d'inscription si la méthode de la requête n'est pas POST
    return render(request, 'auth/signup.html')



def signin(request):
    # Vérifie si la méthode de la requête est POST
    if request.method == 'POST':
        # Récupère les données du formulaire
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')

        # Authentifie l'utilisateur
        user = authenticate(username=uname, password=pass1) ##Cette ligne utilise la fonction authenticate pour vérifier les informations d'identification fournies par l'utilisateur. avec les informations stockées dans la base de données.

        # Si l'utilisateur est authentifié avec succès
        if user is not None:  # Si l'utilisateur est authentifié, la fonction login est appelée pour connecter l'utilisateur.
            login(request, user)  # Connecte l'utilisateur  # # login(request, user)  La fonction login est utilisée pour connecter l'utilisateur.  # La fonction login prend request et user comme arguments.
            fname = user.first_name  # Récupère le prénom de l'utilisateur  # La variable fname est utilisée pour stocker le prénom de l'utilisateur.
            return render(request, 'auth/index.html', {'fname': fname})  # Affiche la page d'accueil avec le prénom de l'utilisateur  # La fonction render est utilisée pour renvoyer la page d'accueil avec le prénom de l'utilisateur. qui a été stocké dans la variable fname.
        else:
            messages.error(request, 'Invalid Credentials')  # Affiche un message d'erreur
            return redirect('signinP')  # Redirige vers la page de connexion

    # Affiche le formulaire de connexion si la méthode de la requête n'est pas POST
    return render(request, 'auth/signin.html')



def signout(request):
    logout(request)  # Déconnecte l'utilisateur
    messages.success(request, 'You have been logged out')  # Affiche un message de succès   # La fonction logout est utilisée pour déconnecter l'utilisateur.
    return redirect('signinP')  # Redirige vers la page de connexion  # La fonction redirect est utilisée pour rediriger l'utilisateur vers la page de connexion.


def dashboard(request):
    return render(request, 'auth/dashboard.html')









# Explication des deux vues
# signup Vue
# Vérification de la méthode: La vue commence par vérifier si la méthode de la requête est POST, ce qui indique que le formulaire a été soumis.
# Récupération des données: Les données du formulaire sont récupérées en utilisant request.POST.get().
# Vérification des mots de passe: Il vérifie si les mots de passe ne correspondent pas et affiche un message d'erreur si c'est le cas.
# Vérification des duplicata: Il vérifie si le nom d'utilisateur ou l'email existe déjà dans la base de données et affiche un message d'erreur si c'est le cas.
# Création de l'utilisateur: S'il n'y a pas d'erreurs, il crée un nouvel utilisateur avec les informations fournies et les enregistre dans la base de données.
# Message de succès: Un message de succès est affiché une fois l'utilisateur créé avec succès.
# Redirection: Après avoir créé l'utilisateur, la vue redirige vers la page de connexion.
# Affichage du formulaire: Si la méthode n'est pas POST, la vue affiche simplement le formulaire d'inscription.


# signin Vue
# Vérification de la méthode: La vue commence par vérifier si la méthode de la requête est POST, ce qui indique que le formulaire a été soumis.
# Récupération des données: Les données du formulaire sont récupérées en utilisant request.POST.get().
# Authentification: Elle essaie d'authentifier l'utilisateur en utilisant le nom d'utilisateur et le mot de passe fournis.
# Connexion réussie: Si l'authentification réussit, l'utilisateur est connecté et la vue affiche la page d'accueil avec un message de bienvenue.
# Connexion échouée: Si l'authentification échoue, un message d'erreur est affiché et l'utilisateur est redirigé vers la page de connexion.
# Affichage du formulaire: Si la méthode n'est pas POST, la vue affiche simplement le formulaire de connexion.