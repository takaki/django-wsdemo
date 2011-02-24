# Create your views here.

from django_websocket import require_websocket

import logging

logger = logging.getLogger(__name__)

#LOGFILE_FORMAT = "[%(asctime)s %(process)d] %(levelname)s " +
#"(%(funcName)s: %(module)s:%(lineno)d) %(message)s"

LOGFILE_FORMAT  = '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(
    level=logging.DEBUG,
    format=LOGFILE_FORMAT,
    datefmt=DATE_FORMAT
    )
logger.debug('debug!!')

@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    request.websocket.send(message)

from django.http import HttpResponse
from django_websocket import accept_websocket
import Queue

m_queue = Queue.Queue()

@require_websocket
def echo(request):
    while True:
        # wait() will return new messages as they arrive
        message = request.websocket.wait()
        # wait() returns None if the connection was closed by the client
        if message is None:
            return
        # simple method for sending messages
        request.websocket.send(message)

import time

def logo_png(request):
    import datetime
    logger.debug("pre put()")
    m_queue.put(str(datetime.datetime.now()))
    logger.debug("post put()")
    return HttpResponse(file('wstest/logo.png').read(), mimetype="image/png")

@require_websocket
def echo_time(request):
    count = 0
    while True:
        message = request.websocket.wait()
        if message is None:
            return
        while True:	
            try:
                logger.debug("pre get_nowait()")
                request.websocket.send('{0}\n'.format(m_queue.get_nowait()))
                logger.debug("post get_nowait()")
            except Queue.Empty:
                logger.debug("except")
                time.sleep(1.0)
            # count += 1
            # request.websocket.send('{0}\n'.format(count))
            # time.sleep(1.0)	
            

def modify_message(message):
    return message.lower()

@accept_websocket
def lower_case(request):
    time.sleep(0)	
    if not request.is_websocket():
        message = request.GET['message']
        message = modify_message(message)
        return HttpResponse(message)
    else:
        for message in request.websocket:
            message = modify_message(message)
            request.websocket.send(message)
