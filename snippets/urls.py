from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

'''
class-based views를 사용하기 위해 아래 코드를 수정한 것

path('snippets/', views.snippet_list),
path('snippets/<int:pk>', views.snippet_detail),

ex) views의 SnippetList라는 클래스를 view처럼 사용
'''

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])