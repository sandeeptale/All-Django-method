
from django.urls import path
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('empAPI/',views.empAPI.as_view(),name='empAPI'),
    path('POSTAPI/',views.POSTAPI.as_view(),name='POSTAPI'),

]