from django.views.decorators.csrf import ensure_csrf_cookie
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from tasks.views import TaskViewSet, TaskListViewSet, CommentViewSet, UserRegistrationView, MyTokenObtainPairView, TaskView
from django.http import HttpResponse
from rest_framework import permissions

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tasklists', TaskListViewSet)
router.register(r'comments', CommentViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for Your Project",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/task/', TaskView.as_view(), name='Task'),
]
