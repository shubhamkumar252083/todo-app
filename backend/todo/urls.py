from django.urls import path, include
from rest_framework import routers
from .views import TodoView

app_name = 'todo'
router = routers.DefaultRouter()
router.register(r'todos', TodoView, 'todo')


urlpatterns = [
    path('', include(router.urls)),
]


# Note :-
'''
This code specifies the URL path for the API. This was the final step that completes the building of the API.

You can now perform CRUD operations on the Todo model. The router class allows you to make the following queries:

1.  /todos/ - returns a list of all the Todo items. CREATE and READ operations can be performed here.


2.  /todos/id - returns a single Todo item using the id primary key. UPDATE and DELETE operations can be performed here.
'''
