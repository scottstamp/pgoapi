#!/usr/bin/python
# -*- coding: utf-8 -*-

"""accept-tos.py: Example script to accept in-game Terms of Service"""

from pgoapi import PGoApi
from pgoapi.utilities import f2i
from pgoapi import utilities as util
from pgoapi.exceptions import AuthException
import pprint
import time
import threading

def worker(num):
	api = PGoApi()
	api.set_position(40.7127837, -74.005941, 0.0)
	api.login('ptc', 'usernameprefix{}'.format(num), 'password')
	time.sleep(12)
	req = api.create_request()
	req.mark_tutorial_complete(tutorials_completed = 0, send_marketing_emails = False, send_push_notifications = False)
	response = req.call()
	print('Verified usernameprefix{}'.format(num))
	#print('Response dictionary: \r\n{}'.format(pprint.PrettyPrinter(indent=4).pformat(response)))

threads = []
for i in range(50):
	t = threading.Thread(target=worker, args=(i+1000,))
	threads.append(t)
	t.start()