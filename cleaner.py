#!/usr/bin/python3

# Copyright (c) 2012 Andrey Zhidenkov, <andrey.zhidenkov@gmail.com>
# POP3 mail cleaner

import sys
import getpass, poplib

def main(argv):

  black_list = [ b'list.avia.ru', b'dotnews.ru', b'info@molotok.ru', b'subscribe.ru' ]

  m = poplib.POP3('pop.yandex.ru')
  m.user('user')
  m.pass_('password')
  numMessages = len(m.list()[1])
  TotalCount = 0
  print('Logged in OK. Total messages in mailbox: {c}'.format(c = numMessages))
  for i in range(numMessages):
    try:
      t = m.top(i+1, 10)
    except poplib.error_proto as err:
      print('Cannot retrieve message {m}'.format(m = i+1))
    for j in t[1]:
      if j.startswith(b'From:'):
        for black_item in black_list:
          if black_item in j:
            print('Message {m} will be deleted (from {f})'.format(m = i+1, f = j))
            m.dele(i+1)
            TotalCount += 1
  m.quit()
  print('All done. Total messages deleted: {c}'.format(c = TotalCount))
  return
  
if __name__ == "__main__":
  sys.exit(main(sys.argv))
