class RawStash:

    __slots__ = [
        '_id',
        '_public',
        '_account_name',
        '_last_character_name',
        '_stash_name',
        '_stash_type',
        '_league',
        '_items'
    ]

    def __init__(self, raw_stash_data):
        self._id = raw_stash_data.get('id')
        self._public = raw_stash_data.get('public')
        self._account_name = raw_stash_data.get('accountName')
        self._last_character_name = raw_stash_data.get('lastCharacterName')
        self._stash_name = raw_stash_data.get('stash')
        self._stash_type = raw_stash_data.get('stashType')
        self._league = raw_stash_data.get('league')
        self._items = raw_stash_data.get('items')

    @property
    def id(self): return self._id

    @property
    def is_public(self): return self._public

    @property
    def account_name(self): return self._account_name

    @property
    def last_character_name(self): return self._last_character_name

    @property
    def name(self): return self._stash_name

    @property
    def type(self): return self._stash_type

    @property
    def league(self): return self._league

    @property
    def raw_items(self): return self._items
