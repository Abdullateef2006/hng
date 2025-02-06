from django.urls import path
from  .views import *
urlpatterns = [
        path("api/classify-number/", Classify_Api.as_view() , name="classify-number"),

]