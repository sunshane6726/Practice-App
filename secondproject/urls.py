
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import blog.views
import portfolio.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name = 'home'),
    path('blog/', include('blog.urls')),  
    path('portfolio/', include('portfolio.urls')),  
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, docunment_root = settings.MEDIA_ROOT)
