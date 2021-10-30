from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('EmployeeApp.urls'))
]

# from django.contrib import admin
# from django.urls import path
#
# from django.conf.urls import url,include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^', include('EmployeeApp.urls'))
# ]
