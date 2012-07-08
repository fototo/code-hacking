#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/kiennt/hackerrank-bot/blob/master/hackerrank.py

import shelve
import requests
from config import *
from ch2 import guess, conv2numeric, solveCypher, caesar


# constant for API ENDPOINT
LOGIN_ENDPOINT = "https://www.hackerrank.com/users/sign_in.json"
SUBMIT_ENDPOINT = "https://www.hackerrank.com/game.json"
# SIGNOUT_ENDPOIT = "https://www.hackerrank.com/users/sign_out?remote=true&commit=Sign+out&utf8=%E2%9C%93"
USERSTATS_ENDPOINT = "https://www.hackerrank.com/splash/userstats.json"
# LEADERBOARD_ENDPOINT = "https://www.hackerrank.com/splash/leaderboard.json"
# CHALLENGE_ENDPOINT = "https://www.hackerrank.com/splash/challenge.json"


safeSounds = ['phobia', 'graph', 'phy', 'psy',
              'ism', 'phi', 'ous', 'ist', 'gy',
              'ess', 'ion', 'ence', 'ive',
              'sis', 'ics', 'cy', 'ope', 'nia',
              'rian', 'ize', 'box', 'ate',
              'ty', 'ter', 'ette', 'tic',
              'the', 'ver', 'dont', 'ough',
              'ic', 'dle', 'for']



class HackerRankAPI(object):

    def __init__(self, username, password, dbName=None):
        self.username = username
        self.password = password
        self.dbName = dbName

        self.headers = {
            "Accept": "*/*",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-us,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://www.hackerrank.com",
            "Referer": "http://www.hackerrank.com/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11",
            "X-Requested-With": "XMLHttpRequest",
        }

        self.s = requests.session(headers=self.headers)

        self.login()

    def post(self, endpoint, data={}):
        return self.s.post(endpoint, data=data)

    def get(self, endpoint):
        return self.s.get(endpoint)

    def put(self, endpoint, data={}):
        return self.s.put(endpoint, data=data)

    def login(self):
        payload = {
            'commit': 'Sign in',
            'remote': 'true',
            'user[login]': self.username,
            'user[password]': self.password,
            'user[remember_me]': '1'
        }
        r = self.post(LOGIN_ENDPOINT, data=payload)
        if 'email' in r.json.keys():
            return True
        else:
            raise Exception('Login failed!')

    def userstats(self):
        return self.get(USERSTATS_ENDPOINT).json


    def submitChallenge(self, answer, ids):
        payload = {'answer': answer,
                   'id': ids,
                   'remote': 'true'}
        r = self.put(SUBMIT_ENDPOINT, data=payload)
        value = r.json
        return value

    def getChallenge(self, n):
        db = shelve.open(self.dbName, writeback=True)

        if str(n) in db.keys():
            value = db[str(n)]
        else:
            endpoint = 'https://www.hackerrank.com/game.json'
            payload = {'n': n,
                       'remote': 'true'}
            r = self.post(endpoint, data=payload)
            value = r.json
            db[str(n)] = value
        db.close()
        return value

    def saveChallenge(self, n):
        print n


def main():

    maxChallenge = 11100
    hr = HackerRankAPI(username, password, 'c2.s')

    try:

        db = shelve.open('c2success.s')

        # for i in range(6370, 6380):
        for i in range(9999, maxChallenge + 1):

            if str(i) in db.keys() or i in [10600]:
                # print 'Skipping', i
                continue
            else:
                r = hr.getChallenge(i)

                # print i
                # print '===' * 20
                # print r['game']

                if 'cph_number' in r['game'].keys():
                    toDecode = r['game']['cph_number']
                    text = guess(toDecode)
                    c2n = True

                elif 'cph_question'  in r['game'].keys():

                    c2n = False

                    question = r['game']['cph_question']
                    answer = r['game']['sample_cph_answer']

                    question = question.replace("Decipher '", '')
                    question = question.replace("'.", '')

                    if i>10000:
                        poss = [cc for cc in map(lambda n: caesar(question.lower(), n), range(1, 27)) if len(filter(lambda t: t in cc, safeSounds)) > 0]
                        top = zip(range(len(poss)), poss)

                        if len(poss) == 0:
                            continue

                        else:
                            print '====' * 20
                            for tp in top:
                                print '%s - %s' % (tp[0], tp[1])

                            repl = raw_input()
                            if repl == 'n':
                                continue

                            else:
                                text = poss[int(repl)].capitalize()

                    else:

                        text = solveCypher(answer, question)
                        if text != False:
                            text = text.strip()
                            safe = len(filter(lambda s: s in text, safeSounds))
                            if safe == 0:
                                print 'skipping', text
                                # if raw_input('%s ?' % text) == 'n':
                                    # text = False
                                continue

                if text != False:

                    ids = r['game']['id']
                    if c2n == True:
                        answer = conv2numeric(text)
                    else:
                        answer = text

                    sc = hr.submitChallenge(answer, ids)

                    if sc != None:
                        if sc['ok'] == True and 'Congrats' in sc['message']:
                            print i, sc['message'].replace("`Congrats! That was correct`. ", '')
                            db[str(i)] = True
                        else:
                            print 'error on num', i
                            print text, sc
                            raise Exception('Error 01')
                    else:
                        db[str(i)] = True
                else:
                    print 'Could not decode', i
    finally:
        db.close()



if __name__ == '__main__':
    main()
