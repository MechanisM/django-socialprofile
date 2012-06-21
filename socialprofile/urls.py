"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614

from django.conf.urls import *  #@UnusedWildImport
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from socialprofile.views import DeleteView

admin.autodiscover()

urlpatterns = patterns('',
    
    # Select Sign Up Method
    url(r'^select/$', 'socialprofile.views.select_view', name="sp_select_page"),

    # Profile
    url(r'^profile/$', 'socialprofile.views.profile_view', name="sp_profile_page"),

    # Delete Confirm Modal
    url(r'^delete/$', DeleteView.as_view(), name="sp_delete_page"),

    # Delete
    url(r'^delete/action$', 'socialprofile.views.delete_action_view', name="sp_delete_action_page"),

    # Social Registration
    url(r'', include('social_auth.urls')),
    
    # Logout Page
    url(r'^logout/$', 'socialprofile.views.logout_view', name="sp_logout_page"),
      
)