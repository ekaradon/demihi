from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	# Examples:
	# url(r'^$', 'demihi.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^autocomplete/', include('autocomplete_light.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('blog.urls', namespace="blog")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
