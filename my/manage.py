#!/usr/bin/env python
import os
import sys
import ios

if __name1__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
