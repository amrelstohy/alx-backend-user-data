#!/usr/bin/env python3
"""Regex-ing"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str
                 ) -> str:
    """0. Regex-ing"""
    for field in fields:
        message = re.sub(fr'{field}=.*?(?={separator}|$)',
                         f'{field}={redaction}', message)
    return message
