from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.VideoListView.as_view(), name='index'),
    path("cash"+"<int:pk>/", views.AddressView.as_view(), name='twr'),
    path("cash"+"<int:pk>/", views.AddressView1.as_view(), name='twr1'),
    path("cash"+"<int:pk>/", views.AddressView2.as_view(), name='twr2'),
    path("cash"+"<int:pk>/", views.AddressView3.as_view(), name='twr3'),
    path("cash"+"<int:pk>/", views.AddressView4.as_view(), name='twr4'),
    path("cash"+"<int:pk>/", views.AddressView5.as_view(), name='twr5'),
    path("cash"+"<int:pk>/", views.AddressView6.as_view(), name='twr6'),
    path("cash"+"<int:pk>/", views.AddressView7.as_view(), name='twr7'),
    path("cash"+"<int:pk>/", views.AddressView8.as_view(), name='twr8'),
    path("cash"+"<int:pk>/", views.AddressView9.as_view(), name='twr9'),
    path("cash"+"<int:pk>/", views.AddressView10.as_view(), name='twr10'),
    path("cash"+"<int:pk>/", views.AddressView11.as_view(), name='twr11'),
    path("cash"+"<int:pk>/", views.AddressView12.as_view(), name='twr12'),
    path("cash"+"<int:pk>/", views.AddressView13.as_view(), name='twr13'),
    path("cash"+"<int:pk>/", views.AddressView14.as_view(), name='twr14'),
    path("cash"+"<int:pk>/", views.AddressView15.as_view(), name='twr15'),
    path("cash"+"<int:pk>/", views.AddressView16.as_view(), name='twr16'),
    path("cash"+"<int:pk>/", views.AddressView17.as_view(), name='twr17'),
    path("cash"+"<int:pk>/", views.AddressView18.as_view(), name='twr18'),
    path("cash"+"<int:pk>/", views.AddressView19.as_view(), name='twr19'),
    #path(r'^courses/(?P<pk>[\d]+)-(?P<slug>[+\-\w]+)/$', views.CourseCategoryDetailView.as_view(), name='course_category_detail'),
]
