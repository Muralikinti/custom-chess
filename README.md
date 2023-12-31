# custom-chess
## **Overview**

This project implements a simplified version of chess with custom rules and logic. Unlike traditional chess, this version has a unique winning condition: to win, a player must get their king to the 8th rank of the board. Checks are not allowed on either king by either player, and the starting position is different from the standard chess setup.

### **Features**
- Custom chess rules and logic.
- Player vs. Player (PvP) gameplay.
- Move validation and error handling.
- Detection of game state (UNFINISHED, WHITE_WON, BLACK_WON, TIE)
- Interactive command-line interface (CLI)


### **Prerequisites**

      Python 3.x

### **Installation**
- Clone the repository to your local machine:

      git clone https://github.com/Muralikinti/custom-chess.git

- Navigate to the project directory:

      cd SimplifiedChess

### **Usage**

To play the game, run the following command:

      python chess.py

Follow the on-screen instructions to make moves and play the game.

### **Rules and Gameplay**

In this simplified version of chess:
- The game can be won by either white or black, result in a tie, or remain unfinished.
- To win, a player must move their king to the 8th rank.
- Checks on either king are not allowed.
- Moves only require specifying the starting square and the ending square in standard chess notation (e.g., 'e5 to d4').
- There are no pawns in the game, so there is no promotion.
- Castling is impossible in this version.
- White pieces are capitalized while the black pieces are not.
- Kings are denoted by 'k' or 'K', Rooks by either 'r' or 'R', Bishops by either 'b' or 'B' and knights are denoted by either 'n' or 'N'. 
