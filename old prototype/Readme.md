# Math 153 Final Project Documentation

## group members:
- Kent Nico Balondro
- Josef Vincent Jaen

## description:




## goal: zendo inspired game but with a few modifications
- 3x3 space for structure creation
- only triangle and rectangle shapes present
- no overlapping
- multiplayer might not be within reach (but i'll try to modify the program to have it when i can)

## ideas
- what if we have another window to show the structures already made in order to make the building area cleaner
- code can be made more efficient, i think
- watch out for memory leaks

- have a group member create the design (color palette/overall theme) of the game in order to make it less "flat"
    - in line with this, could we also have someone make a manual or a sheet of paper detailing how to play the game

## tasks
[/] create the shapes
    [/] rectangle
    [/] triangle
[/] create the grid
    [/] be able to insert the shapes on each cell individually
[ ] create the layout of the game
    [ ] finalize placement of each grid
    [/] test out each the shapes on each grid
    [ ] create spaces for the black and white stones (circles) for judging
[ ] implement the game loop
    [ ] implement the preliminaries
        [/] implement the secret rule thingy
            [ ] make a list/dictionary of options for the secret rule
            [ ] randomly select the secret rule
        [ ] implement the computer generated structures that follow the secret rule
        [ ] make the computer generate two structures at the start of a game: one valid and one not
    [ ] implement the building mechanic
        [ ] make buttons; finalize keyboard binds
        [ ] make the buttons functional
        [ ] have the player be able to build a structure
            [ ] place down a shape
            [ ] move a shape
            [ ] modify the color of a rectangle
            [ ] modify the color and orientation of a triangle
        [ ] have the player be able to confirm their structure and lock it in place
    [ ] implement the check mechanic
        [ ] tell mechanic
            [ ] have the computer be able to detect if a structure follows the secret rule(make sure to make this function a general case)
            [ ] make the computer drop a white or black circle depending on the result
            [ ] make the game keep the previous grid on static and the player now moves on to the next grid available
    [ ] implement the guess mechanic
        [ ] player spends a guessing token for each guess
        [ ] the player must be able to input in a certain manner their guess for the secret rule
[ ] implement the game end
    [ ] implement a win screen

        
** expound on this **
[ ] make gui
    [ ] create text to guide the player on which keyboard button to press
    [ ] create a main menu
[ ] polishing
    [ ] add music
        [ ] make own music if possible
    [ ] add particles and effects



