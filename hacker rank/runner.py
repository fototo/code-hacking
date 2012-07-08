import shelve
from ch2 import *

maxChallenge = 11100

safeSounds = ['phobia', 'graph', 'phy', 'psy',
              'ism', 'phi', 'ous', 'ist',# 'gy',
              'ess', 'ion', 'ence', 'ive',
              'sis', 'ics', 'cy', 'ope', 'nia',
              'rian', 'ize', 'box', 'ate',
              'ty', 'ter', 'ette', 'tic',
              'the', 'ver', 'dont', 'ough',
              'ic', 'dle', 'for']

try:
    db = shelve.open('c2.s')
    db2 = shelve.open('c2success.s')

    for i in range(1, maxChallenge + 1):
        if str(i) not in db2.keys():
            print i, db[str(i)]['game']

finally:
    db.close()
    db2.close()
