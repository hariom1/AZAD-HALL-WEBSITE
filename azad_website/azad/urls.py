from django.urls import path

from . import views

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

]
