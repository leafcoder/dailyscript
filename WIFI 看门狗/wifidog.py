# -*- coding: utf-8 -*-
# @Author: zhanglei3
# @Date:   2020-08-19 10:26:46
# @Last Modified by:   zhanglei3
# @Last Modified time: 2020-08-19 10:47:22

"""WIFI 看门狗"""

import os
import time
import logging
from datetime import datetime

logger = logging.getLogger()

max_retries = 10
retry_times = 0
while True:
    d = os.system('ping -c 1 163.com')
    if d != 0:
        if retry_times > max_retries:
            os.system('sudo systemctl restart network-manager')
            logger.info('[%s] WIFI has restarted.', datetime.now())
            retry_times = 0
        else:
            retry_times += 1
            logger.info(
                '[%s] WIFI has disconnected. Retring %d.',
                datetime.now(), retry_times)
    else:
        retry_times = 0
        logger.info('[%s] WIFI is connecting.', datetime.now())
    time.sleep(1)
