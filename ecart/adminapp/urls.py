
from django.urls import path
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('testAPI/',views.testAPI.as_view(),name='testAPI'),
]
