
from django.urls import path
from hr import views
urlpatterns = [
    path('hrdash/',views.hrhome,name='hr_dash'),
    path('post_job/',views.post_job,name='post_job'),
    path('candidate_details/<int:pk>',views.candidate,name='candidate_details'),
    path('select-candidate/',views.selectedCandidate,name='selectedcandidate'),
    path('delete-candidate/',views.deleteCandidate,name='deletecandidate'),
    path('about/',views.about,name='about'),
    path('send_email/<int:candidate_id>/', views.send_email, name='send_email'),

]