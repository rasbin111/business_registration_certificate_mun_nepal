from django.urls import path
# from .old_views import CertificateView, CertificateCreatedView
from .views import home_view, generate_certificate

urlpatterns = [
    path('', home_view, name='certificate-form'),
    path('generate-certificate/', generate_certificate, name='generate-certificate')
]