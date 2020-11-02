
import os, sys
path = '/home/EgorKarelin/bot/ioi/autoraz/autoraz'
if path not in sys.path:
    sys.path.append(path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autoraz.settings')

application = get_wsgi_application()
