import sae
from fyp import wsgi

application = sae.create_wsgi_app(wsgi.application)
