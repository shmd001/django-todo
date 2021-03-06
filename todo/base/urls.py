"""URL routing for base app"""

from django.urls import path
from .views import (
    TaskDelete,
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    UserSignin,
    UserSignout,
    UserSignup,
)

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
    path("signin/", UserSignin.as_view(), name="signin"),
    path("signout/", UserSignout.as_view(), name="signout"),
    path("signup/", UserSignup.as_view(), name="signup"),
]
