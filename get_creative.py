#!/usr/bin/python


"""This example demonstrates how to retrieve a Creative.

Tags: Creatives.get
"""
import argparse
import pprint
import sys

from oauth2client.client import AccessTokenRefreshError
import util

parser = argparse.ArgumentParser(description='Gets the status for a single '
                                 'creative.')
parser.add_argument('-a', '--account_id', required=False, type=int,
                    help=('The integer id of the account you\'re retrieving '
                          'the creative from.'))
parser.add_argument('-b', '--buyer_creative_id', required=False,
                    help=('The buyerCreativeId of the creative you want to '
                          'retrieve.'))


def main(ad_exchange_buyer, account_id, buyer_creative_id):
  # Construct the request.
  request = ad_exchange_buyer.creatives().get(
      accountId=account_id,
      buyerCreativeId=buyer_creative_id)

  # Execute request and print response.
  pprint.pprint(request.execute())

if __name__ == '__main__':
  try:
    service = util.GetService()
    args = parser.parse_args()

    if args.account_id and args.buyer_creative_id:
      ACCOUNT_ID = args.account_id
      BUYER_CREATIVE_ID = args.buyer_creative_id
    else:
      ACCOUNT_ID = int('INSERT_ACCOUNT_ID')
      BUYER_CREATIVE_ID = 'INSERT_BUYER_CREATIVE_ID'

    if BUYER_CREATIVE_ID == 'INSERT_BUYER_CREATIVE_ID':
      raise Exception('buyer_creative_id not set.')
  except IOError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you specify the key file in util.py?'
    sys.exit()
  except AccessTokenRefreshError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you set the correct Service Account Email in util.py?'
    sys.exit()
  except ValueError, ex:
    print 'Unable to create adexchangebuyer service - %s' % ex
    print 'Did you set account_id to an integer?'
    sys.exit()

  main(service, ACCOUNT_ID, BUYER_CREATIVE_ID)
