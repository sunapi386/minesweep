Minesweep README
================
Run via

    $VENV/bin/pserve  development.ini --reload

Architecture
------------
This is the sequence of steps how I envision the minesweeper to work.
1/ Client loads page.
2/ Server:
    - Loads a new map for you, if no game found for you.
    - Otherwise, reloads your last game.
    - Ideally can handle resolve multiple clients.
3/ Client clicks on a grid, POST to server.
4/ Server does minesweeper logic, replies with:
    - win
    - lose
    - continuation (expanded grids)
5/ Client updates the view.

Criterias
---------
A game of minesweeper using the Pyramid framework (http://www.pylonsproject.org/) for the server side and javascript / jQuery for the client side.
The map should not be stored on the client side, to prevent cheating.
When you click on any one of the boxes, it should send an AJAX request to the server, to figure out the current status of the field, and update the map accordingly.
As game states are stored on the server, it should be possible to get back to the game by going to the URL.

The most important thing to us is how you structure your code - while having a full-functioned product is important, what's more important is having something that works bug free and is very nicely structured.

Bonus points: If you find that you have extra time, you can make it such that multiple people can work on the same game (e.g. if it is a large puzzle). You can also add any more bells and whistles you think would be cool.
