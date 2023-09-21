# custom-chess
Overview

This project implements a simplified version of chess with custom rules and logic. Unlike traditional chess, this version has a unique winning condition: to win, a player must get their king to the 8th rank of the board. Checks are not allowed on either king by either player, and the starting position is different from the standard chess setup.
Table of Contents

    Features
    Demo
    Getting Started
        Prerequisites
        Installation
    Usage
    Rules and Gameplay
    Contributing
    License

Features

    Custom chess rules and logic
    Player vs. Player (PvP) gameplay
    Move validation and error handling
    Detection of game state (UNFINISHED, WHITE_WON, BLACK_WON, TIE)
    Interactive command-line interface (CLI)

Demo

[Include a link to a video or GIF demonstrating the gameplay if available.]
Getting Started
Prerequisites

    Python 3.x

Installation

    Clone the repository to your local machine:

    shell

git clone https://github.com/YourUsername/SimplifiedChess.git

Navigate to the project directory:

shell

    cd SimplifiedChess

Usage

To play the game, run the following command:

shell

python chess.py

Follow the on-screen instructions to make moves and play the game.
Rules and Gameplay

In this simplified version of chess:

    The game can be won by either white or black, result in a tie, or remain unfinished.
    To win, a player must move their king to the 8th rank.
    Checks on either king are not allowed.
    Moves only require specifying the starting square and the ending square in standard chess notation (e.g., 'e5 to d4').
    There are no pawns in the game, so there is no promotion.
    Castling is impossible in this version.
