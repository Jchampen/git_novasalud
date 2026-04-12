from django.urls import path, include
from django.views.generic import RedirectView
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profesionales', views.ProfesionalViewSet)


urlpatterns = [
    path('crear/', views.crear_profesional, name='crear_profesional'),
    path('lista/', views.profesionales_list, name='profesionales_list'),
    path('formProfesionales/', RedirectView.as_view(pattern_name='crear_profesional', permanent=True), name='form_profesionales'),
    path('editar/<int:id>/', views.editar_profesional, name='editar_profesional'),
    path('actualizar/<int:id>/', views.editar_profesional, name='actualizar_profesional'),
path('eliminar/<int:id>/', views.eliminar_profesional, name='eliminar_profesional'),
path('confirmar_eliminar/<int:id>/', views.eliminar_profesional, name='confirmar_eliminar_profesional'),
path('', include(router.urls)),
]