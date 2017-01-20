#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import email_sender

from_addr = 'xxx@xxx'
password = 'xxx'
to_addr = 'xxx@xxx'
stmp_server = 'xxx'


sender = email_sender.Email_sender(from_addr, password, to_addr, stmp_server)

msg = 'this is a test'

sender.set_msg(msg)
sender.send()
