#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#
# channel_notty_analysis_disable_3 time=1329926319.305358 uristring=NMOD_3.08 uristring=3331882995%3Asg1.nersc.gov%3A22 count=1593597883 count=2 int=633 int=392

#
import urllib
import syslog
import time
import socket

valset = []


parola = []

#t = "channel_data_server_3 time=1405327835.751387 uristring=NMOD_3.10 uristring=8323328%3Alocalhost.localdomain%3A22 count=945287269 count=0 uristring=%0Abin%2F+++++++++etc%2F+++++++++lib64%2F+++++++mnt%2F+++++++++root%2F++++++++srv%2F+++++++++tmp%2F+++++++++"

def analizza(t):
    error_line = 0   # the event line does not contain at least two entries
    error_item = 0   # number of '=' in the type=data < 1
    error_parse = 0  # data parse errors per window
    item_count = 0
    pezzi = t.split(" ")
    for item in pezzi:
        element = item.split("=")
        if len(element) == 2:
            type = element[0]
            #if type == "bool":
             #   if element[1] == "T" or element[1] == "F":
              #      val = element[1]
               # else:
                #    print "parse bool:",element[1]
                 #   error_parse = error_parse + 1
                  #  continue
           # elif type == "count":
             #   element[1] = databrush(type,element[1])

             #   if element[1].isdigit():
                    #val = broccoli.count(element[1])
             #   else:
             #       error_parse = error_parse + 1
              #      print "               parse count:",element[1], " ", event
              #      continue
            #elif type == "time":
            #    try:
            #        tval = float(element[1])
             #   except ValueError, TypeError:
             #       error_parse = error_parse + 1
             #       print "               parse time:",element[1]
             #       continue
             #   else:
                   # val = broccoli.time(element[1])
           # elif type == "interval":
                #val = broccoli.interval(element[1])
            #elif type == "double":
             #   try: 
              #      val = float(element[1])
               # except ValueError, TypeError:
                #    print "               parse double:",element[1]
                 #   error_parse = error_parse + 1
                  #  continue
            #elif type == "string":
             #   val = element[1]
            if type == "uristring":
                val = urllib.unquote_plus( str(element[1]) )
                #print val
                if "#" in val:
                    print str(val)
            #elif type == "port":
             #   if element[1].find('/tcp') == -1:
             #       element[1] = element[1] + '/tcp'
              #  if is_valid_port(element[1]):
               #     val = broccoli.port(element[1])
                #else:
                 #   error_parse = error_parse + 1
                  #  print "               parse port:",element[1]
                   # continue
            #elif type == "addr":
             #   element[1] = databrush(type,element[1])

              #  if is_valid_ipv4_address(element[1]):
             #       val = broccoli.addr(element[1])
              #  else:
             #       error_parse = error_parse + 1
              #      print "               parse addr:",element[1]
              #      continue
            #elif type == "subnet":
              #  val = broccoli.subnet(element[1])
            #elif type == "int":
             #   try:
              #      val = int(element[1])
               # except ValueError:
                #    error_parse = error_parse + 1
                 #   print "               parse int:",element[1]
                  #  continue
            #else:
                #print "unknown type: ", type
                 #error_parse = error_parse + 1
                #print "parse unknown:",element[0],element[1]
                 #continue
                 
f = open('/Users/isztld/Desktop/isshd/ssl_log/ssllogmux.log')
for line in iter(f):
    analizza(line)
f.close()
