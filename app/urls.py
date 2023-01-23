from django.urls import path
from . import views  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path("", views.home, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("welcome/", views.after_login, name="afterLogin"),
    path("getlit/", views.get_lit, name="Get LIT"),
    path("yourplan/", views.your_plan, name= "Your Plan"),
    path("yourgoal/", views.goal, name="Your Goal"),
]