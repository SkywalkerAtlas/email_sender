#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

class Email_sender(object):
	
	def __init__(self, from_addr, password, to_addr, smtp_server):
		self.__from_addr = from_addr
		self.__password = password
		self.__to_addr = to_addr
		self.__smtp_server = smtp_server

	def __str__(self):
		return 'Email_sender objects, from: %s' % self.__from_addr
	
	def set_msg(self, msg):
		self.msg = MIMEText(msg, 'plain', 'utf-8')
		self.msg['From'] = _format_addr('test <%s>' % self.__from_addr)
		self.msg['To'] = _format_addr('skywalkeratlas <%s>' % self.__to_addr)
		self.msg['Subject'] = Header('love, dva……', 'utf-8').encode()
	
	def send(self):
		server = smtplib.SMTP(self.__smtp_server, 25)
		server.set_debuglevel(1)
		server.login(self.__from_addr, self.__password)
		server.sendmail(self.__from_addr, [self.__to_addr], self.msg.as_string())
		server.quit()

