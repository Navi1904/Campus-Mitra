from django.urls import path
from candidate import views
urlpatterns = [
    
     path('candidate_dashbordh/',views.candidate_dashbordh,name='candidate_dashbordh'),
     path('my-job-list/',views.myJobListviews,name='myJobListviews'),
     path('apply-for-job/<int:pk>/',views.applyforjob,name='applyforjob'),
     path('aboutcompany',views.aboutcom,name='aboutcom'),

]
