from django.contrib import admin

# Register your models here.

# 관리자 페이지를 커스터마이징
# 옵션 클래스를 만들어서 추가

from .models import Bookmark

class BookmarkOptions(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'url']
    # list_editable = ['site_name', 'url'] 리스트에서 편집 가능은 위험할 수 있음
    # list_filter = ['url'] # 대부분 DateTime 필드가 있을경우 많이 사용
    search_fields = ['site_name', 'url'] # ForeignKey 필드 같은 다른 테이블을 참조하는 항목은 x
    # raw_id_fields : 선택값 -> 입력값

admin.site.register(Bookmark, BookmarkOptions)