# Basic Captcha Bypass PoC

A basic captcha bypass proof-of-concept script.
<br>
<br>
<img src="https://raw.githubusercontent.com/NodePoint/Basic-Captcha-Bypass-PoC/master/demo.png" style="max-width:100%;" alt="Demo of PoC">

## About

Basic captcha bypass is a Python 3.x script that mainly focuses on basic captchas that utilises four character numeric codes (regex: ^[1-9][0-9]{3}$), assigns that value to a session cookie, does not invalidate (or change the code) after failure, and does not have bruteforce protection.
<br>
This would also work against captchas that has all of that being the case apart from utilising session cookies (backend storage [database, file]).

## Disclaimer

This is for educational purposes only. I am not responsible for misuse or damage caused by the program. Get mutual consent first if you plan on trying this against websites you do not own. 

## Prerequisites

- Python 3.x
- 'requests' Python module

## Setup

Open 'basic_captcha_bypass_poc.py' in a code editor and change the values assigned to the variables found under '# configuration'.

|  Config         | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| protocolinput   | Protocol to utilise (http/https)                             |
| hostinput       | Hostname of target                                           |
| captchapath     | Path to captcha script that sets up a new code               |
| registerpath    | Register / sign up submission script                         |
| usernameinput   | Username of the account to create                            |
| passwordinput   | Password of the account to create                            |
| emailinput      | Email of the account to create                               |
| newsletterinput | Newsletter toggle (account)                                  |
| sessionidname   | Session ID name (maybe different depending on configuration) |

This PoC was tested with one site of which required specific POST parameters, values, and HTTP responses. You will need to make a lot of changes request-wise to best suit the target.
