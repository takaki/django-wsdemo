from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns (
	'',
    (r'^logo.png$', logo_png),
    (r'^ua_log$', ua_log),
    (r'^echo$', echo),
    (r'^echo_once$', echo_once),
    (r'^lower_case$', lower_case),
)
