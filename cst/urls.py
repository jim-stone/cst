from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dictionaries import apis as dict_api
from users import apis as users_api

router = DefaultRouter()
router.register(r'institutions', dict_api.InstitutionViewset)
router.register(r'axes', dict_api.AxisViewset)
router.register(r'measures', dict_api.MeasuresViewset)
router.register(r'pwds', dict_api.ListPWDViewset, basename='pwds')
router.register(r'programmes', dict_api.ProgrammeViewset,
                basename='programmes')
router.register(r'users', users_api.UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]
