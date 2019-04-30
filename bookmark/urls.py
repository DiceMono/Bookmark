from django.urls import path

from .views import BookmarkList, BookmarkCreate, BookmarkDelete, BookmarkDetail, BookmarkUpdate
# 옛날 버전에
# namespace 이름공간
# 다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해서 사용
# namespace라는 인수가 존재

app_name = 'bookmark'
urlpatterns = [
    # path(url pattern, view, url pattern name),
    # 함수형 뷰 : 이름만
    # 클래스형 뷰: 이름.as_view()
    # 이름이 있어야 하는 이유는 주소를 가져다 써야할 때
    # converter -> path, uuid, slug, int, str(기본값), custom converter도 가능
    path('detail/<int:pk>/', BookmarkDetail.as_view(), name = 'detail'),
    path('delete/<int:pk>/', BookmarkDelete.as_view(), name = 'delete'),
    path('update/<int:pk>/', BookmarkUpdate.as_view(), name = 'update'),
    path('create/', BookmarkCreate.as_view(), name = 'create'),
    path('', BookmarkList.as_view(), name = 'index'),
]