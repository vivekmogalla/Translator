from django.urls import path

from .import views

urlpatterns = [
    path('', view=views.translate, name='translate'),
    path('success/', views.success_page, name='success_page'),
    # path(route='info', view=views.translate, name='translate'),
    # path('translation/success/', views.translation_success, name='translation_success'),
]