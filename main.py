class GameObject: 
    # ovo drzimo samo zbog ucenja pajtonu ovo ne treba ali kod drugih jezika treba
    name = ""
    appearance = "" 
    feel = ""
    smell = ""
    
    # Field = varijabla, Method = funkcija

    # pravimo funkciju initilizer koja uzima parametre nase klase i parametar self pomocu koga
    # pozivamo sve ostale fildove (varijable)
    # self znaci sve sto pripada ovoj klasi i potrebno je svuda da bi program znao
    # Set upujemo instancu GameObject koja ima name, appearance, feel i smell
    def __init__(self, name, appearance, feel, smell):
        self.name = name    
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # pravimo methods odnosno funkcije  
    # vraca string koji opisuje appearence objekta  
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"
    
    # vraca string koji opisuje feel objekta 
    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"
    
    # vraca string koji opisuje smell objekta 
    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"

class Room:
    # klasa room ima escape code i listu game objects kao fields
    escape_code = 0
    game_objects = []

    # Set upujemo instacu Room koja ima escape code i game objects
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # vraca da li je kod koji je uneo igrac isti (True) kao escape kod ili nije (False)
    def check_code(self, code):
        return self.escape_code == code
    
    # vraca listu imena objekata koje imamo u sobi
    def get_game_objects_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names

class Game:
    # Set upujemo Game instancu sa defaultnom vrednosti od 0 pokusaja i room koja je puna
    # objekata sa kodom koji je 731
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(731, objects)

    # vraca 5 GameObjects sa dovoljno informacija da se pogodi kod
    def create_objects(self):
        return [
        GameObject(
        "Sweater",
        "It's a blue sweater that had the number 12 stitched on it.",
        "Someone has unstitched the second number, leaving only the 1.",
        "The sweater smells of laundry detergent."),
      GameObject(
        "Chair", 
        "It's a wooden chair with only 3 legs.",
        "Someone has deliberately snapped off one of the legs.",
        "It smells like old wood."),
      GameObject(
        "Journal",
        "The final entry states that time should be hours then minutes then seconds (H-M-S).",
        "The cover is worn and several pages are missing.",
        "It smells like musty leather."),
      GameObject(
        "Bowl of soup", 
        "It appears to be tomato soup.",
        "It has cooled down to room temperature.",
        "You detect 7 different herbs and spices."),
      GameObject(
        "Clock", 
        "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
        "The battery compartment is open and empty.",
        "It smells of plastic.")
        ]

    # ovde runujemo main game loop, uzimamo prompt i na pocetku poteza ga pozivamo
    def take_turn(self):
        # ovde pozivamo prompt iz game_room_prompt() metode
        prompt = self.game_room_prompt()
        # ovde biramo opcije iz prompta i konvertujemo ih u integere jer input uvek vraca
        # string
        selection = int(input(prompt))
        # ovde pravimo if statement da ako se biraju objekti igra nastavlja da lupuje
        # dok se ne pogodi kod
        if selection >= 1 and selection <= 5:
        # ovo radimo zbog indexiranja koje krece od 0 pa kada na primer izaberemo opciju 2
        # nama treba index 1
            self.select_object(selection - 1)
            self.take_turn()
        else:
            is_code_correct = self.guess_code(selection)
            if is_code_correct:
                print("You win!")
            else:
                if self.attempts == 3:
                    print("You lose!")
                else:
                    print(f"Incorrect code try again. You have {self.attempts}/3 attempts left.")
                    self.take_turn()

    # vraca prompt koji koristimo u game loopu koji govori igracu da ili izabere objekat sa
    # sa kojim interaguje ili da ukuca escape_kod 
    def game_room_prompt(self):
        prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
        # ovde uzimamo listu koju smo prethodno napravili u klasi room a to je lista
        # get_game_objects_names() i onda koristeci for loop dodajemo listu u prompt
        # a pomocu indexa ih obelezavamo od 1 do 5
        names = self.room.get_game_objects_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt
    # printuje interakciju (look, smell or touch) sa sa objektom na odredjenom (izabranom) indexu
    def select_object(self, index):
        # selected_object field poziva iz fielda room.game_objects izabrani index
        selected_object = self.room.game_objects[index]
        # ovde ga stavljamo u prompt i pozivamo kroz metodu get_object_interaction_string
        # i uzimamo ime sa tog indexa
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        # clue uzima string iz interaction_with_objects (objekat i interakciju) i printuje je 
        clue = self.interaction_with_objects(selected_object, interaction)
        print(clue)
        
    # ovo je metoda da pozovemo prompt koji ce da pita igraca na koji nacin zeli da interaguje
    # sa objektom (feel, touch ili smell)
    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n 1. Look\n 2. Touch\n 3. Smell\n"

    # ova metoda vraca string iz nase klase GameObject koji smo definisali pod look(), touch()
    # sniff()
    def interaction_with_objects(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else:
            return object.sniff()
        
    def guess_code(self, code):
        
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
            return False
            



game = Game()
game.take_turn()


#class RoomTests:

#     def __init__(self):
#         self.room1 = Room(111, [
#         GameObject(
#             "Sweater",
#             "It's a blue sweater that had the number 12 stitched on it.",
#             "Someone has unstitched the second number, leaving only the 1.",
#             "The sweater smells of laundry detergent."),
#         GameObject(
#             "Chair", 
#             "It's a wooden chair with only 3 legs.",
#             "Someone has deliberately snapped off one of the legs.",
#             "It smells like old wood."),
#         ])

#         self.room2 = Room(222, [])

#     def test_check_code(self):
#         print(self.room1.check_code(111) == True)
#         print(self.room1.check_code(222) == False)
    
#     def test_get_game_object_names(self):
#         print(self.room1.get_game_objects_names() == ["Sweater", "Chair"])
#         print(self.room2.get_game_objects_names() == [])

# tests = RoomTests()
# tests.test_check_code()
# tests.test_get_game_object_names()

#class GameObjectTests:

#     def __init__(self):
#         self.game_object_1 = GameObject("Knife", "Old", "Rusty", "Like chocolate")

#     def test_look(self):
#         print("Test look:", self.game_object_1.look() == "You look at the Knife. Old\n")

#     def test_touch(self):
#         print("Test feel:", self.game_object_1.touch() == "You touch the Knife. Rusty\n")

#     def test_sniff(self):
#         print("Test smell:", self.game_object_1.sniff() == "You sniff the Knife. Like chocolate\n")


# tests = GameObjectTests()
# tests.test_look()
# tests.test_touch()
# tests.test_sniff()
         




