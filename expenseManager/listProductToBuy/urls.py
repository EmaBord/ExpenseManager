from django.conf.urls import patterns, url
from listProductToBuy.views import *
urlpatterns = patterns ('expenseManager.listProductToBuy.views',
			 url(r'productToBuy/add/$', ProductToBuyCreate.as_view(), name='ProductToBuy-add'),
			 url(r'ProductToBuy/(?P<pk>[0-9]+)/$', ProductToBuyUpdate.as_view(), name='ProductToBuy-update'),
    		 url(r'productToBuy/(?P<pk>[0-9]+)/delete/$', ProductToBuyDelete.as_view(),  name='ProductToBuy-delete'),
			 url(r'productToBuy/$', ProductToBuyListView.as_view(), name='ProductToBuy-list'),
			 
			)
