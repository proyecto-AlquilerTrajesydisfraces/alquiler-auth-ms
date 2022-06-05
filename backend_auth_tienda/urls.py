from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from auth_tienda                    import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/',                 admin.site.urls),
    path('login/',                 TokenObtainPairView.as_view()),
    path('refresh/',               TokenRefreshView.as_view()),
    path('verifyToken/',           views.VerifyTokenView.as_view()),
    path('user/',                  views.UserCreateView.as_view()),
    path('user/<int:pk>/',         views.UserDetailView.as_view()),
    path('user/update/<int:pk>/',  views.UserUpdateView.as_view()),
    path('user/delete/<int:pk>/',  views.UserDeleteView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   
]
