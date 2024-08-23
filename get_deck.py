from database_wixoss import Database;

d = Database();

#card_database_src = "01.Wixoss TCG.xml";

#deck_src = d.deck_data;

class Deck:

    def __init__(self):

        # Deck can be a dictionary, but cards need alternate naming
        # because dicts cannot have more than 1 identical key.

        self.deck = {};

        self.name = "";
        
        self.number = 0;
    
        self.counter = 0;

    def get_cards(self):

        print("Entering cards METHOD");

        for card in d.deck_data_root.findall(".//card"):

            print("Processing cards.")

            print(card.get('name'));
        
            self.name = card.get('name') if card.get('name') is not\
            None else 'Unknown';
        
            self.number = int(card.get('number')) if int(card.get('number')) is not\
            None else "Unknown"
        
            for i in range(self.number):

                self.deck[f"{self.name} {i}"] = self.name;

        print("Exiting cards METHOD")

        print(self.deck)

deck = Deck();
print("Created Deck instance")

deck.get_cards();
print("Finished script")









