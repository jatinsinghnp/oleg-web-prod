from django.urls import path
from .tokenurls import urlpatterns as tokenurls_patterns
from .register_urls import urlpatterns as registerurl_patterns
from ..urls.router_urls import urlpatterns as routerurls
from ..urls.swagger_urls import urlpatterns as swaggerpatterns

urlpatterns = (
    [] + tokenurls_patterns + registerurl_patterns + routerurls + swaggerpatterns
)
