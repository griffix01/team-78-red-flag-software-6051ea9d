*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.  \n\n https://raw.githubusercontent.com/level-up-program/team-78-red-flag-software-6051ea9d/main/tests/robot/images/spec-by-example.png
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move up in the middle                    5             5             1                     UP           5           6           2
Move down in the middle                  5             5             1                     DOWN         5           4           2
Move left in the middle                  5             5             1                     LEFT         4           5           2
Move right in the middle                 5             5             1                     RIGHT        6           5           2
Move up from the bottom left corner      0             0             5                     UP           0           1           6
Move down from the bottom left corner    0             0             5                     DOWN         0           0           6
Move left from the bottom left corner    0             0             5                     LEFT         0           0           6
Move right from the bottom left corner   0             0             5                     RIGHT        1           0           6
Move up from the top left corner         0             9             6                     UP           0           9           7
Move down from the top left corner       0             9             7                     DOWN         0           8           8
Move left from the top left corner       0             9             8                     LEFT         1           9           9
Move right from the top left corner      0             9             9                     RIGHT        0           9           10
Move up from the bottom right corner     9             0             5                     UP           9           1           6
Move down from the bottom right corner   9             0             5                     DOWN         9           0           6
Move left from the bottom right corner   9             0             5                     LEFT         8           0           6
Move right from the bottom right corner  9             0             5                     RIGHT        9           0           6
Move up from the top right corner        9             9             12                     UP           9           9           13
Move down from the top right corner      9             9             12                     DOWN         9           8           13
Move left from the top right corner      9             9             12                     LEFT         8           9           13
Move right from the top right corner     9             9             12                     RIGHT        9           9           13

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}