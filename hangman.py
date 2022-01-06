import pygame, sys
from pygame.locals import *
import random
# set up pygame
pygame.init()

def printLetters(letter, word, windowSurface):
    fontname = pygame.font.match_font('courier', bold=False, italic=False)
    basicFont = pygame.font.Font(fontname, 48)
    totalLength = int(windowSurface.get_rect().width*.8)
    pieceLength = int(totalLength/len(word) - .02*windowSurface.get_rect().width)
    height = int(windowSurface.get_rect().height*.55)
    for i in range(len(word)):
        if letter.upper() == word[i].upper():
            text = text = basicFont.render(word[i], True, TAN, BACKGROUND)
            textRect = text.get_rect()
            textRect.centerx = int((windowSurface.get_rect().width - totalLength)/2 + i*(pieceLength +.02*windowSurface.get_rect().width) + .5*pieceLength)
            textRect.centery = height
            windowSurface.blit(text, textRect)
def isPressed(rectangle, mouseEvent):
    [right, down] = mouseEvent.pos
    leftBound = rectangle[0]
    rightBound = rectangle[0] + rectangle[2]
    upperBound = rectangle[1]
    lowerBound = rectangle[1] + rectangle[3]
    if (right > leftBound) and (right < rightBound) and (down < lowerBound) and (down > upperBound):
        return True
    return False
def drawLetters(grayedOut, green, windowSurface): #where grayedOut is a list of letters that are wrong and green are a list of correctly chosen letters
    letterRects = []
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARKGREEN = (0,150,0)
    GRAY = (180, 180, 180)
    BLUE = (0, 0, 255)
    BACKGROUND = (106,0,106) #dark violet
    TAN = (255, 236, 139)
    # set up fonts

    fontname = pygame.font.match_font('courier', bold=False, italic=False)
    basicFont = pygame.font.Font(fontname, 48)

    letter = 'A'
    row = 0
    col = 0
    lettersInRow = 13
    for i in range(lettersInRow): #firstrow
        text = text = basicFont.render(letter, True, BACKGROUND, TAN)
        if letter in grayedOut:
            text = text = basicFont.render(letter, True, BLACK, GRAY)
        elif letter in green:
            text = text = basicFont.render(letter, True, GREEN, DARKGREEN)
        textRect = text.get_rect()
        letter = chr(ord(letter) + 1)
        if col == 0:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*48/lettersInRow/10)
        if col == 1:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*40/lettersInRow/10)
        if col == 2:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*32/lettersInRow/10)
        if col == 3:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*24/lettersInRow/10)
        if col == 4:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*16/lettersInRow/10)
        if col == 5:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*8/lettersInRow/10)
        if col == 6:
            textRect.centerx = int(windowSurface.get_rect().centerx)
        if col == 7:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*8/lettersInRow/10)
        if col == 8:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*16/lettersInRow/10)
        if col == 9:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*24/lettersInRow/10)
        if col == 10:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*32/lettersInRow/10)
        if col == 11:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*40/lettersInRow/10)
        if col == 12:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*48/lettersInRow/10)
        col = (col + 1)%13
        #textRect.centerx = int(windowSurface.get_rect().centerx)
        textRect.centery = .7 * windowSurface.get_rect().height
        letterRects.append(textRect)
        windowSurface.blit(text, textRect)
    for i in range(lettersInRow): #second row
        text = text = basicFont.render(letter, True, BACKGROUND, TAN)
        if letter in grayedOut:
            text = text = basicFont.render(letter, True, BLACK, GRAY)
        elif letter in green:
            text = basicFont.render(letter, True, GREEN, DARKGREEN)
        textRect = text.get_rect()
        letter = chr(ord(letter) + 1)
        if col == 0:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*48/lettersInRow/10)
        if col == 1:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*40/lettersInRow/10)
        if col == 2:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*32/lettersInRow/10)
        if col == 3:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*24/lettersInRow/10)
        if col == 4:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*16/lettersInRow/10)
        if col == 5:
            textRect.centerx = int(windowSurface.get_rect().centerx - windowSurface.get_rect().width*8/lettersInRow/10)
        if col == 6:
            textRect.centerx = int(windowSurface.get_rect().centerx)
        if col == 7:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*8/lettersInRow/10)
        if col == 8:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*16/lettersInRow/10)
        if col == 9:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*24/lettersInRow/10)
        if col == 10:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*32/lettersInRow/10)
        if col == 11:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*40/lettersInRow/10)
        if col == 12:
            textRect.centerx = int(windowSurface.get_rect().centerx + windowSurface.get_rect().width*48/lettersInRow/10)
        col = (col + 1)%13
        #textRect.centerx = int(windowSurface.get_rect().centerx)
        textRect.centery = int(.8 * windowSurface.get_rect().height)
        letterRects.append(textRect)
        windowSurface.blit(text, textRect)

    return letterRects
def findLetter(mouseEvent, letterRects):
    letter = 'A'
    for rect in letterRects:
        if isPressed(rect, mouseEvent):
            return letter
        letter = chr(ord(letter) + 1)
    return -1
