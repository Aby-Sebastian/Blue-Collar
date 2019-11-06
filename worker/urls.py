from django.urls import path
from . import views
urlpatterns=[
	path('abc/',views.home,name='abc'),
	path('login',views.login,name='login'),
	path('workerreg/',views.workerreg,name='workerreg'),
	path('cusreg/',views.cusreg,name='cusreg'),
	path('trial/',views.trial,name='trial'),
	path('new/',views.new,name='new'),
	path('aa/',views.aa,name='aa'),
	path('l/',views.l,name='l'),
	path('reg/',views.reg,name='reg'),
	path('addskill/',views.addskill,name='addskill'),
	path('',views.home,name='home'),
	]