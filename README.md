# Pygame-Project
Project for CSCI 3328 OOP in Python. This is to be a project using Pygame module and library

Our current goals are to give this game a window to play on, instead of using terminal
and keyboard characters for the map. This will be achieved using Pygame surface functions. The
player and enemies will now be changed to sprites, instead of keyboard characters. Using
Pygame’s image manipulation functions, battle screens can be implemented using the same
images for sprites. This will look somewhat like Pokemon battle encounters. Pygame will also
allow for easier movement systems that will shorten the code. Previously, WASD was used to
move but the method in which the game detected movement was not sufficient. Again, using
image functions, characters will flip their images depending on which direction they move. We
will also be using Pygame to implement various sounds and music. Lastly, we will be using
import OS to use it’s paths and directories functions to be able to use all of the necessary in game
items, such as armor and weapons, in addition to images and sounds.

The current challenges we envision start with implementing all the class systems for the
map, player, character, and even the items. Each humanoid (player and enemies), will have
various stats such as health, and inventory slots. These humanoid classes will have subclasses
player and enemies. Then they will also have interaction with item classes such as weapons and armor.
These too will have various stats such as added health and damage. Another challenge we
will face will be applying the enemy tracking system through python and Pygame specifically.
We are unfamiliar with all of Pygame’s functions so either there are functions to assist this or
this will all have to be done manually with an array system for player position and enemy
positions. The tracking was created with somewhat of a coordinate system, so if Pygame has
resources for that it could help. Another challenge would be creating a database of leveled items
to spawn and to be used by the player and enemies. All items spawn depending on the current
map level and each has their own stats. So we would need a way to track map level, and grab the
currently available items. If OS or Pygame have functions to assist in database control, we could
have an easier system of item spawning and item use by the player and enemies. Another
challenge that will be completely new to us, will be adding sounds and music to the game.
However, Pygame is able to easily implement any sounds into the program and the only
challenge will be using Pygame functions correctly. Lastly, the unfinished game was heavily
unbalanced. There are ten levels and through multiple playthroughs, the farthest anybody has
gotten is level 5. The reason for this project is to learn about creating games in all levels of
development, and this includes gameplay balancing. It is no fun playing a game that is unfair.
We will have the challenge of altering the game’s luck based battle system and create something
that is challenging but fair to play.

For this game we will mostly be using the Pygame framework. It has many different
already created resources and functions that are meant for building games which will be
useful.The SDL library which is included in Pygame gives the program low-level access to
various hardware inputs such as keyboard and mouse. On top of this, we will be building our
own architecture with our various classes. As mentioned, most of these will inherit from the few
general classes such as humanoid and items. This architecture will allow for different characters
and items to hold different stats and even attributes. These will be used for every movement,
item storage, and battles.
Our timeline will separate each task in order of program dependency. For example, we
can’t create anything in the program without first knowing what it will consist of. So we will
dedicate this first week to understanding the original game code and figuring out how it works,
and how to implement it with Pygame. Then we will begin working on creating the necessary
classes and their functions and attributes. After that, we will work on the movement system for
the player, and tracking system for the enemies. The map design will come next, with various
levels, walls, item spawns, and enemy spawns implemented. After that part is done, we will
begin working on the battle system. If that gets improved and finished, we will finally move on
to working with sprites and giving the game some art. Somewhere in all this, we will also be
working on giving this game a unique feel, and we will create an original soundtrack for the
game. Various sounds might be obtained from free resources, and the music will be mostly
original work.
