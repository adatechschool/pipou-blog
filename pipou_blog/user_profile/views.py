from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from authentication.models import User
from blog.models import Post

@login_required
def profile_view(request, user_id):
    print(f"--- DANS LA VUE PROFILE POUR L'UTILISATEUR ID: {user_id} ---")
    user_profile = get_object_or_404(User, id=user_id)
    print(f"--- UTILISATEUR TROUVÉ: {user_profile.username} ---")

    user_posts = Post.objects.filter(user=user_profile)
    print(f"Nombre de posts trouvés : {user_posts.count()}")
    return render(request, 'user_profile/profile.html', {'user_profile': user_profile, "user_posts": user_posts})
