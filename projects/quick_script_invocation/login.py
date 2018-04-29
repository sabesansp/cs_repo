import sys

from optparse import OptionParser


def parse_options():  
  # Error conditions are not handled here because the user of the script
  # does not envision sending less than 3 parameters or mismatching argument names.
  parser = OptionParser()
  parser.add_option("-i", "--ip", dest="ip",
                  help="ip address of host to connect to")
  parser.add_option("-u", "--user", dest="user",
                  help="user name for the host")
  parser.add_option("-p", "--password", dest="pwd",
                  help="password of host to connect to")
  (options, args) = parser.parse_args()
  return (options.ip, options.user, options.pwd)


if __name__ == '__main__':
  (ip, user, pwd) = parse_options()
  print "ip = %s" % ip
  print "user = %s" % user
  print "password = %s" % pwd
