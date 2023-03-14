#!/usr/bin/python3
"""function to import"""
import datetime


def time_form(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')


def type_conv(arg):
    try:
        if arg.isdigit():
            return int(arg)
        elif float(arg):
            return float(arg)
    except ValueError:
        return arg
