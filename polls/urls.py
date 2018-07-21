from django.urls import path
from . import views

app_name='polls'
urlpatterns=[
    path('',views.Index.as_view(),name='index'),
    path('<int:pk>/',views.Detail.as_view(),name='detail'),
    path('<int:id>/vote/',views.vote,name='vote'),
    path('<int:id>/<str:c>/results/',views.results,name='results'),
    path('create/',views.create,name='create'),
    path('create/choice',views.choice_form,name='choice_form')

]
