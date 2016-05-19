from django.conf.urls import url, include
from django.contrib import admin

from esp_web_app.views import LedStatus

urlpatterns = [
    url(r'^led_app/$', LedStatus.as_view()),]
