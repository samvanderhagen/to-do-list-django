from django.urls import path

from . import views

urlpatterns = [
        path("", views.index, name ="index"),
        path("<int:todo_id>/", views.detail, name="detail"),
        path("create/", views.create, name="create"),
        path("created/", views.created, name="created"),
        path("remove/<int:todo_id>/", views.remove, name="remove"),
        path("edit/<int:todo_id>/", views.edit,name="edit"),
]

