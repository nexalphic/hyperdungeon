#this is the new frontier

#Contains the data for the generator module to use.

#monster data: "name", attack damage, health, "first adjective", "second adjective",
#"death message", xp, level
monsters = [
    ("Green Slime", 5, 1, "disgusting", "sticky", "dissolves away", 1, 1),
    ("Giant Rat", 6, 1, "filthy", "wild", "flops over and dies.", 2, 1),
    ("Jackal", 7, 2, "wild, "hungry", "flops over and dies.", 3 , 1),
    ("Bat", 6, 3, "screeching", "flying", "falls to the floor bleeding.", 3, 2),
    ("Zombie", 9, 3, "undead", "rotting", "falls over, truly dead", 4, 2),
    ("Kobold", 11, 4, "short", "blue skinned", "shivers violently and falls dead.", 4, 3),
    ("Goblin", 15, 4, "hunched", "green", "dies from its wounds.", 6, 3),
    ("Skeleton", 15, 5, "bony", "clacking", "crumbles into bones.", 6, 3),
    ("Blue Slime", 17, 6, "disgusting", "sticky", "dissolves away.", 7, 4),
    ("Cave Spider", 17, 7, "creepy", "crawling", "flops upside down and dies.", 7, 4),
    ("Water Elemental", 20, 8, "shifting", "fluidic", "dissolves into harmless water on the ground.", 8, 5)]

#room detail data: percentage chance to generate, "string", "action"
#if action is  
room_details = [
    (10, "A mural of the ultimate creator covers the ceiling.", false),
    
