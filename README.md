# Getting Started

## Prereqs

* Python 3.7 with pip
* `brew` and `brew cask`

## Setup

1. Start a `virtualenv` or `venv` with Python 3.7 (or install it in your global env, you do you)
1. `pip install -r requirements.txt`
1. `brew cask install ngrok`

## Running

In this directory, open two terminal windows then in one

```
ngrok http 5000
```

And in the other

```
python compliment.py
```

Copy and paste the forwarding URL from ngrok (this changes every time you start it) and add the `/sms` endpoint
(e.g. `https://fbf4668c.ngrok.io/sms`)

Receive your compliment!
