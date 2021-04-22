
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from api import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/tasklists/', views.TaskListView.as_view(), name='taskslist'),

    path('api/tasklists/<int:pk>', views.TaskItemView.as_view(), name='task'),

    path('api/tasklists/<int:pk>/', views.TaskListDetail.as_view(), name='affect_list'),

    path('api/tasklists/<int:pk>/task', views.TaskItemView.as_view(), name='new_task'),

    path('api/tasklists/<int:tasklist_pk>/task/<int:pk>/', views.TaskItemDetailed.as_view(), name='affect_task'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
