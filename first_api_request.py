#!/usr/bin/python


"""Sample application that authenticates and makes an API request."""

import pprint
from apiclient.discovery import build
import httplib2
from oauth2client import client
# Developers Console.
SERVICE_ACCOUNT_EMAIL = 'rare-basis-686@appspot.gserviceaccount.com'
KEY_FILE = 'path_to_key'

# Ad Exchange Buyer REST API authorization scope.
SCOPE = 'https://www.googleapis.com/auth/adexchange.buyer'
VERSION = 'v1.4'  # Version of Ad Exchange Buyer REST API to use.


def main():
  # Create credentials using the Service email and P12 file.
  oauth_credentials = client.SignedJwtAssertionCredentials(
      SERVICE_ACCOUNT_EMAIL,
      open(KEY_FILE).read(),
      scope=SCOPE)

  # Use the credentials to authorize an Http object
  http = oauth_credentials.authorize(httplib2.Http())

  # Use the http object to create a client for the API service.
  buyer_service = build('adexchangebuyer', VERSION, http=http)

  # Call the Accounts resource on the service to retrieve a list of
  # Accounts for the service account.
  request = buyer_service.accounts().list()

  pprint.pprint(request.execute())

if __name__ == '__main__':
  main()
