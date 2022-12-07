from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dictionaries import apis as dict_api
from users import apis as users_api
from slowniki import apis as slowniki_api

router = DefaultRouter()
router.register(r'axes', dict_api.AxisViewset)
router.register(r'measures', dict_api.MeasuresViewset)
router.register(r'pwd_tree', dict_api.ListPWDViewset, basename='pwd_tree')
router.register(r'pwds', dict_api.PwdViewset)
router.register(r'programmes', dict_api.ProgrammeViewset)
router.register(r'users', users_api.UserViewset)
router.register(r'institutional_roles', users_api.InstitutionalRoleViewset)
router.register(r'subjects', users_api.SubjectViewset, basename='subject')
router.register(r'organisations', users_api.OrganisationViewset)
router.register(r'persons', users_api.PersonViewset)
router.register(r'dictionaries/new/specification',
                slowniki_api.EntryFieldSpecificationApi)
router.register(r'dictionaries/new', slowniki_api.DictionaryCreateApi,
                basename='slowniki/nowy')
router.register(r'dictionaries', slowniki_api.DictionariesListApiViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