def drawMan(errors, windowSurface):
    TAN = (255, 236, 139)
    if errors == 1:
        #draw the head
        pygame.draw.circle(windowSurface, TAN, (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height)), 30, 4)
    if errors == 2:
        #draw the spine
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 30), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 96), 4)
    if errors == 3:
        #draw left arm
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx - 30, int(.27*windowSurface.get_rect().height) + 50), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 60), 4)
    if errors == 4:
        #draw the right arm
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx + 30, int(.27*windowSurface.get_rect().height) + 50), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 60), 4)
    if errors == 5:
        #draw the left leg
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx - 30, int(.27*windowSurface.get_rect().height) + 110), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 95), 4)
    if errors == 6:
        #draw the right leg and game over
        fontname = pygame.font.match_font('impact', bold=True, italic=False)
        madFont = pygame.font.Font(fontname, 120)
        RED = (255, 0, 0)
        text = madFont.render('GAME OVER', True, RED, BACKGROUND)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = int(windowSurface.get_rect().centery*.28)
        windowSurface.blit(text, textRect)
        pygame.draw.circle(windowSurface, TAN, (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height)), 30, 4)
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 30), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 96), 4)
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx - 30, int(.27*windowSurface.get_rect().height) + 50), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 60), 4)
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx + 30, int(.27*windowSurface.get_rect().height) + 50), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 60), 4)
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx - 30, int(.27*windowSurface.get_rect().height) + 110), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 95), 4)
        pygame.draw.line(windowSurface, TAN, (windowSurface.get_rect().centerx + 30, int(.27*windowSurface.get_rect().height) + 110), (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height) + 95), 4)
        for letter in word:
            printLetters(letter, word, windowSurface)
def checkStatus(errors, green, word):
    if errors >= 6:
        return "LOST"
    for i in word:
        if i not in green:
            return "INCOMPLETE"
    return "WON"
# set up the window
scale = .6
w = int(pygame.display.Info().current_w * scale)
h = int(pygame.display.Info().current_h * scale)

windowSurface = pygame.display.set_mode((600, 700), 0, 32)
#windowSurface = pygame.display.set_mode((w, h), 0, 32)
pygame.display.set_caption('Hangman')
def getHint(gray, green, word):
    indexes = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for i in alphabet:
        if (i not in word) and (i not in gray):
            indexes.append(i)
    letter = indexes[random.randint(0, len(indexes)-1)]
    return letter
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0,150,0)
GRAY = (180, 180, 180)
BLUE = (0, 0, 255)
BACKGROUND = (106,0,106) #dark violet
TAN = (255, 236, 139)
# set up fonts

fontname = pygame.font.match_font('courier', bold=False, italic=False)
basicFont = pygame.font.Font(fontname, 48)

# set up the text
text = basicFont.render('HANGMAN', True, TAN, BACKGROUND)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery//3

# draw the white background onto the surface
windowSurface.fill(BACKGROUND)
# draw the text onto the surface
windowSurface.blit(text, textRect)

letterRects = drawLetters([],[],windowSurface)
hintText = basicFont.render("HINT", True, BACKGROUND, TAN)
hintTextRect = hintText.get_rect()
hintTextRect.centerx = windowSurface.get_rect().centerx
hintTextRect.centery = int(.921 * windowSurface.get_rect().height)
windowSurface.blit(hintText, hintTextRect)

# draw the window onto the screen
file  = open("easyWords.txt", "r")
content = file.read()
file.close()
words = content.split()
wordIndex = random.randint(0,len(words)-1)
word = words[wordIndex].upper()
#word = "SHUSH"
#word = "LANDON"
totalLength = int(windowSurface.get_rect().width*.8)
pieceLength = int(totalLength/len(word) - .02*windowSurface.get_rect().width)

for i in range(len(word)):
    pygame.draw.line(windowSurface, TAN, (int((windowSurface.get_rect().width - totalLength)/2 + i*(pieceLength +.02*windowSurface.get_rect().width)), int(windowSurface.get_rect().height*.6)), (int(pieceLength + (windowSurface.get_rect().width - totalLength)/2 + i*(pieceLength +.02*windowSurface.get_rect().width)), int(windowSurface.get_rect().height*.6)), 4)

pygame.display.update()
gray = []
green = []
errors = 0
hints = 1;
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            if checkStatus(errors, green, word) == "INCOMPLETE":
                if hints <= 5:
                    if isPressed(hintTextRect, event):
                        hints = hints + 1
                        gray.append(getHint(gray, green, word))
                        drawLetters(gray, green, windowSurface)
                        pygame.display.update()
                if hints == 5:
                        hintText = basicFont.render("HINT", True, BLACK, GRAY)
                        hintTextRect = hintText.get_rect()
                        hintTextRect.centerx = windowSurface.get_rect().centerx
                        hintTextRect.centery = int(.921 * windowSurface.get_rect().height)
                        windowSurface.blit(hintText, hintTextRect)
                letter = findLetter(event, letterRects)
                if letter != -1:
                    printLetters(letter, word, windowSurface)
                    if letter in word.upper():
                        green.append(letter)
                    elif letter not in gray:
                        gray.append(letter)
                        errors = errors + 1
                    drawLetters(gray, green, windowSurface)
                    drawMan(errors, windowSurface)
                    pygame.display.update()
            if checkStatus(errors, green, word) == "WON":
                fontname = pygame.font.match_font('impact', bold=True, italic=False)
                madFont = pygame.font.Font(fontname, 120)
                text = madFont.render('YOU WIN', True, GREEN, BACKGROUND)
                textRect = text.get_rect()
                textRect.centerx = windowSurface.get_rect().centerx
                textRect.centery = int(windowSurface.get_rect().centery*.28)
                windowSurface.blit(text, textRect)
                if errors > 0:
                    pygame.draw.circle(windowSurface, TAN, (windowSurface.get_rect().centerx, int(.27*windowSurface.get_rect().height)), 30, 4)
                pygame.display.update()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
