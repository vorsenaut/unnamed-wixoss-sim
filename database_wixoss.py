#Database for Wixoss-Game

import xml.etree.ElementTree as ET

card_database_src = "01.Wixoss TCG.xml";

deck_src = "Diva Debut.xml";

class Database:


    def __init__(self):
            
            if card_database_src:

                self.database_xml = ET.parse(card_database_src);
            
                self.database_root = self.database_xml.getroot();
            
            if deck_src:

                self.deck_data = ET.parse(deck_src);

                self.deck_data_root = self.deck_data.getroot();

            
            else:
                 
                print("Deck or Database XML not found");
                
                print(f"DATA: {card_database_src} DECK: {deck_src}");


            

        
    


        

