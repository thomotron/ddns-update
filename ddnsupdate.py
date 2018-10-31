#!/usr/bin/python3

import requests
from argparse import ArgumentParser
from configparser import ConfigParser

parser = ArgumentParser()
parser.add_argument('-c', '--config', help='path to the config file', default='config.ini')
args = parser.parse_args()

config = ConfigParser()
config.read(args.config)

if not config.sections():
    print('No existing config was found')
    print('Copy the following blank template into ' + args.config + ' and fill in the blanks:')
    print('[Credentials]\n' + \
          'host = \n' + \
          'domain = \n' + \
          'password = ')
    exit(1)

if not 'Credentials' in config:
    print('Failed to read config: \'Credentials\' section missing')
    exit(1)

if not 'host' in config['Credentials']:
    print('Failed to read config: \'host\' missing')
    exit(1)

if not 'domain' in config['Credentials']:
    print('Failed to read config: \'domain\' missing')
    exit(1)

if not 'password' in config['Credentials']:
    print('Failed to read config: \'password\' missing')
    exit(1)

host = config['Credentials']['host']
domain = config['Credentials']['domain']
password = config['Credentials']['password']

p = {
    "host": host,
    "domain": domain,
    "password": password,
    "ip": "" # Leave blank to use current IP
}

r = requests.get("https://dynamicdns.park-your-domain.com/update", params=p)
print(r.status_code)
