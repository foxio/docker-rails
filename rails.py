from waflib import Utils, Logs, Errors
from waflib.Configure import conf

def display_header (title):
    Logs.pprint ('BOLD', title)

def display_msg (conf, msg, status = None, color = None):
    color = 'CYAN'
    if type(status) == bool and status or status == "True":
        color = 'GREEN'
    elif type(status) == bool and not status or status == "False":
        color = 'YELLOW'
    Logs.pprint('BOLD', " *", sep='')
    Logs.pprint('NORMAL', "%s" % msg.ljust(conf.line_just - 3), sep='')
    Logs.pprint('BOLD', ":", sep='')
    Logs.pprint(color, status)
