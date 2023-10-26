
from django.urls import path
from home import views
urlpatterns = [
    # path('register',views.register,name='register'),
    path('',views.home, name='home'),

    path('homescreen',views.homescreen, name='homescreen'),
    path('mappingscreen',views.mappingscreen, name='mappingscreen'),
    path('sqlscrappingmapping',views.sqlscrappingmapping, name='sqlscrappingmapping'),
    path('lineagepushscreen',views.lineagepushscreen, name='lineagepushscreen'),
    path('Extract',views.mappingscreen, name='Extract'),
    path('mappingscreen.html',views.mappingscreen, name='mappingscreen'),
    path('sqlscrappingmapping.html',views.sqlscrappingmapping, name='sqlscrappingmapping'),
    path('lineagepushscreen.html',views.lineagepushscreen, name='lineagepushscreen'),
    path('homescreen.html',views.homescreen, name='homescreen'),
    path('Extract',views.mappingscreen, name='Extract'),
]



#     path('login',views.log, name='login'),
#     path('project1',views.project1,name='project1'),
#     path('project2',views.project2,name='project2'),
#     path('third',views.third,name='third'),
#     path('lgout',views.log_out, name='logout'),
#     path('edit/<id>',views.editData,name='edit')
    



   
   
   