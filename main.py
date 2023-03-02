#!/usr/bin/env python3

from typing import Union


MENU_PROMPT = """
Pick an option: (a)dd a new card, (p)lay a session, (e)xit
"""


class FlashCard:
    def __init__(self, card_id: int, side_a: str, side_b: str, tags: List[str]) -> None:
        self.card_id = card_id
        self.side_a = side_a
        self.side_b = side_b
        self.visible_side = self.side_a

    def __str__(self) -> str:
        repr_str = "Side A:\n{}\nSide B:\n{}\nTags:\n{}"
        return repr_str.format(self.side_a, self.side_b, self.tags)


class CardDeck:
    def __init__(self):
        
        self.card_list = []
        self.current_card_index = 0
        self.cards_shown = set()

    def add_card(self, card):
        self.card_list.append(card)

    def is_empty(self):
        return self.card_list == []

    def get_random_card(self) -> FlashCard:
        picked_card = random.choice(self.card_list)
        while picked_card in self.cards_shown:
            picked_card = random.choice(self.card_list)
        self.cards_shown.add(picked_card)
        return picked_card

    def play_session(self):
        




def create_new_card() -> Union[None, FlashCard]:
    side_a = input("Side A text (one line, press ENTER to submit):\n")
    side_b = input("Side B text (one line, press ENTER to submit):\n")
    tags = input("Tags or categories (single words separated by spaces):\n").split()
    fc = FlashCard(side_a, side_b, tags)
    print(fc)
    print("Does this look correct? Press 's' to save or 'n' to delete and start over")
    save_choice = str(input()).lower()
    if save_choice == 's':
        return fc
    elif save_choice == 'n':
        return
    else:
        print("invalid choice: {}".format(save_choice))
        return


def invalid_option():
    print("Invalid choice")


def main():
    deck = CardDeck()
    options = {
        "a": create_new_card,
        "p": deck.play_session,
        "e": sys.exit
    }
    while True:
        if deck.is_empty()::
            print("There are no flash cards to view, add one to get started."
            new_card = create_new_card()
            if new_card is not None:
                deck.add_card(new_card)
        option = input(MENU_PROMPT)
        func = options.get(option, invalid_option)
        func()
                

