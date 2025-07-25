from django.test import TestCase, Client
from authentication.models import *
from django.urls import reverse
from django.conf import settings
from authentication.forms import RegisterForm


class RegisterViewTest(TestCase):
    
    def setUp(self):

        self.client = Client() 
        self.register_url = reverse('register') 
        
        # Données de test valides
        self.valid_user_data = {
            'username': 'Valentin',
            'first_name': 'Valentin',
            'last_name' : 'B',
            'email': 'valentinb@test.fr',
            'password1': '1234valb',
            'password2': '1234valb',
        }
        
        # Données de test invalides
        self.invalid_user_data = {
            'username': 'baduser',
            'first_name': 'Bad',
            'last_name' : 'User',
            'email': 'invalid-email',  
            'password1': 'testpassword123',
            'password2': 'differentpassword', 
        }

    def test_register_page_get_request(self):
        # On teste l'affichage de la page d'inscription lors d'un GET

        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form') 
        self.assertIsInstance(response.context['form'], RegisterForm)
        self.assertTemplateUsed(response, 'authentication/register.html')   


    def test_register_page_post_valid_data(self):
        # On teste l'inscription avec des données valides

        initial_user_count = User.objects.count()
        response = self.client.post(self.register_url, self.valid_user_data)
    
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(response.status_code, 302)  # Redirection après succès
        self.assertEqual(User.objects.count(), initial_user_count + 1)
    
        created_user = User.objects.get(username='Valentin')
        self.assertEqual(created_user.email, 'valentinb@test.fr')
        self.assertTrue(created_user.check_password('1234valb'))

        self.assertTrue('_auth_user_id' in self.client.session)


    def test_register_page_post_invalid_data(self):
        # On teste l'inscription avec des données invalides

        initial_user_count = User.objects.count()
        response = self.client.post(self.register_url, self.invalid_user_data)
    
        self.assertEqual(response.status_code, 200)  # Reste sur la même page
        self.assertTemplateUsed(response, 'authentication/register.html')

        self.assertEqual(User.objects.count(), initial_user_count)
        self.assertFormError(response, 'form', 'email', 'Saisissez une adresse de courriel valide.')
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_register_page_duplicate_email(self):
        #On teste l'inscription avec un utilisateur existant
    
        User.objects.create_user(
            username='existing_user',
            email='valentinb@test.fr',
            password='password123'
        )
    
        response = self.client.post(self.register_url, self.valid_user_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(email='valentinb@test.fr').count(), 1)


    def test_register_page_post_empty_data(self):
        # On teste l'inscription avec des données vides

        response = self.client.post(self.register_url, {})
    
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', 'Ce champ est obligatoire.')
        self.assertFormError(response, 'form', 'email', 'Ce champ est obligatoire.')

