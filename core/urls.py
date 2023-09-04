from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    #path('subjects/categories', core_views.subjectcategories, name='subjects'),
    path('subjects/categories/maths', core_views.maths, name='maths'),
    path('subjects/categories/english', core_views.english, name='english'),
    path('subjects/categories/kiswahili', core_views.kiswahili, name='kiswahili'),
    path('subjects/categories/science', core_views.science, name='science'),
    path('subjects/categories/social', core_views.social, name='social'),
    path('myresults', core_views.myresults, name='myresults'),
    path('stop/test', core_views.stoptest, name='stop-test'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('register/', core_views.register, name='register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="core/reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="core/password_reset_done.html"), name='password_reset_complete'),
    path('dashboard', core_views.dashboard, name='dashboard'),
    #path('newdashboard', core_views.newdashboaord, name='new-dashboard'),
    path('categories-questions/<int:cat_id>', core_views.category_questions, name='category-questions'),
    path('free-category-questions/<int:cat_id>', core_views.free_category_questions, name='free-category-questions'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', core_views.submit_answer, name='submit-answer'),
    path('profile', core_views.profile, name='profile'),
    path('about', core_views.about, name='about'),
    path('contactus', core_views.contactus, name='contactus'),
]



