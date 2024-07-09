import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
    django.setup()
