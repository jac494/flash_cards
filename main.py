#!/usr/bin/env python3

import sqlite

from typing import List


LOCAL_DB_NAME = "flash_cards.sqlite3.db"


class FlashCard:
    def __init__(self, card_id: int, side_a: str , side_b: str, tags: List[str]):
        self.side_a = side_a
        self.side_b = side_b
        self.tags = tags


class FlashCardsDB:
    _local_db = LOCAL_DB_NAME

    def __init__(self, db_name: str) -> None:
        # if db file does not exist,
        # create the db file and initial tables needed
        # and set the connection
        # otherwise just connect to the db
        self.conn = sqlite3.connect(db_name or self._local_db)
        self._init_tables()

    def _init_tables(self):
        cursor = self.conn.cursor()

    def commit_flash_card(card: FlashCard) -> Bool:
        cursor
