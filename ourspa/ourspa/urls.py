from django.urls import include, re_path
urlpatterns = [
    re_path(r'^api/', include('djoser.urls')),
    re_path(r'^api/', include('djoser.urls.jwt')),
    re_path(r'^api/', include('spauser.urls')),
]
