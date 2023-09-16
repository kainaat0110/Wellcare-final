from django.urls import path
from home import views
from blog import views as bv
from diary import views as dv
from chatbot import views as cv
from chartapp import views as ccv



urlpatterns = [
    path('', views.index, name="index"),
    path('comm.html', views.index2, name="community"),
    path('login.html',views.login1 ,name="login"),
    path('afterlogin.html',views.afterlogin,name="afterlogin"),
    path('blog_index.html', bv.PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', bv.PostDetail.as_view(), name='blog_post_detail'),
    path('diary.html',dv.index,name='diary_home'),
    path('add.html', dv.add,name='add'),
    path('chatbot/index.html',cv.index,name='index'),
    path('getResponse',cv.getResponse,name='getResponse'),
    path('therapist.html',views.therapist,name="therapist"),
    path('games.html',views.games,name="games"),
    path('sos.html',views.sos,name="sos"),
    path('dc.html',views.dc,name="dc"),
    path('ac.html',views.ac,name="ac"),
    path('aissues.html',views.anger,name="anger"),
    path('Hi.html',views.Hi,name="Hi"),
    path('ri.html',views.ri,name="ri"),
    path('ms.html',views.ms,name="ms"),
    path('chartapp/index.html',ccv.index99,name="chartapp"),
    path('sos.html',views.sos,name="sos"),
    path('sos2.html',views.sos2,name="sos2"),
    
]
