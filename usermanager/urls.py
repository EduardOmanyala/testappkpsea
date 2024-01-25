from django.urls import path
from usermanager import views as manage_views

urlpatterns = [
    path('questionlist/browse', manage_views.questionListAll, name='questionlist_all'),
    path('questionlist/english', manage_views.questionListEnglish, name='questionlist_english'),
    path('questionlist/science', manage_views.questionListScience, name='questionlist_science'),
    path('questionlist/social', manage_views.questionListSocial, name='questionlist_social'),
    path('questionlist/kiswahili', manage_views.questionListKiswahili, name='questionlist_swahili'),
    path('verify_email/test', manage_views.verifyEmail, name='verifyemail'),
    path('verify_email/iLdxMr8pCW0p57u0/68yhz2uu/<int:id>/$2y$10$Oixfkm5gRoCjlmHRgDVB5Z0T2RQ/', manage_views.EmailVerificationComplete, name='emailVerificationComplete'),
    path('blank/404', manage_views.blank, name='blank_404'),
]