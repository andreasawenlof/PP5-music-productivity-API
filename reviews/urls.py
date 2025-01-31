from django.urls import path
from .views import ReviewList, ReviewDetail, ReviewCreate, ReviewUpdate, ReviewDelete, ReviewHistoryList, ReviewHistoryDetail, ReviewHistoryCreate, ReviewHistoryUpdate, ReviewHistoryDelete

urlpatterns = [
    path('', ReviewList.as_view(), name='review_list'),
    path('create/', ReviewCreate.as_view(), name='review_create'),
    path('<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('<int:pk>/update/', ReviewUpdate.as_view(), name='review_update'),
    path('<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),
    path('history/', ReviewHistoryList.as_view(), name='review_history_list'),
    path('history/create/', ReviewHistoryCreate.as_view(),
         name='review_history_create'),
    path('history/<int:pk>/', ReviewHistoryDetail.as_view(),
         name='review_history_detail'),
    path('history/<int:pk>/update/', ReviewHistoryUpdate.as_view(),
         name='review_history_update'),
    path('history/<int:pk>/delete/', ReviewHistoryDelete.as_view(),
         name='review_history_delete'),
]
