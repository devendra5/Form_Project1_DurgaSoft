"""Form_Project1_DurgaSoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path
from django.contrib import admin
from django.urls import path
from TestApp import views
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Register/',views.Studentregisteration_view),

]





"""
This Project flow wise :
-----------------------
1.create project and App
2.create template directories and static directories  into the project level
3. go to settings.py and add the APP name to Installed_Apps
4.Go to BASIC_dIR and in the bellow add to the STATIC_DIR,TEMPLATE_DIR
5.go to settings.py and add the bellow item  # STATICFILES_DIRS = [ STATIC_DIR,]
6.In the APP level take one python file name as a #forms.py
7.go to views.py and create form object to views.py level and rendering Html file and at time to pass the form object 
8. go to tempate file like register.html and to add the the bellow item
# {{form.as_p}}
9. go to template folder and open html file and add to {%csrf_token}



"""