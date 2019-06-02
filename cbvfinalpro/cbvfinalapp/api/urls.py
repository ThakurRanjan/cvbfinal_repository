from django.conf.urls import url,include
from cbvfinalapp.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('berr',views.BeerSerializerView)

urlpatterns =[
    url('',include(router.urls)),
]