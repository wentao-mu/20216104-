from django.urls import path
from django.contrib import admin
from apps import views
from django.views.generic import RedirectView
urlpatterns = [
    # 页面
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    path('errors/', views.errors),
    path('index/', views.index),
    path('logout/', views.logout),
    path('home/', views.home),
    path('insert/', views.insert),
    path('detail/<int:paperid>/', views.detail),
    path('check/<int:paperid>/', views.check),
    path('modify/<int:paperid>/', views.modify),
    path('query/', views.query),
    path('createuser/', views.createuser),

    # 测试上传论文
    path('process_q/', views.query_process),
    
    # API
    path('get_code/', views.get_code, name='get_code'),
    path('download/<path:paperid>/', views.download, name="download"),
    path('set_password/', views.set_password),
    path('delete_tmp_paper', views.delete_tmp_paper),
    path('export/<path:paperids>/', views.export),
    path('bibtex/', views.bibtex),
    path('api_dropbox/', views.api_dropbox),
    path('api_checkTitle/', views.api_checkTitle),
    path('api_createUser/', views.api_createUser),

    # 管理员
    path('admin/', admin.site.urls),
]
