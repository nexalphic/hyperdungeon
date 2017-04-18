#this is the new frontier

#Contains the data for the generator module to use.

#monster data: "name", attack damage, health, "first adjective", "second adjective",
#"death message", xp, level
monsters = [
	("Green Slime", 5, 1, "disgusting", "sticky", "dissolves away", 1, 1),
	("Giant Rat", 6, 1, "filthy", "wild", "flops over and dies.", 2, 1),
	("Jackal", 7, 2, "wild", "hungry", "flops over and dies.", 3 , 1),
	("Bat", 6, 3, "screeching", "flying", "falls to the floor bleeding.", 3, 2),
	("Zombie", 9, 3, "undead", "rotting", "falls over, truly dead", 4, 2),
	("Kobold", 11, 4, "short", "blue skinned", "shivers violently and falls dead.", 4, 3),
	("Goblin", 15, 4, "hunched", "green", "dies from its wounds.", 6, 3),
	("Skeleton", 15, 5, "bony", "clacking", "crumbles into bones.", 6, 3),
	("Blue Slime", 17, 6, "disgusting", "sticky", "dissolves away.", 7, 4),
	("Cave Spider", 17, 7, "creepy", "crawling", "flops upside down and dies.", 7, 4),
	("Water Elemental", 20, 8, "shifting", "fluidic", "dissolves into harmless water on the ground.", 8, 5)]

#room detail data: percentage chance to generate, "string", "action"
#if action is boolean false, then there is no action.
room_details = [
	(10, "The sound of a synth is in the", False),
	(10, "A mural of the ultimate creator covers the ceiling in the", False),
	(10, "Several headless statues are scattered throughout the", False),
	(30, "Part of the ceiling has collapsed into the", False),
	(30, "A large demonic idol with ruby eyes sits in the", False),
	(30, "A throne upon a stone dais is in the", "throne")
	#Note: remember to create throne action events
	(30, "A mural of ghoulish carnage covers the ceiling in the", False),
	(30, "A mural of the universe's planes covers the ceiling in the", False),
	(30, "A shallow pool of quicksilver lies in the", False),
	(30, "A tile mosaic of legendary monsters covers the floor in the", False),
	(30, "A tile mosaic of legendary heroes covers the floor in the", False),
	(40, "Several rotten apples are scattered about the", "Rotten Food"),
	(40, "Mushrooms are growing along the floor in the", "Mushroom"),
	(50, "The floor is covered with teeth in the", "Teeth"),
	(50, "There is a toppled statue in the", False),
	(50, "A acrid odour fills the", False),
	(50, "There is a high domed ceiling in the", False),
	(50, "There are withered corpses in the", False),
	(50, "A tile labyrinth covers the floor in the", False),
	(50, "Perfect hexagonal tiles covers the floor in the", False),
	(50, "A stream of blood flows a channel in the floor in the", False),
	(50, "Part of the wall has collapsed in the", False),
	(50, "The scent of ozone fills the", False),
	(50, "The floor is covered with dust in the", False),
	#Note: remember to create fountain action event
	(50, "A clear pool of water is in the", "Fountain"),
	(50, "A deep blue pool of water is in the", "Fountain"),
	(50, "A light blue pool of water is in the", "Fountain"),
	(50, "A pool of greenish water is in the", "Fountain"),
	(50, "A pool of indigo is in the", "Fountain"),
	(50, "A carved stone statue stands in the", False),
	(50, "The sound of chanting is in the", False),
	(50, "The sound of sobbing is in the", False),
	(50, "The sound of marching is in the", False),
	(50, "The sound of tapping is in the", False),
	(50, "The sound of running is in the", False),
	(50, "The sound of whistling is in the", False),
	(50, "The sound of mournful whistling is in", False),
	(50, "The sound of rattling is in the," False),
	(50, "The sound of horns is in the", False),
	(50, "The sound of a flute is in the", False),
	(50, "The sound of a guitar is in the", False),
	(50, "The sound of scratching is in the", False),
	(50, "The sound of splashing is in the", False),
	(50, "The sound of moaning is in the", False),
	(50, "The sound of knocking is in the", False),
	(50, "The sound of rushing water is in", False),
	(50, "A simple fireplace sitting against the wall is in the", False),
	(50, "The floor is covered with ash in the", False),
	(50, "Iron chains hang from the ceiling in the", False),
	(50, "An unexplained breeze can be felt in the", False),
	(50, "Spirals of white stones cover the floor in the", False),
	(50, "Spirals of black stones cover the floor in the", False),
	(50, "Burning torches cover the wall in the", False),
	(50, "Several corpses are impaled on spikes on ceiling in the", False)
]

#trap data: percentage chance to generate, trap name, effect, numbers of turns affecting, damage, damage type, level
traps = (
	#level 1 setback traps
	(10, "Teleporter Crystal", "Teleport", False, False, False, "Any"),
	(40, "Magic Missile", False, "1d3", False, "arcane", 1),
	(50, "Rune Of Paralyzation", "paralyze", "1d4", False, False, 1),
	(50, "Net", "restrain", False, False, False, 1),
	(50, "Symbol of Panic", "frightened", "1d3", False, False, 1),
	(50, "Rune of Fear", "frightened", "1d2", False, False, 1),
	(50, "Arrow", False, False, False, "1d2", 1),
	(50, "Symbol of Hypnosis", "frightened", "1d4", False, 1)
)

	
