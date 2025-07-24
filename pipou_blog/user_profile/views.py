from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from authentication.models import User

@login_required
def profile_view(request, user_id):
    print(f"--- DANS LA VUE PROFILE POUR L'UTILISATEUR ID: {user_id} ---")
    user_profile = get_object_or_404(User, id=user_id)
    print(f"--- UTILISATEUR TROUVÉ: {user_profile.username} ---")
    return render(request, 'user_profile/profile.html', {'user_profile': user_profile})