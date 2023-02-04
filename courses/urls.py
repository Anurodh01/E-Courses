from django.urls import path
from courses.views import home, coursepage, SignUpView, LoginView,logoutpage , checkout, verify_payment, MycourseView, getCourseList
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', logoutpage , name='logout'),
    path('mycourses/', MycourseView.as_view(), name='mycourses'),
    path('checkout/<str:slug>/',checkout, name= 'checkout'),
    path('verify_payment/',verify_payment,name='verify_payment'),
    path('course/<str:slug>/', coursepage, name='coursepage'), 
    path('api/getcourselist/',getCourseList, name='courselist-api') 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)