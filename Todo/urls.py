from django.urls import path


from Todo.views import (apiOverview, task_list, taskDetail,
 taskCreate, taskUpdate, taskDelete)



urlpatterns = [
    path('', apiOverview , name='home'),
    path('task_list/', task_list , name='task_list'),
    path('taskCreate/', taskCreate, name='taskcreate'),

    path('taskDetail/<str:pk>', taskDetail , name='taskDetail'),
    path('taskUpdate/<str:pk>', taskUpdate , name='taskUpdate'),
    path('taskDelete/<str:pk>', taskDelete , name='taskDelete')




]