import requests
from poemarketdb.backend.exceptions import POEAPIException

from poemarketdb.backend.database import DBHandler

# TODO: Completely clean this up, currently just for testing.
# TODO: Code here is scratch file code, just here for git control right now.

request = requests.get('http://api.pathofexile.com/public-stash-tabs')

if request.status_code != 200:
    raise POEAPIException(
        'Failed to get stash data from POE Stash API, '
        'Error Code: {} - Reason: {}"'.format(
            request.status_code,
            request.reason
        )
    )
data = request.json()

database_handler = DBHandler()
database_handler.initialize_tables()
database_handler._add_stashes(data)
database_handler.find_stash(account_name='Kricys', league='Standard')
database_handler.close_connection()