from django.urls import path
from.import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('listAPI/',views.listAPI.as_view(),name='listAPI'),
    path('logAPI/',views.logAPI.as_view(),name='logAPI'),
    

]


