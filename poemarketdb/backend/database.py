import sqlite3

from poemarketdb.backend.raw_stash import RawStash
from poemarketdb.backend.settings import DATABASE_PATH


# TODO: Implement items table.
# TODO: Implement players table.
# TODO: Implement primary keys for tables.
# TODO: Add logging with rotating file handler.
class DBHandler:
    """
    Handler class for all interactions with the database.

    Database currently contains the following tables:

    * Players
    * Stashes
    * Items

    One Player to many Stashes. <- not yet linked
    One Stash to many Items. <- not yet linked
    """

    def __init__(self):
        self._tables = ['players', 'stashes', 'items']
        self._connection = sqlite3.connect(DATABASE_PATH)

    @property
    def tables(self):
        return self._tables

    # TODO: Reminder! Implement players and items tables.
    # TODO: Look into use of a file as schema, not sure yet though.
    def initialize_tables(self):
        cursor = self._connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS stashes (
                stash_id text,
                stash_name text,
                account_name text,
                league text
            )
            """
        )
        self._connection.commit()

    # TODO: Not sure if more work needed on this to involve primary key etc.
    def _add_stashes(self, request_json):
        """
        Adds all stashes returned from the query to the POE API into
        the stashes table in the DB and commits changes.

        Args:
            request_json (dict): raw JSON data from the query.
        """
        cursor = self._connection.cursor()
        for stash_data in request_json.get('stashes'):
            stash = RawStash(stash_data)
            if stash.is_public:
                cursor.execute(
                    """
                    INSERT INTO stashes VALUES (
                        :stash_id, 
                        :stash_name, 
                        :account_name, 
                        :league
                        )
                    """,
                    {
                        'stash_id': stash.id,
                        'stash_name': stash.name,
                        'account_name': stash.account_name,
                        'league': stash.league or 'Harvest'
                    }
                )
        self._connection.commit()

    # TODO: Add find one method.
    # TODO: Move away from kwargs and use explicit keywords.
    # TODO: Return list of not-yet-implemented Stash objects.
    # TODO: Add more flexible filtering rather than just WHERE.
    # TODO: Add fields argument which describes fields to return.
    def find_stash(self, **kwargs):
        """
        Returns a list of raw stash data from the database which matches
        the values passed.

        Args:
            **kwargs: packed kwargs, key must be name of field on stash
                             table and value must match datatype on field.

        Returns:
            result (list): list of dictionaries which contain raw stash data.
        """
        cursor = self._connection.cursor()
        filter_string = ' AND '.join(
            '{0}=:{0}'.format(k) for k in kwargs.keys()
        )
        cursor.execute(
            """SELECT * FROM stashes WHERE {}""".format(filter_string), kwargs
        )
        result = cursor.fetchall()
        print(result)

    def close_connection(self):
        self._connection.close()
