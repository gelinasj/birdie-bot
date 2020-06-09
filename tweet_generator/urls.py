from django.contrib import admin
from django.urls import path
from tweet_generator.api import PostTweet

urlpatterns = [
    path('tweet/', PostTweet.as_view()),
    path('admin/', admin.site.urls)
]
