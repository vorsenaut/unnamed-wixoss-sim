#WIXOSS Card simulator ACV 08/15/24


import xml.etree.ElementTree as ET
import random
from random import randint

import pygame
import requests
from io import BytesIO



pygame.init();


screen_width = 500;
screen_height = 500;

screen = pygame.display.set_mode([screen_width, screen_height]);


#pygame.display.init();



class DeckManager:

	def __init__(self, new_deck):

		self.new_deck = new_deck;

	def shuffle(self, deck):

		keys = list(deck.keys());

		random.shuffle(keys);

		shuffled = {key: deck[key] for key in keys};

		w.system_message("Deck has been shuffled!");

		return shuffled;

class Card:

	def __init__(self, name, url):


		self.url = url;
		response = requests.get(self.url);
		image_data = BytesIO(response.content);

		self.name = name;
		self.image = pygame.image.load(image_data);
		self.rect = self.image.get_rect();
		self.is_dragging = False;

		self.resized = pygame.transform.scale(self.image, (250, 350));

	def draw(self, surface):

		#print(image)

		surface.blit(self.resized, self.rect);

	def update_pos(self, pos):

		self.rect.topleft = pos;

class WixossGame:

	def __init__(self):

		self.hand = {};
		self.deck = {};


		self.field_lrig = {};
		self.field_signi = {};
		self.check_zone = {};


		self.lrigdeck = {};
		self.signi_count = 0;
		self.ener = 0;

		# start with 0, each player puts 7 cards from the top of deck to life cloth zone
		self.lifecloth = {};

		self.limit = 0;

		self.state = "UP";
		self.colours = ['R', 'G', 'B', 'W', 'U'];

		self.first = False;



		# Phase Structure
		self.phases  = {

			"SETUP": False,

			"UP": False,

			"DRAW": False,

			"ENER": False,

			"GROW": False,

			"MAIN": False,

			"ATTACK": False,

			"END": False

		}

		# set the current phase when it initialises
		self.current_phase = "SETUP";


		self.game_over = False;

	def game_loop(self):

		card = None;



		#c = Card("dummy", "url");

		'''test = pygame.image.load("back.png");

		test_rect = test.get_rect();

		screen.blit(test, test_rect)

		#pygame.display.update();'''




		for card_name, card_details in self.new_deck.items():
			if 'image' in card_details:
				print('image found')
				card = Card(card_name, card_details['url']);




		while not self.game_over:

			for event in pygame.event.get():


				#check whether a key was pressed here


				if event.type == pygame.QUIT:

					pygame.quit();

					self.game_over = True;



			if self.current_phase == "SETUP":

				self.setup();

			elif self.current_phase == "UP":

				self.up_phase();

			elif self.current_phase == "DRAW":

				self.draw_phase();

			'''elif self.current_phase == "ENER":

				
				self.system_message(f"HAND {self.hand}");
				self.system_message(f"FIELD LRIG {self.field_lrig}");
				self.system_message(f"FIELD SIGNI {self.field_signi}");

				self.ener_phase();


			elif self.current_phase == "GROW":

				self.grow_phase();

			elif self.current_phase == "MAIN":

				self.main_phase();

			elif self.current_phase == "ATTACK":

				self.attack_phase();

			elif self.current_phase == "END":

				self.end_phase();'''

		#print(self.hand)

		#Draw cards to screen

			screen.fill((0, 0, 0));


			if card:

				card.draw(screen);

		#print(card.pos);


			pygame.display.update();

		#print(self.current_phase);

		#c.draw(screen);
		#c.update_pos(100, 100);

		#pygame.time.wait(100);

		#self.next_phase();



	def up_phase(self):

		print("UP" , self.field_lrig);


		if self.field_signi:

			for cards, props in self.field_signi.items():

				if props.get('state') == 'DOWN':

					self.field_signi[cards]['state'] = 'UP';

		#print(type(self.field_signi))

		self.next_phase();

	def draw_phase(self):

		print("DRAWING");

		if self.first == True:

			count = 1;

		else:

			count = 2;
			
		#self.draw_cards(self.hand, count, self.field_signi);

		#print(self.field_signi);

		self.next_phase();





	'''def draw_phase(self):

	def ener_phase(self):

	def grow_phase(self):

	def main_phase(self):

	def attack_phase(self):

	def end_phase(self):
'''













	def load_card_database(self):

		card_tree = ET.parse("01.Wixoss TCG.xml");

		card_root = card_tree.getroot();

		pcard_root = card_tree.getroot();

		database_cards = {};

		count = 0;

		index = 0;
		
		#print(list(database_cards.keys()));

		#print(list(database_cards.keys()))

		card_properties = {};

		deck = {};

		new_deck={}

		done = False;

		signi_count = 0;
		lrig_count = 0;
		spell_count = 0;
		piece_count = 0;

		card_amount = 1;

		card_state = "UP";


		deck_tree = ET.parse("Diva Debut.xml");

		deck_root = deck_tree.getroot();

		for cards in deck_root.findall(".//card"):

			amount_element = int(cards.get('number'));

		for card in card_root.findall(".//card"):

			card_name = card.find('name').text if card.find('name') is not None else "Unknown";
			text_element = card.find('text').text if card.find('text') is not None else "Unknown";
			maintype_element = card.find('maintype').text if card.find('maintype') is not None else "Unknown";
			color_element = card.find('colors').text if card.find('colors') is not None else "Unknown";
			card_url_tag = card.find('set');
			pic_url = card_url_tag.get('picURL') if card_url_tag is not None else "No URL";


			for prop in card.findall('.//prop'):

				limit_element = prop.find('loyalty').text if prop.find('loyalty') is not None else "Unknown";
				level_element = prop.find('cmc').text if prop.find('cmc') is not None else "Unknown";
				cost_element = prop.find('manacost').text if prop.find('manacost') is not None else "Unknown";
				power_element = prop.find('pt').text if prop.find('pt') is not None else "Unknown";
				type_element = prop.find('type').text if prop.find('type') is not None else "Unknown";


				for child in prop:

					card_properties[child.tag] = child.text;

					#print(card_properties);
			#name_element = card.find('name').text if card.find('name') is not None else "Unknown";
				

			if card_name:

				#print(card_amount);

				#This creates a dictionary entry in database_cards at the 'card name'
				database_cards[card_name] = {
					'name': card_name,
					'text': text_element,
					'maintype': maintype_element,
					'colors': color_element,
					'limit': limit_element,
					'level': level_element,
					'cost': cost_element,
					'power': power_element,
					'type': type_element,
					'state': card_state,
					'url': pic_url,

					**card_properties

							#this is fucking magic and I love it
							


			}

			'''database_cards[card_name] = card;
			database_cards[card_text] = text;'''

		for card_name in self.init_deck:


			if card_name in database_cards:

				#print(card_name)


			#print(card_name)

			#print(card_name);

			#print(database_cards)



				#print(f"Card '{card_name}' found");
				#print(f"MAINTYPE: {database_cards[card_name]}");
				#print(database_cards[card_name]);
				#print(database_cards[card_name]['text'])

				#print(database_cards[card_name].items());

				#print(database_cards[card_name]['maintype'])

				if database_cards[card_name]['maintype'] != "LRIG" and database_cards[card_name]['maintype'] != "LRIG|Assist" and database_cards[card_name]['maintype']\
				!= "PIECE":


					for i in range(self.card_amount):
				
						deck[f"{card_name} {i}"] = {key: value for key, value in database_cards[card_name].items() if key in\
							['name', 'text', 'maintype', 'colors', 'limit',\
							'level', 'cost', 'power', 'type', 'url']}

					#print(card_name)



					#print(database_cards[card_name]['name'])
					#print(database_cards[card_name]['maintype']);

				else:

					self.lrigdeck[card_name] = {key: value for key, value in database_cards[card_name].items() if key in\
							['name', 'text', 'maintype', 'colors', 'limit',\
							'level', 'cost', 'power']}


								#print(f"Card '{card_name}' found!");


				#count += 1;

						#print(f"{key}: {value}");

				#print("__________________________________________________________");
		
		#print(new_deck)

		self.new_deck = deck;


		for card_name, details in deck.items():

			if details.get('maintype') == 'LRIG' or details.get('maintype')\
			 == 'LRIG|Assist' or details.get('maintype') == 'PIECE':
			 	self.lrigdeck[card_name] = details;

			'''if details.get('maintype') == 'SIGNI' or details.get('maintype')\
			 == 'SIGNI|LB' or details.get('maintype') == 'SPELL':
			 	deck[card_name] = details;'''




		#check for LRIGS
		lrig_cards = {name: details for name, details in deck.items() if\
		details.get('maintype') == 'LRIG' or details.get('maintype') == 'LRIG|Assist'}

		for lrig in self.lrigdeck:

			lrig_count += 1;

		#lrigdeck = lrig_cards;
		#print(lrigdeck)

		#check for SIGNI
		signi_cards = {name: details for name, details in deck.items() if\
		details.get('maintype') == 'SIGNI' or details.get('maintype') == 'SIGNI|LB'\
		and details.get('maintype') != "SPELL" and details.get('maintype') != "SPELL|LB"}

		for signi in signi_cards:

			#print(signi)

			signi_count += 1;

		#Check for Spells

		spell_cards = {name: details for name, details in deck.items() if\
		details.get('maintype') == 'SPELL' or details.get('maintype') == 'SPELL|LB'}

		for spells in spell_cards:

			#print(signi)

			spell_count += 1;

		#Check for PIECE card

		piece_cards = {name: details for name, details in self.lrigdeck.items() if\
		details.get('maintype') == 'PIECE' or details.get('maintype') == 'PIECE|LB'}

		for piece in piece_cards:

			#print(signi)

			piece_count += 1;


		#count = signi_count + lrig_count + spell_count + piece_count;
				
		#print(piece_cards)

		done = True;
		self.system_message(f"Deck loaded, added {signi_count + lrig_count + spell_count + piece_count} cards!\
			 (PIECE included in count)");
		self.system_message(f"SIGNI count {signi_count}");
		self.system_message(f"LRIG count {lrig_count}");
		self.system_message(f"SPELL count {spell_count}");
		self.system_message(f"PIECE count {piece_count}");
		#print("SIGNI>>", deck);
		#print("LRIG>>", self.lrigdeck);






	def load_deck(self):

		self.init_deck = [];

		card_tree = ET.parse("DIVA DEBUT DECK Nijisanji ver. Sanbaka.xml");

		card_root = card_tree.getroot();

		for lrig in card_root.findall(".//card"):

			card_name = lrig.get('name');
			self.card_amount = int(lrig.get('number')) if lrig.get('number')\
			is not None else 1;

			if card_name:

				for i in range(self.card_amount):

					self.init_deck.append(card_name);
				#self.init_deck.append(self.card_amount);

		#print(self.init_deck);
			#print(lrig.get('number'));






		#def get_cards(self):























	def start_phase(self, phase):
		if phase in self.phases:
			self.phases[phase] = True;
			self.current_phase = phase;

	def end_phase(self, phase):
		if phase in self.phases:
			self.phases[phase] = False;

	def next_phase(self):
		phase_order = ["SETUP", "UP", "DRAW", "ENER", "GROW", "MAIN", "ATTACK",
		"END"];
		current_index = phase_order.index(self.current_phase);
		next_index = (current_index + 1) % len(phase_order);
		self.end_phase(self.current_phase);
		self.start_phase(phase_order[next_index]);

		self.system_message("NEXT PHASE");

		#print(phase_order[next_index])


		#CARD PHASES IN ORDER

	def draw_cards(self, deck, draw_count, destination):

		i = 0;

		#print(type(list(destination.keys())))
		#print(list(deck.keys()))

		while i < draw_count:

			deck_keys = list(deck.keys());

			key = deck_keys.pop(i);

			card = deck.pop(key);

			destination[key] = card;

			i += 1;







		#SETUP phase will take 3 level 0 LRIG and put them on the field in LRIG ZONE. One level 0 LRIG will be the 'center' LRIG
		# or the main LRIG, with which a player may use to attack one another's life cloth directly.


	#GAMEPLAY FUNCTIONS:

	def system_message(self, msg):

		if msg:

			print(f"<SYSTEM: {msg}>");







	def set_lrigs(self, ldeck):

		if ldeck:

			for lname, ldetails in ldeck.items():


				if ldetails['level'] == '0':

					#print(ldetails['level']);
					#print(lname)

					ldetails['name'] = lname;

					print(f"Found {lname} at Lv. {ldetails['level']}");

					self.field_lrig[lname] = ldetails;

					#print(self.field_lrig);

	def coin_toss(self):


		try:

			choice = int(input("COIN TOSS> Choose 1 for heads and 2 for tails and (press ENTER)?>"));

		
			rand_num = randint(1, 2);

			if rand_num == choice:

				self.system_message("You will go first.");

				self.first = True;

			else:

				self.system_message("You will go second.");




		except ValueError:

			self.system_message("Choice must be an integer!");

			self.coin_toss();

	def preload_card_gfx(self):

		#Loop between cards to be displayed
		# and set their url to an image source

		for card, details in self.new_deck.items():

			pic_url = details.get('url');

			#print(pic_url)

			if pic_url:

				c = Card(card, pic_url);

				#print(c.image);

				self.new_deck[card]['image'] = c.image;










		



























	def setup(self):

		#self.new_deck = dm.shuffle(self.new_deck);

		#shuffle deck
		#self.phases['SETUP'] = True;

		self.new_deck = dm.shuffle(self.new_deck);

		#print(self.lrigdeck);

		self.set_lrigs(self.lrigdeck);


		#Draw Hand of 5 cards
		self.draw_cards(self.new_deck, 5, self.hand);

		#Draw 7 cards for life cloth
		self.draw_cards(self.new_deck, 7, self.lifecloth);

		#self.coin_toss();

		self.system_message("OPEN!");

		self.preload_card_gfx();

		self.next_phase();

		#self.start_phase('UP');

		#print(self.lifecloth)

		#print(self.field_lrig);

		


#c = Card();
w = WixossGame();
w.load_deck();
w.load_card_database();
dm = DeckManager(w.new_deck);
w.setup();
w.game_loop();







