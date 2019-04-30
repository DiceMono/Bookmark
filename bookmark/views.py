from django.shortcuts import render

# Create your views here.

# 함수형 뷰는 자유도가 클래스형 뷰에 비해서 높다.
# 함수형 : def 뷰 이름(request[, 추가인수]):
#                   처리할 내용
# 처리할 코드를 직접 다 개발자가 작성

# CRUDL 에 관련 기능은 자주 사용 하기 때문에 장고에서 제네릭
# 클래스형 뷰는 생산성이 함수형 뷰에 비해 높다.
# 클래스형 : CLASS 뷰이름(제네릭뷰):
#         처리할 내용
# 제네릭 기능 외에 추가적인 기능을 개발자가 작성
# 메서드 방식 - 커스터마이징에 관련된 메서드를 찾아야한다.

# CRUD_L
from django.views.generic.list import ListView

# 클래스형 뷰의 이름은 자유
from .models import Bookmark

class BookmarkList(ListView):
    model = Bookmark

    # 템플릿 종류
    # 읽어오는 데이터
    # 페이지네이션을 걸거나
    # 검색 쿼리를 적용하거나
    # 권한 체크

# 뷰를 만들었다 -> url 연

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_create'
    success_url = '/'
    # _form

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_update'
    success_url = '/'
    # _form
class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = '/'
    # _confirm_delete

from django.views.generic.detail import DetailView

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name_suffix = '_detail'


