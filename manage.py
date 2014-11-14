# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
from django.conf import settings


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.simplelife.settings")
    sys.path.insert(0, settings.APPS_ROOT)
    sys.path.insert(0, settings.UTILS_ROOT)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)