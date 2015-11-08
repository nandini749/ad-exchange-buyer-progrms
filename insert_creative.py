
import argparse
import pprint
import sys

from oauth2client.client import AccessTokenRefreshError
import util

# Optional arguments; overrides default values if set.
parser = argparse.ArgumentParser(description='Inserts a new creative into the '
                                 'verification pipeline.')
parser.add_argument('-a', '--account_id', required=False, type=int,
                    help=('The integer id of the account you\'re using to '
                          'insert the creative.'))
parser.add_argument('-b', '--buyer_creative_id', required=False,
                    help=('The buyerCreativeId of the creative you want to '
                          'retrieve.'))
parser.add_argument('-s', '--html_snippet', required=False,
                    default='<h1>Hello, World!</h1>',
                    help=(''))
parser.add_argument('-c', '--click_through_url', required=False,
                    default='www.google.com',
                    help=(''))
parser.add_argument('-w', '--width', required=False, type=int, default=300,
                    help=(''))
parser.add_argument('-ht', '--height', required=False, type=int, default=250,
                    help=(''))
parser.add_argument('-n', '--advertiser_name', required=False, default='test',
                    help=(''))


def main(ad_exchange_buyer, body):
  # Construct the request.
  request = ad_exchange_buyer.creatives().insert(body=body)

  # Execute request and print response.
  pprint.pprint(request.execute())

if __name__ == '__main__':
  try:
    service = util.GetService()
    args = parser.parse_args()

    # Create a body containing the Creative's details.
    if args.account_id and args.buyer_creative_id:
      BODY = {
          'accountId': args.account_id,
          'buyerCreativeId': args.buyer_creative_id,
          'HTMLSnippet': args.html_snippet,
          'clickThroughUrl': [args.click_through_url],
          'width': args.width,
          'height': args.height,
          'advertiserName': args.advertiser_name
      }
    else:
      BODY = {
          'accountId': int('INSERT_ACCOUNT_ID'),
          'buyerCreativeId': 'BUYER_CREATIVE_ID',
          'HTMLSnippet': 'INSERT_HTML_SNIPPET',
          'clickThroughUrl': ['INSERT_URL'],
          'width': int('INSERT_WIDTH'),
          'height': int('INSERT_HEIGHT'),
          'advertiserName': 'INSERT_ADVERTISER_NAME'
      }

    if BODY['buyerCreativeId'] == 'BUYER_CREATIVE_ID':
      raise Exception('The buyerCreativeId was not set.')
    if BODY['HTMLSnippet'] == 'INSERT_HTML_SNIPPET':
      raise Exception('The HTMLSnippet was not set.')
    if BODY['clickThroughUrl'][0] == 'INSERT_URL':
      raise Exception('The clickThroughUrl was not set.')
    if BODY['advertiserName'] == 'INSERT_ADVERTISER_NAME':
      raise Exception('The advertiserName was not set.')
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
    print 'Did you set account_id, width and height to an integer?'
    sys.exit()

  main(service, BODY)
