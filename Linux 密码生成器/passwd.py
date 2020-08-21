#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''shadow 密码生成工具

以下脚本可以生成 /etc/shadow 中使用的密码。
'''

import crypt
import logging
import sys

from uuid import uuid4
from random import randint

logger = logging.getLogger()

size = randint(8, 12)
salt = uuid4().hex[:size]
pwd = ''
if len(sys.argv) > 1:
    pwd = sys.argv[1]
pwd = crypt.crypt(pwd, '$6$%s' % salt)
sys.stdout.write('%s\n' % pwd)
