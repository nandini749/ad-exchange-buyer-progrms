
import pprint
import sys

from oauth2client.client import AccessTokenRefreshError
import util


def main(ad_exchange_buyer):
  # Construct the request.
  request = ad_exchange_buyer.accounts().list()

  # Execute request and print response.
  pprint.pprint(request.execute())

if __name__ == '__main__':
  try:
    service = util.GetService()
  except IOError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you specify the key file in util.py?'
    sys.exit()
  except AccessTokenRefreshError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you set the correct Service Account Email in util.py?'
    sys.exit()

  main(service)
