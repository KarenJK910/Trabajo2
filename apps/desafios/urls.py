from django.urls import path
from . import views 

app_name='desafios'

urlpatterns = [
    path('desafio1/',views.Desafio_1 ,name='Desafio_1'),
    path('desafio2/',views.Desafio_2 ,name='Desafio_2'),
    path('desafio3/',views.Desafio_3 ,name='Desafio_3'),
    path('desafio4/',views.Desafio_4 ,name='Desafio_4'),
    path('desafio5/',views.Desafio_5 ,name='Desafio_5'),
    path('desafio6/',views.Desafio_6 ,name='Desafio_6'),
    path('desafio7/',views.Desafio_7 ,name='Desafio_7'),
    path('desafio8/',views.Desafio_8 ,name='Desafio_8'),
    path('desafio9/',views.Desafio_9 ,name='Desafio_9'),
    path('desafio10/',views.Desafio_10 ,name='Desafio_10'),
    path('desafio11/',views.Desafio_11 ,name='Desafio_11'),
    path('desafio12/',views.Desafio_12 ,name='Desafio_12'),
    path('desafio13/',views.Desafio_13 ,name='Desafio_13'),
    path('desafio14/',views.Desafio_14 ,name='Desafio_14'),
    path('desafio15/',views.Desafio_15 ,name='Desafio_15'),
    path('desafio16/',views.Desafio_16 ,name='Desafio_16'),
    path('desafio17/',views.Desafio_17 ,name='Desafio_17'),
]
