from django.urls import path, include
from django.contrib.auth.views import logout_then_login
from . import views
from django.conf import settings 
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<int:eventid>', views.event, name='event'),
    path('events', views.events, name='events'),
    path('notice/<int:noticeid>', views.notice, name='notice'),
    path('noticeboard', views.noticeboard, name='noticeboard'),
    path('achievement/<int:achievementid>', views.achievement, name='achievement'),
    path('achievements', views.achievements, name='achievements'),
    path('about', views.about, name='about'),
    path('post/comment', views.postComment, name="post_comment"),
    path('login', views.login, name='login'),
    path('', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),
    path('custom_logout', views.custom_logout, name='custom_logout'),
    path('addBoarders', views.addBoarders, name='addBoarders'),
    path('importFromExcel', views.import_from_excel, name='importFromExcel'),
    path('complain', views.complain, name='complain'),
    path('submit', views.submit_form, name='submit_form'),
    path('showComplaints', views.showComplaints, name='showComplaints'),
    path('updateStatus', views.updateStatus, name='updateStatus'),
    path('complain_status', views.complain_status, name='complain_status'),
    path('fullComplain/<int:complain_id>', views.showFullComplain, name='fullComplain'),
    path('khoj', views.khoj, name='khoj'),
    path('library', views.library, name='library'),
    path('checkout', views.checkout, name='checkout'),
    path('checkedOutBooks', views.checkedOutBooks, name='checkedOutBooks'),
    path('approve', views.approve, name='approve'),
    path('checkIn', views.checkIn, name='checkIn'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  