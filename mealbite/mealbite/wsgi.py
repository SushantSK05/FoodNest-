"""
WSGI config for mealbite project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

# Add mealbite directory to Python path for Vercel serverless function
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mealbite.settings")

application = get_wsgi_application()
app = application
