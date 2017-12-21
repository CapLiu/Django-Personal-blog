#!/usr/bin/python3.5
"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath
import sys
sys.path.append('/home/liu/.local/lib/python3.5/site-packages')
#sys.path.append('/home/liu/djangotest/myblog')
from django.core.wsgi import get_wsgi_application
#PROJECT_DIR = dirname(dirname(abspath(__file__)))
#sys.path.insert(0,PROJECT_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

application = get_wsgi_application()
