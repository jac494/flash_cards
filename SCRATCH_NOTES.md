# Notes for flash card study app

* want to be able to create flash cards with attributes:
  * front (side_a)
  * back (side_b)
  * tags = list of subjects that the card is related to

* want to be able to automatically assign cards to a "deck" based on tags
  * decks can be as general as one tag
  * decks can be an intersection of multiple tags (probably the default behavior) or union of multiple tags (likely _not_ the default)
  * decks can also be created manually
  * probably need a DB table that maps deck_id -> card_id

* want this to be available "anywhere" so likely a web app to get started
  * going to just use django

* anon users can view cards and decks and retrieve an "ephemeral" deck (where the deck only exists as a query and not concretely in a table as deck->cards) but cannot create or edit cards or decks
* authenticated users can create cards and decks, but maybe limit to 2000 cards and 20 decks or something like that
* 

