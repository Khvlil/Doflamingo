from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
        path('beautifullsoup/', views.beautifullsoup, name='beautifullsoup'),
            path('django/', views.django, name='django'),
                path('numpy/',views.numpy, name='numpy' ),
                    path('request/', views.request, name='request'),
                        path('flask/', views.flask, name='flask'),
                            path('panda/', views.panda, name='panda'),
                                path('matplotib/', views.matplotib, name='matplotib'),
                                    path('tester/', views.tester, name='tester'),
]
