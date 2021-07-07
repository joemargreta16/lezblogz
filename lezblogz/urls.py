from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "The Blog Admin"
admin.site.site_title = "The Blog"
admin.site.index_title = 'Welcome to "The Blog" Admin Panel'

urlpatterns = [
                  path( 'admin/', admin.site.urls ),
                  path( 'accounts/', include( 'allauth.urls' ) ),
                  path( '', include( 'pages.urls', namespace='pages' ) ),
                  path( '', include( 'blog.urls' ) ),
                  path( 'ckeditor/', include( 'ckeditor_uploader.urls' ) ),
              ] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) + static( settings.STATIC_URL,
                                                                                            document_root=settings.STATIC_ROOT )
