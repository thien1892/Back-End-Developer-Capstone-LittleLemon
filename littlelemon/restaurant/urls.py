from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemsView.as_view()),
    path('booking/tables', views.BookingViewSet.as_view({'get': 'list',
                                                         'post':'create',
                                                        #  'put': 'update',
                                                        #  'delete': 'destroy',
                                                        #  'patch': 'partial_update',
                                                         })),
    path('booking/tables/<int:pk>', views.BookingViewSet.as_view({'get': 'retrieve',
                                                        #  'post':'create',
                                                         'put': 'update',
                                                         'delete': 'destroy',
                                                         'patch': 'partial_update',
                                                         })),
    path('api-token-auth/', obtain_auth_token),
]