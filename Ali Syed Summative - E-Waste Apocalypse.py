from pygame import *
from random import *

init()

SIZE = (width,height) = (1000,700) #Screen size (change to 1000,700)
screen = display.set_mode(SIZE)

#Colours
SEAGREEN = (144,188,144) #Polluted Sky
PERU = (205,133,63) #Dry Grass
MAROON = (128,0,0) #Dirt
BLACK = (0,0,0) #Oil/Shoe
WHITE = (255,255,255) #White Cloud
GRAY = (100,100,100) #Cloud/Smoke

SKIN = (240,207,158) #Skin Colour
BLUE = (30,144,255) #Eye
DARKBLUE = (25,25,112) #Clothes
BROWN = (165,42,42) #Hair
SLATE = (112,128,144) #Jetpack
ORANGE = (255,165,0) #Fire

GREEN = (0,128,0) #E-Waste Face
LIGHTGRAY = (220,220,220) #Computer
WHEAT = (245,222,179) #MUD on device
DARKGRAY = (100,100,100) #CPU
RED = (255,0,0) #Exclamation Mark

RUST = (210,90,0) #Factory
ROSYBROWN = (108,53,53) #Windows
STEELBLUE = (176,196,222) #Propane Containers
YELLOW = (255,215,0) #Caution Signs

LIME = (0,255,0) #States
GREY = (128,128,128) #Customizing Screen
PURPLE = (128,0,128) #Labels for Customization
DARKBROWN  = (129,69,32) #New Skin Colour

#Customization Main Colours
SKINCOLOUR = SKIN
EYECOLOUR = BLUE
HAIRCOLOUR = BROWN
PYJAMACOLOUR = DARKBLUE
SHOECOLOUR = BLACK

#Fonts
fontTitle = font.SysFont("American Purpose",100) #Title 
fontNormal = font.SysFont("American Purpose",40) #Titles for Instructions
fontInstruct = font.SysFont("American Purpose",20) #Instructions
fontSigns = font.SysFont("American Purpose",30) #Signs for smaller buttons
fontCustoms = font.SysFont("American Purpose",70) #Signs for bigger buttons

#Music (Loading Music)
startMusic = mixer.music.load("Kevin MacLeod - Thatched Villagers.wav")

#States
MAINSTATE = 0 #Main Menu
GAMESTATE = 1 #Game State
CUSTOMSTATE = 2 #Customization Menu
INSTRUCTSTATE = 3 #Instruction/Story Menu
CONTROLSTATE = 4 #Controls Menu
POWERUPSTATE = 5 #Power-Up Info Menu
GOSTATE = 6 #Game Over Menu
SKINSTATE = 7 #Skin Customization Menu
EYESTATE = 8 #Eye Customization Menu
HAIRSTATE = 9 #Hair Customization Menu
PYJAMASTATE = 10 #Pyjama Customization Menu
SHOESTATE = 11 #Shoe Customization Menu
CONTROLGO = 12 #Control Game Over Menu

#Loading Texts
scoreCount = font.SysFont("Times New Roman",20)  #initializing text

#Games States
KEY_SPACE = False #Space for character to move up or down

myClock = time.Clock() #Make graphics smoother (convert() also helped with that)
FPS = 60 #Frame per second

cloudX = 1100 #Makes cloud scroll from right to left
cloudY = 60 #Original y value of cloud
factoryX = 1000 #Makes factory scroll from right to left
oilSize = 3 #The size of the oil sands

platformY = height//1.14 #starting position of character
topScreen = 60 #Top of the screen
playerY = height//1.14 #y position of character

counter = 0 #Score counter
counterList = [] #HighScore List

charCount = 0 #Character count (for running effect)
charSteps = 100 #For the speed of character running effect
lastTime = time.get_ticks() #current time
charPos = False #To decide which pic. of character to bring up
playerSpeed = 5 #Speed of character

enemySpeed = 0 #Enemy counter (speeding up over time)
enemySpeed1 = 12 #For the speed of enemies appearing
enemySpeed2 = 19 #For the speed of enemies appearing
enemyNum = 0 #Enemy counter (increasing # over time)

#Tablet
enemyCount1 = 0 #Enemy counter
enemyAS1 = 10 #AS - Arrival Speed
enemyListX1 = [] #Keep track of enemies 
enemyListY1 = [] #Keep track of enemies 
enemyWidth1 = -60 #To make object leave screen smoothly

#CPU Case
enemyCount2 = 0 #Enemy counter
enemyAS2 = 1000 #AS - Arrival Speed
enemyListX2 = [] #Keep track of enemies 
enemyListY2 = [] #Keep track of enemies 
enemyWidth2 = -120 #To make object leave screen smoothly

#PowerUps (Speed)
powerupCount1 = 0 #PowerUp counter
powerupAS1 = 500 #As - Arrival Speed
powerupListX1 = [] #Keep track of power ups 
powerupListY1 = [] #Keep track of power ups
powerupWidth = -70 #To make object leave screen smoothly
speedUse = False #State of whether power up is activated
speedTimer = 0 #PowerUp1 Speed Timer
speedDuration = 500 #How long you can use power-up

#PowerUps (Vaporizing E-Waste Gun)
powerupCount2 = 0 #PowerUp counter
powerupAS2 = 1200 #As - Arrival Speed
powerupListX2 = [] #Keep track of power ups 
powerupListY2 = [] #Keep track of power ups
bulletList = [] #Keep track of bullets x-value
playerYList = [] #Keep track of bullets y-value
bulletUse = False #State of whether power up is activated
bulletTimer = 0 #PowerUp2 Bullet Timer
bulletDuration = 800 #How long you can use power-up

#Functions

def drawBG (x,y,FX): #Game Background 
    draw.rect(screen, SEAGREEN, (0,0,1000,700)) #Polluted Sky
    draw.rect(screen, PERU, (0,600,1000,30)) #Dry grass
    draw.rect(screen, MAROON, (0,630,1000,70)) #Dirt w/ oil sands
    
    #Oil sand generator
    for i in range (1,5):   
        for j in range (5,996,5):
            oilY = randint (635,645)
            draw.rect(screen, BLACK, (j,oilY,oilSize,oilSize))

    #Complex Cloud
    draw.polygon (screen, GRAY, [(x+155,y),(x+255,y),(x+255,y+30),(x+355,y+30),
                                  (x+355,y+65),(x+445,y+65),(x+445,y+100),(x+405,y+100),
                                  (x+405,y+130),(x+355,y+130),(x+355,y+160),(x+155,y+160),
                                  (x+155,y+130),(x+80,y+130),(x+80,y+100),(x,y+100),
                                  (x,y+65),(x+40,y+65),(x+40,y+30),(x+155,y+30)]) 
   
    draw.rect (screen, RUST, (FX+275,410,90,190)) #Tall Building
    draw.rect (screen, RUST, (FX+15,480,250,120)) #Long Building
    draw.rect (screen, RUST, (FX+265,565,10,35)) #Wall bw two buildings
    
    for a in range (425,531,35):
        draw.rect (screen, ROSYBROWN, (FX+290,a,22,22)) #Windows (Tall)
        draw.rect (screen, ROSYBROWN, (FX+330,a,22,22)) #Windows (Tall)
    for b in range (490,561,35):
        draw.rect (screen, ROSYBROWN, (FX+190,b,22,22)) #Windows (Long)
        draw.rect (screen, ROSYBROWN, (FX+230,b,22,22)) #Windows (Long)  
    draw.rect (screen, STEELBLUE, (FX+30,490,60,110)) #Container 1
    draw.rect (screen, STEELBLUE, (FX+110,490,60,110)) #Container 2
    for d in range (510,531,20):
        draw.rect (screen, YELLOW, (FX+30,d,60,10)) #Container Lines
        draw.rect (screen, YELLOW, (FX+110,d,60,10)) #Container Lines
    draw.rect (screen, ROSYBROWN, (FX+40,410,30,70)) #Gas Pipes 1
    draw.rect (screen, YELLOW, (FX+40,415,30,10)) #Gas Line 1
    draw.rect (screen, YELLOW, (FX+40,430,30,5)) #Gas Line 2
    draw.rect (screen, ROSYBROWN, (FX+90,410,30,70)) #Gas Pipes 2
    draw.rect (screen, YELLOW, (FX+90,415,30,10)) #Gas Line 1
    draw.rect (screen, YELLOW, (FX+90,430,30,5)) #Gas Line 2   
    draw.rect (screen, ROSYBROWN, (FX+140,410,30,70)) #Gas Pipes 3
    draw.rect (screen, YELLOW, (FX+140,415,30,10)) #Gas Line 1
    draw.rect (screen, YELLOW, (FX+140,430,30,5)) #Gas Line 2    
        
    draw.rect (screen, ROSYBROWN, (FX+390,480,100,120)) #Bottom Gas Buliding
    draw.rect (screen, YELLOW, (FX+385,460,110,20)) #Yellow Bottom Divider
    draw.rect (screen, ROSYBROWN, (FX+410,340,60,120)) #Top Gas Building
    draw.rect (screen, YELLOW, (FX+405,325,70,15)) #Yellow Top 
    for f in range (350,363,12):
        draw.rect (screen, YELLOW, (FX+410,f,60,5)) #Top Lines
    for g in range (490,503,12):
        draw.rect (screen, YELLOW, (FX+390,g,100,5)) #Bottom Lines
    
    #Polluted Clouds    
    draw.rect (screen, GRAY, (FX+390,278,120,28)) #Top Middle
    draw.rect (screen, GRAY, (FX+470,250,55,20)) #Top Higher Right
    draw.rect (screen, GRAY, (FX+320,310,60,20)) #Top Lower Left
    
    draw.rect (screen, GRAY, (FX+75,385,50,15)) #Bottom Lower Middle
    draw.rect (screen, GRAY, (FX+150,375,50,15)) #Bottom Lower Right
    draw.rect (screen, GRAY, (FX,360,70,18)) #Bottom Lower Left  
    draw.rect (screen, GRAY, (FX+35,337,50,15)) #Bottom Higher Left
    draw.rect (screen, GRAY, (FX+97,355,46,13)) #Bottom Higher Middle
    draw.rect (screen, GRAY, (FX+180,340,55,17)) #Bottom Higher Right     

def createChar1 (location): #Running Character ---- Distance +5
    #Variable for Collisions
    char1Nose = Rect(119,location-42,3,4) #Nose
    char1HairS = Rect(119,location-58,4,2) #Standing Hair
    char1HairON = Rect(95,location-56,28,7) #Hair on head
    char1Leg1 = draw.line (screen, DARKBLUE, (106,location-15), (121,location-4),8) #Leg 1
    char1Leg2 = draw.line (screen, DARKBLUE, (104,location-15), (90,location-4),8) #Leg 2
    char1Shoe1 = draw.line (screen, BLACK, (121,location),(124,location-6),4) #Shoe 1
    char1Shoe2 = Rect(88,location-7,3,8) #Shoe 2
    char1Jetpack = Rect(87,location-33,11,27) #Jetpack
    
    #Actual Drawing
    draw.rect (screen, SKINCOLOUR, (97,location-49,22,20)) #Face
    draw.rect (screen, SKINCOLOUR, char1Nose) #Nose
    draw.rect (screen, WHITE, (111,location-47,5,6)) #Eye
    draw.rect (screen, EYECOLOUR, (114,location-47,3,6)) #Blue Eye
    draw.rect (screen, HAIRCOLOUR, char1HairON) #Hair on head
    draw.rect (screen, HAIRCOLOUR, char1HairS) #Standing Hair
    draw.rect (screen, HAIRCOLOUR, (95,location-49,12,12)) #Back Hair    
    
    draw.rect (screen, PYJAMACOLOUR, (97,location-29,17,18)) #Body
    draw.line (screen, PYJAMACOLOUR, (113,location-23), (115,location-18),2) #Arm Cloth
    draw.rect (screen, SKINCOLOUR, (115,location-23,4,6)) #Hand
    draw.line (screen, BLACK, (97,location-29), (103,location-19),2) #Arm Line 1
    draw.line (screen, BLACK, (102,location-29), (106,location-23),2) #Arm Line 2
    draw.line (screen, BLACK, (103,location-19), (115,location-19),2) #Arm Line 1 Straight
    draw.line (screen, BLACK, (106,location-23), (115,location-23),2) #Arm Line 2 Straight
    
    draw.line (screen, PYJAMACOLOUR, (106,location-15), (121,location-4),8) #Leg 1
    draw.line (screen, PYJAMACOLOUR, (104,location-15), (90,location-4),8) #Leg 2
    
    draw.line (screen, SHOECOLOUR, (121,location),(124,location-6),4) #Shoe 1 
    draw.rect (screen, SHOECOLOUR, char1Shoe2) #Shoe 2  

    draw.line (screen, BLACK, (97,location-14), (113,location-14),1) #ShirtPant Divider
    
    draw.rect (screen, SLATE, char1Jetpack) #Jetpack  
    draw.polygon (screen, YELLOW, [(87,location-33),(92.5,location-39),(98,location-33)]) #Top
    draw.rect (screen, BLACK, (87,location-11,11,5)) #Bottom    
    
    return char1Nose, char1HairS, char1HairON, char1Leg1, char1Leg2, char1Shoe1, char1Shoe2, char1Jetpack
      
def createChar2 (location): #Bending Leg Character --- Distance +3
    #Variables
    char2Face = Rect(97,location-51,22,20) #Face
    char2Nose = Rect(119,location-44,3,4) #Nose
    char2HairS = Rect(119,location-60,4,2) #Hair Standing
    char2HairON = Rect(95,location-58,28,7) #Hair on Head
    char2Hand = Rect(115,location-25,4,6) #Hand
    char2LegU = draw.line (screen, DARKBLUE, (105,location-17),(113,location-11),8) #Leg 1 Upper
    char2LegL = draw.line (screen, DARKBLUE, (113,location-11),(105,location-6),8) #Leg 1 Lower
    char2Shoe = Rect(103,location-9,3,8) #Shoe
    char2Jetpack = Rect(87,location-36,11,27) #Jetpack
    
    #Acutual Drawing
    draw.rect (screen, SKINCOLOUR, char2Face) #Face 
    draw.rect (screen, SKINCOLOUR, char2Nose) #Nose
    draw.rect (screen, WHITE, (111,location-49,5,6)) #Eye
    draw.rect (screen, EYECOLOUR, (114,location-49,3,6)) #Blue Eye
    draw.rect (screen, HAIRCOLOUR, char2HairON) #Hair
    draw.rect (screen, HAIRCOLOUR, char2HairS) #Standing Hair
    draw.rect (screen, HAIRCOLOUR, (95,location-51,12,12)) #Back Hair    
    
    draw.rect (screen, PYJAMACOLOUR, (97,location-31,17,18)) #Body
    draw.line (screen, PYJAMACOLOUR, (113,location-25), (115,location-21),2) #Arm Cloth
    draw.rect (screen, SKINCOLOUR, char2Hand) #Hand
    draw.line (screen, BLACK, (97,location-31), (103,location-21),2) #Arm Line 1
    draw.line (screen, BLACK, (102,location-31), (106,location-25),2) #Arm Line 2
    draw.line (screen, BLACK, (103,location-21), (115,location-21),2) #Arm Line 1 Straight
    draw.line (screen, BLACK, (106,location-25), (115,location-25),2) #Arm Line 2 Straight  
    
    draw.line (screen, PYJAMACOLOUR, (105,location-17),(113,location-11),8) #Leg 1 Upper
    draw.line (screen, PYJAMACOLOUR, (113,location-11),(105,location-6),8) #Leg 1 Lower
    
    draw.rect (screen, SHOECOLOUR, char2Shoe) #Shoe
    
    draw.line (screen, BLACK, (97,location-16), (113,location-16),1) #ShirtPant Divider
    
    draw.rect (screen, SLATE, char2Jetpack) #Jetpack    
    draw.polygon (screen, YELLOW, [(87,location-36),(92.5,location-42),(98,location-36)]) #Top
    draw.rect (screen, BLACK, (87,location-14,11,5)) #Bottom    
    
    return char2Face, char2Nose, char2HairS, char2HairON, char2Hand, char2LegU, char2LegL, char2Shoe, char2Jetpack
    
def createChar3 (location): #Flying Character --- Distance +2
    #Variables
    char3Face = Rect(97,location-52,22,20) #Face
    char3Nose = Rect(119,location-45,3,4) #Nose
    char3HairS = Rect(119,location-61,4,2) #Standing Hair
    char3HairON = Rect(95,location-59,28,7) #Hair on head
    char3Hand = Rect(115,location-26,4,6) #Hand
    char3Leg = draw.polygon (screen, DARKBLUE, [(97,location-14),(112,location-14),
                                                (106,location-2),(100,location-2)]) #Legs
    char3Shoe = Rect(100,location-2,6,3) #Shoe
    char3Jetpack = Rect(87,location-38,11,27) #Jetpack   
    
    #Actual Drawing
    draw.rect (screen, SKINCOLOUR, char3Face) #Face 
    draw.rect (screen, SKINCOLOUR, char3Nose) #Nose
    draw.rect (screen, WHITE, (111,location-50,5,6)) #Eye
    draw.rect (screen, EYECOLOUR, (114,location-50,3,6)) #Blue Eye
    draw.rect (screen, HAIRCOLOUR, char3HairON) #Hair
    draw.rect (screen, HAIRCOLOUR, char3HairS) #Standing Hair
    draw.rect (screen, HAIRCOLOUR, (95,location-52,12,12)) #Back Hair    

    draw.rect (screen, PYJAMACOLOUR, (97,location-32,17,18)) #Body
    draw.line (screen, PYJAMACOLOUR, (113,location-26), (115,location-22),2) #Arm Cloth
    draw.rect (screen, SKINCOLOUR, char3Hand) #Hand
    draw.line (screen, BLACK, (97,location-32), (103,location-22),2) #Arm Line 1
    draw.line (screen, BLACK, (102,location-32), (106,location-26),2) #Arm Line 2
    draw.line (screen, BLACK, (103,location-22), (115,location-22),2) #Arm Line 1 Straight
    draw.line (screen, BLACK, (106,location-26), (115,location-26),2) #Arm Line 2 Straight  
    
    draw.polygon (screen, PYJAMACOLOUR, [(97,location-14),(112,location-14),
                                     (106,location-2),(100,location-2)]) #Legs
    
    draw.rect (screen, SHOECOLOUR, char3Shoe) #Shoe
    
    draw.line (screen, BLACK, (97,location-17), (113,location-17),1) #ShirtPant Divider 
    
    draw.rect (screen, SLATE, char3Jetpack) #Jetpack
    draw.polygon (screen, YELLOW, [(87,location-38),(92.5,location-44),(98,location-38)]) #Top
    draw.rect (screen, BLACK, (87,location-16,11,5)) #Bottom
    
    return char3Face, char3Nose, char3HairS, char3HairON, char3Hand, char3Leg, char3Shoe, char3Jetpack

def jetpackBoost(location):
    draw.rect (screen, ORANGE, (88,location-11,8,12)) #Fire/Boost
    draw.rect (screen, RED, (88,location-11,1,12)) #Red Fire 1
    draw.rect (screen, RED, (89,location-9,1,12)) #Red Fire 2
    draw.rect (screen, RED, (90,location-7,1,12)) #Red Fire 2
    draw.rect (screen, RED, (91,location-5,1,12)) #Red Fire 3
    draw.rect (screen, RED, (92,location-3,1,12)) #Red Fire 4
    draw.rect (screen, RED, (93,location-5,1,12)) #Red Fire 5
    draw.rect (screen, RED, (94,location-7,1,12)) #Red Fire 6
    draw.rect (screen, RED, (95,location-9,1,12)) #Red Fire 7
    draw.rect (screen, RED, (96,location-11,1,12)) #Red Fire 8    
    
def movingChar(): #System to slow down the leg switching of the character
    global lastTime, charSteps, charCount
    if time.get_ticks() - lastTime > charSteps: #current time - last time
        charCount += 1 #increase timer
        if charCount%5 == 0: #Every 5 multiple 
            charSteps += 170 #Slow down speed of character legs (controls them)
            
def drawCounter(): #Score
    global counter
    text = scoreCount.render("%i" %counter, 10, BLACK) 
    screen.blit(text, Rect(10,10,0,0)) #Simply put score on screen

def enemyMaker (enemiesX1,enemiesY1,enemiesX2,enemiesY2): #Enemy Control System
    global enemyCount1, enemyAS1, enemyCount2, enemyAS2, enemyNum
    
    #Enemy 1 (Tablet)
    enemyCount1 += 1 #Counter for enemies
    if enemyCount1 == enemyAS1: #if enemyCounter equals a certain number 
        enemyNum += 1 #Counter for # of enemies
        
        newEnemyX1 = 1000 #print enemy at end of screen (x)
        enemiesX1.append(newEnemyX1) #append that enemy to list
        
        newEnemyY1 = randint(20,555) #print enemy randomly on y-axis
        enemiesY1.append(newEnemyY1) #append that enemy to list
        
        enemyCount1 = 0 #Resets enemy counter  
        
        if enemyNum == 2000: 
            enemyAS1 -= 1 #increase # of enemies
            enemyNum = 0 #Resets counter
            if enemyAS1 == 5:
                enemyNum = 0 #To not overkill # of enemies
                   
        return enemiesX1, enemiesY1
    
    #Enemy 2 (CPU Case)
    enemyCount2 += 1 #Counter for enemies
    if enemyCount2 == enemyAS2: #if enemyCounter equals a certain number 
                       
        newEnemyX2 = 1200 #print enemy at end of screen (x)
        enemiesX2.append(newEnemyX2) #append that enemy to list            
        
        newEnemyY2 = randint(20,555) #print enemy randomly on y-axis
        enemiesY2.append(newEnemyY2) #append that enemy to list           
        
        enemyCount2 = 0 #Resets enemy counter   
        
        return enemiesX2,enemiesY2
    
    if enemyCount2 >= enemyAS2-100: #Alert sign    
        draw.circle (screen, YELLOW, (950,300),30) #Circle
        draw.rect (screen, RED, (945,278,10,31)) #Exclamation Mark
        draw.rect (screen, RED, (945,312,10,10)) #Dot for the Mark      
    
def moveEnemies(enemiesX1,enemiesY1,enemiesX2,enemiesY2): #Enemy movement
    global enemyWidth1, enemyWidth2, enemySpeed, enemySpeed1, enemySpeed2
    
    enemySpeed += 1 #Speed Counter for enemies
    
    #Enemy1 (Tablet)
    for enemy1 in range(len(enemiesX1) - 1, -1, -1):
        enemiesX1[enemy1] -= enemySpeed1 #move enemy across the screen       
        if enemiesX1[enemy1] < enemyWidth1: #if enemies go off screen
            del(enemiesX1[enemy1]) #removes x-value &
            del(enemiesY1[enemy1]) #removes y-value
        if enemySpeed == 1000: #If score reaches 1000
            enemySpeed1 += 1 #Enemy speed goes up by one
            enemySpeed = 0 #Resets counter
    
    #Enemy2 (CPU Case)        
    for enemy2 in range(len(enemiesX2) - 1, -1, -1):
        enemiesX2[enemy2] -= enemySpeed2 #move enemy across the screen
        if enemiesX2[enemy2] < enemyWidth2: #if enemies go off screen
            del(enemiesX2[enemy2]) #removes x-value &
            del(enemiesY2[enemy2]) #removes y-value
        if enemySpeed == 1000: #If score reaches 1000
            enemySpeed2 += 1 #Enemy speed goes up by one
            enemySpeed = 0 #Resets counter     
          
def drawEnemy(enemiesX1,enemiesY1,enemiesX2,enemiesY2,location): #Draw Enemy
    
    #Enemy1 (Tablet)    
    for count1 in range (0,len(enemiesY1)): #Goes through list and use those values for enemies
        draw.rect(screen, WHEAT, (enemiesX1[count1],enemiesY1[count1],60,50)) #Cover
        draw.rect(screen, BLACK, (enemiesX1[count1]+5,enemiesY1[count1]+5,50,40)) #Screen
        draw.rect(screen, GREEN, (enemiesX1[count1]+15,enemiesY1[count1]+13,7,7)) #Eye 1   
        draw.rect(screen, GREEN, (enemiesX1[count1]+37,enemiesY1[count1]+13,7,7)) #Eye 2
        draw.rect(screen, GREEN, (enemiesX1[count1]+20,enemiesY1[count1]+28,20,5)) #Mouth
        draw.rect(screen, GREEN, (enemiesX1[count1]+13,enemiesY1[count1]+33,7,5)) #Sad Face 1
        draw.rect(screen, GREEN, (enemiesX1[count1]+40,enemiesY1[count1]+33,7,5)) #Sad Face 2        
              
    #Enemy2 (CPU Case)
    for count2 in range (0,len(enemiesY2)): #Goes through list and use those values for enemies      
        draw.rect (screen, BLACK, (enemiesX2[count2],enemiesY2[count2],120,60)) #CPU Box 
        draw.rect (screen, LIGHTGRAY, (enemiesX2[count2],enemiesY2[count2],120,60),3) #Frame
        draw.line (screen, DARKGRAY, (enemiesX2[count2]+20,enemiesY2[count2]+3), 
                   (enemiesX2[count2]+20,enemiesY2[count2]+57),2) #Line 1
        draw.line (screen, DARKGRAY, (enemiesX2[count2]+40,enemiesY2[count2]+3), 
                   (enemiesX2[count2]+40,enemiesY2[count2]+57),2) #Line 2
        draw.line (screen, DARKGRAY, (enemiesX2[count2]+60,enemiesY2[count2]+3), 
                   (enemiesX2[count2]+60,enemiesY2[count2]+57),2) #Line 3
        draw.rect (screen, LIGHTGRAY, (enemiesX2[count2]+70,enemiesY2[count2]+12,20,36)) #White - HD
        draw.rect (screen, DARKGRAY, (enemiesX2[count2]+70,enemiesY2[count2]+12,10,36),2) #HD 1
        draw.rect (screen, DARKGRAY, (enemiesX2[count2]+80,enemiesY2[count2]+12,10,36),2) #HD 2
        draw.circle (screen, DARKGRAY, (enemiesX2[count2]+105,enemiesY2[count2]+30),7) #Power Button Border
        draw.circle (screen, LIGHTGRAY, (enemiesX2[count2]+105,enemiesY2[count2]+30),5) #Power Button 
                  
                                    
def enemyCollide1 (enemiesX1, enemiesY1, enemiesX2, enemiesY2, location): #Collision with Character 1
    char1Nose, char1HairS, char1HairON, char1Leg1, char1Leg2, char1Shoe1, char1Shoe2, char1Jetpack = createChar1 (location)
    
    #Enemy 1 Collisions w/ Character 1
    for count1 in range (0,len(enemiesY1)):   
        enemyRect1 = Rect(enemiesX1[count1],enemiesY1[count1],60,50)   
        
        #Character parts being checked for collisions          
        if enemyRect1.colliderect (char1Nose): #Enemy collide w/ nose
            return False #Returning False to end game
        if enemyRect1.colliderect (char1HairS): #Enemy collide w/ Hair(Standing)
            return False
        if enemyRect1.colliderect (char1HairON): #Enemy collide w/ Hair(on head)
            return False     
        if enemyRect1.colliderect (char1Leg1): #Enemy collide w/ Leg 1
            return False
        if enemyRect1.colliderect (char1Leg2): #Enemy collide w/ Leg 2
            return False        
        if enemyRect1.colliderect (char1Shoe1): #Enemy collide w/ Shoe 1
            return False  
        if enemyRect1.colliderect (char1Shoe2): #Enemy collide w/ Shoe 2
            return False    
        if enemyRect1.colliderect (char1Jetpack): #Enemy collide w/ Jetpack
            return False   
        
    #Enemy 2 Collisions w/ Character 1
    for count2 in range (0,len(enemiesY2)):   
        enemyRect2 = Rect(enemiesX2[count2],enemiesY2[count2],120,60)  
        
        #Character parts being checked for collisions
        if enemyRect2.colliderect (char1Nose): #Enemy collide w/ nose
            return False #Returning False to end game
        if enemyRect2.colliderect (char1HairS): #Enemy collide w/ Hair(Standing)
            return False
        if enemyRect2.colliderect (char1HairON): #Enemy collide w/ Hair(on head)
            return False     
        if enemyRect2.colliderect (char1Leg1): #Enemy collide w/ Leg 1
            return False
        if enemyRect2.colliderect (char1Leg2): #Enemy collide w/ Leg 2
            return False        
        if enemyRect2.colliderect (char1Shoe1): #Enemy collide w/ Shoe 1
            return False  
        if enemyRect2.colliderect (char1Shoe2): #Enemy collide w/ Shoe 2
            return False    
        if enemyRect2.colliderect (char1Jetpack): #Enemy collide w/ Jetpack
            return False    
       
def enemyCollide2 (enemiesX1, enemiesY1, enemiesX2, enemiesY2, location): #Collision with Character 2  
    char2Face, char2Nose, char2HairS, char2HairON, char2Hand, char2LegU, char2LegL, char2Shoe, char2Jetpack = createChar2 (location)    
    
    #Enemy 1 Collisions w/ Character 2
    for count1 in range (0,len(enemiesY1)):   
        enemyRect1 = Rect(enemiesX1[count1],enemiesY1[count1],60,50) 
        
        #Character parts being checked for collisions
        if enemyRect1.colliderect (char2Face): #Enemy collide w/ face
            return False #Returning False to end game
        if enemyRect1.colliderect (char2Nose): #Enemy collide w/ nose
            return False
        if enemyRect1.colliderect (char2HairS): #Enemy collide w/ Hair(Standing)
            return False
        if enemyRect1.colliderect (char2HairON): #Enemy collide w/ Hair(on head)
            return False     
        if enemyRect1.colliderect (char2Hand): #Enemy collide w/ Hand
            return False            
        if enemyRect1.colliderect (char2LegU): #Enemy collide w/ Upper Leg
            return False
        if enemyRect1.colliderect (char2LegL): #Enemy collide w/ Lower Leg
            return False        
        if enemyRect1.colliderect (char2Shoe): #Enemy collide w/ Shoe
            return False  
        if enemyRect1.colliderect (char2Jetpack): #Enemy collide w/ Jetpack
            return False  
        
    #Enemy 2 Collisions w/ Character 2
    for count2 in range (0,len(enemiesY2)):   
        enemyRect2 = Rect(enemiesX2[count2],enemiesY2[count2],120,60)  
        
        #Character parts being checked for collisions
        if enemyRect2.colliderect (char2Face): #Enemy collide w/ face
            return False #Returning False to end game
        if enemyRect2.colliderect (char2Nose): #Enemy collide w/ nose
            return False
        if enemyRect2.colliderect (char2HairS): #Enemy collide w/ Hair(Standing)
            return False
        if enemyRect2.colliderect (char2HairON): #Enemy collide w/ Hair(on head)
            return False     
        if enemyRect2.colliderect (char2Hand): #Enemy collide w/ Hand
            return False            
        if enemyRect2.colliderect (char2LegU): #Enemy collide w/ Upper Leg
            return False
        if enemyRect2.colliderect (char2LegL): #Enemy collide w/ Lower Leg
            return False        
        if enemyRect2.colliderect (char2Shoe): #Enemy collide w/ Shoe
            return False  
        if enemyRect2.colliderect (char2Jetpack): #Enemy collide w/ Jetpack
            return False  
         
        
def enemyCollide3 (enemiesX1, enemiesY1, enemiesX2, enemiesY2, location): #Collision with Character 3     
    char3Face, char3Nose, char3HairS, char3HairON, char3Hand, char3Leg, char3Shoe, char3Jetpack = createChar3 (location)    
    
    #Enemy 1 Collisions w/ Character 3
    for count1 in range (0,len(enemiesY1)):   
        enemyRect1 = Rect(enemiesX1[count1],enemiesY1[count1],60,50) 
        
        #Character parts being checked for collisions
        if enemyRect1.colliderect (char3Face): #Enemy collide w/ face
            return False #Returning False to end game
        if enemyRect1.colliderect (char3Nose): #Enemy collide w/ nose
            return False
        if enemyRect1.colliderect (char3HairS): #Enemy collide w/ Hair(Standing)
            return False
        if enemyRect1.colliderect (char3HairON): #Enemy collide w/ Hair(on head)
            return False     
        if enemyRect1.colliderect (char3Hand): #Enemy collide w/ Hand
            return False            
        if enemyRect1.colliderect (char3Leg): #Enemy collide w/ Leg
            return False         
        if enemyRect1.colliderect (char3Shoe): #Enemy collide w/ Shoe
            return False  
        if enemyRect1.colliderect (char3Jetpack): #Enemy collide w/ Jetpack
            return False 
        
    #Enemy 2 Collisions w/ Character 3
    for count2 in range (0,len(enemiesY2)):   
        enemyRect2 = Rect(enemiesX2[count2],enemiesY2[count2],120,60) 
        
        #Character parts being checked for collisions
        if enemyRect2.colliderect (char3Face): #Enemy collide w/ face
            return False #Returning False to end game
        if enemyRect2.colliderect (char3Nose): #Enemy collide w/ nose
            return False
        if enemyRect2.colliderect (char3HairS): #Enemy collide w/ Hair(Standing)
            return False
        if enemyRect2.colliderect (char3HairON): #Enemy collide w/ Hair(on head)
            return False     
        if enemyRect2.colliderect (char3Hand): #Enemy collide w/ Hand
            return False            
        if enemyRect2.colliderect (char3Leg): #Enemy collide w/ Leg
            return False         
        if enemyRect2.colliderect (char3Shoe): #Enemy collide w/ Shoe
            return False  
        if enemyRect2.colliderect (char3Jetpack): #Enemy collide w/ Jetpack
            return False                  

def powerUpMaker (powerUpX1,powerUpY1,powerUpX2,powerUpY2): #Power-Up Control System
    global powerupCount1, powerupAS1, powerupCount2, powerupAS2
    
    #Power-Up 1 (Speed Power-Up)
    powerupCount1 += 1 #Counter for power-ups

    if powerupCount1 == powerupAS1: #if powerup counter equals a certain #
        
        newPowerUpX1 = 1000 #print power-up at end of screen (x)
        powerUpX1.append(newPowerUpX1) #append that power-up to list
        
        newPowerUpY1 = randint(20,555) #print power-up randomly on y-axis
        powerUpY1.append(newPowerUpY1) #append that enemy to list
        
        powerupCount1 = 0 #Resets enemy counter  
                   
        return powerUpX1, powerUpY1
    
    #Power-Up 2 (Gun Power-Up)
    powerupCount2 += 1 #Counter for power-ups

    if powerupCount2 == powerupAS2: #if powerup counter equals a certain #
        
        newPowerUpX2 = 1000 #print power-up at end of screen (x)
        powerUpX2.append(newPowerUpX2) #append that power-up to list
        
        newPowerUpY2 = randint(20,555) #print power-up randomly on y-axis
        powerUpY2.append(newPowerUpY2) #append that enemy to list
        
        powerupCount2 = 0 #Resets enemy counter  
                   
        return powerUpX2, powerUpY2 
    
def movePowerUps(powerUpX1,powerUpY1,powerUpX2,powerUpY2): #Power-Up movement
    global powerupWidth
    
    #PowerUp1 (Speed)
    for powerup1 in range(len(powerUpX1) - 1, -1, -1):
        powerUpX1[powerup1] -= 7 #move power-up across the screen       
        if powerUpX1[powerup1] < powerupWidth: #if power-up go off screen
            del(powerUpX1[powerup1]) #removes x-value &
            del(powerUpY1[powerup1]) #removes y-value
            
    #PowerUp2 (Gun)
    for powerup2 in range(len(powerUpX2) - 1, -1, -1):
        powerUpX2[powerup2] -= 7 #move power-up across the screen       
        if powerUpX2[powerup2] < powerupWidth: #if power-up go off screen
            del(powerUpX2[powerup2]) #removes x-value &
            del(powerUpY2[powerup2]) #removes y-value    
            
def drawPowerup(powerUpX1,powerUpY1,powerUpX2,powerUpY2,location): #Draw Power-Ups 
    
    #PowerUp1 (Speed)    
    for count1 in range (0,len(powerUpY1)): #Goes through list and use those values 
        draw.rect (screen, GREEN, (powerUpX1[count1],powerUpY1[count1],70,50)) #Green Rect
        draw.rect (screen, BROWN, (powerUpX1[count1],powerUpY1[count1],70,50),3) #Brown Border
        draw.rect (screen, YELLOW, (powerUpX1[count1]+30,powerUpY1[count1]+10,10,30)) #Speed Plus Sign 1
        draw.rect (screen, YELLOW, (powerUpX1[count1]+20,powerUpY1[count1]+20,30,10)) #Speed Plus Sign 2 
        
    #PowerUp2 (Gun)    
    for count2 in range (0,len(powerUpY2)): #Goes through list and use those values 
        draw.rect (screen, RED, (powerUpX2[count2],powerUpY2[count2],70,50)) #Red Rect
        draw.rect (screen, BROWN, (powerUpX2[count2],powerUpY2[count2],70,50),3) #Brown Border
        draw.rect (screen, YELLOW, (powerUpX2[count2]+25,powerUpY2[count2]+22,20,6)) #Bullet
        
def powerup1Collide1 (powerUpX1,powerUpY1,location): #Collision with Character 1
    char1Nose, char1HairS, char1HairON, char1Leg1, char1Leg2, char1Shoe1, char1Shoe2, char1Jetpack = createChar1(location)
    
    #Power-Up 1 Collisions w/ Character 1
    for count1 in range (0,len(powerUpY1)):   
        powerupRect1 = Rect(powerUpX1[count1],powerUpY1[count1],70,50)   
        
        #Character parts being checked for collisions          
        if powerupRect1.colliderect (char1Nose): #Power-Up collide w/ nose
            return False #Returning False to confirm collision
        if powerupRect1.colliderect (char1HairS): #Power-Up collide w/ Hair(Standing)
            return False
        if powerupRect1.colliderect (char1HairON): #Power-Up collide w/ Hair(on head)
            return False     
        if powerupRect1.colliderect (char1Leg1): #Power-Up collide w/ Leg 1
            return False
        if powerupRect1.colliderect (char1Leg2): #Power-Up collide w/ Leg 2
            return False        
        if powerupRect1.colliderect (char1Shoe1): #Power-Up collide w/ Shoe 1
            return False  
        if powerupRect1.colliderect (char1Shoe2): #Power-Up collide w/ Shoe 2
            return False    
        if powerupRect1.colliderect (char1Jetpack): #Power-Up collide w/ Jetpack
            return False  
              
def powerup2Collide1 (powerUpX2,powerUpY2,location): #Collision with Character 1
    char1Nose, char1HairS, char1HairON, char1Leg1, char1Leg2, char1Shoe1, char1Shoe2, char1Jetpack = createChar1(location)
          
    #Power-Up 2 Collisions w/ Character 1
    for count2 in range (0,len(powerUpY2)):   
        powerupRect2 = Rect(powerUpX2[count2],powerUpY2[count2],70,50)   
        
        #Character parts being checked for collisions          
        if powerupRect2.colliderect (char1Nose): #Power-Up collide w/ nose
            return False #Returning False to confirm collision
        if powerupRect2.colliderect (char1HairS): #Power-Up collide w/ Hair(Standing)
            return False
        if powerupRect2.colliderect (char1HairON): #Power-Up collide w/ Hair(on head)
            return False     
        if powerupRect2.colliderect (char1Leg1): #Power-Up collide w/ Leg 1
            return False
        if powerupRect2.colliderect (char1Leg2): #Power-Up collide w/ Leg 2
            return False        
        if powerupRect2.colliderect (char1Shoe1): #Power-Up collide w/ Shoe 1
            return False  
        if powerupRect2.colliderect (char1Shoe2): #Power-Up collide w/ Shoe 2
            return False    
        if powerupRect2.colliderect (char1Jetpack): #Power-Up collide w/ Jetpack
            return False   
          
def powerup1Collide2 (powerUpX1,powerUpY1,location): #Collision with Character 2  
    char2Face, char2Nose, char2HairS, char2HairON, char2Hand, char2LegU, char2LegL, char2Shoe, char2Jetpack = createChar2(location)    
    
    #Power-Up 1 Collisions w/ Character 2
    for count1 in range (0,len(powerUpY1)):   
        powerupRect1 = Rect(powerUpX1[count1],powerUpY1[count1],70,50) 
        
        #Character parts being checked for collisions
        if powerupRect1.colliderect (char2Face): #Power-Up collide w/ face
            return False #Returning False to confirm collision
        if powerupRect1.colliderect (char2Nose): #Power-Up collide w/ nose
            return False
        if powerupRect1.colliderect (char2HairS): #Power-Up collide w/ Hair(Standing)
            return False
        if powerupRect1.colliderect (char2HairON): #Power-Up collide w/ Hair(on head)
            return False     
        if powerupRect1.colliderect (char2Hand): #Power-Up collide w/ Hand
            return False            
        if powerupRect1.colliderect (char2LegU): #Power-Up collide w/ Upper Leg
            return False
        if powerupRect1.colliderect (char2LegL): #Power-Up collide w/ Lower Leg
            return False        
        if powerupRect1.colliderect (char2Shoe): #Power-Up collide w/ Shoe
            return False  
        if powerupRect1.colliderect (char2Jetpack): #Power-Up collide w/ Jetpack
            return False
        
def powerup2Collide2 (powerUpX2,powerUpY2,location): #Collision with Character 2  
    char2Face, char2Nose, char2HairS, char2HairON, char2Hand, char2LegU, char2LegL, char2Shoe, char2Jetpack = createChar2(location)    
    
    #Power-Up 2 Collisions w/ Character 2
    for count2 in range (0,len(powerUpY2)):   
        powerupRect2 = Rect(powerUpX2[count2],powerUpY2[count2],70,50) 
        
        #Character parts being checked for collisions
        if powerupRect2.colliderect (char2Face): #Power-Up collide w/ face
            return False #Returning False to confirm collision
        if powerupRect2.colliderect (char2Nose): #Power-Up collide w/ nose
            return False
        if powerupRect2.colliderect (char2HairS): #Power-Up collide w/ Hair(Standing)
            return False
        if powerupRect2.colliderect (char2HairON): #Power-Up collide w/ Hair(on head)
            return False     
        if powerupRect2.colliderect (char2Hand): #Power-Up collide w/ Hand
            return False            
        if powerupRect2.colliderect (char2LegU): #Power-Up collide w/ Upper Leg
            return False
        if powerupRect2.colliderect (char2LegL): #Power-Up collide w/ Lower Leg
            return False        
        if powerupRect2.colliderect (char2Shoe): #Power-Up collide w/ Shoe
            return False  
        if powerupRect2.colliderect (char2Jetpack): #Power-Up collide w/ Jetpack
            return False    
                    
def powerup1Collide3 (powerUpX1,powerUpY1,location): #Collision with Character 3     
    char3Face, char3Nose, char3HairS, char3HairON, char3Hand, char3Leg, char3Shoe, char3Jetpack = createChar3(location)    
    
    #Power-Up 1 Collisions w/ Character 3
    for count1 in range (0,len(powerUpY1)):   
        powerupRect1 = Rect(powerUpX1[count1],powerUpY1[count1],70,50) 
        
        #Character parts being checked for collisions
        if powerupRect1.colliderect (char3Face): #Power-Up collide w/ face
            return False #Returning False to confirm collision
        if powerupRect1.colliderect (char3Nose): #Power-Up collide w/ nose
            return False
        if powerupRect1.colliderect (char3HairS): #Power-Up collide w/ Hair(Standing)
            return False
        if powerupRect1.colliderect (char3HairON): #Power-Up collide w/ Hair(on head)
            return False     
        if powerupRect1.colliderect (char3Hand): #Power-Up collide w/ Hand
            return False            
        if powerupRect1.colliderect (char3Leg): #Power-Up collide w/ Leg
            return False         
        if powerupRect1.colliderect (char3Shoe): #Power-Up collide w/ Shoe
            return False  
        if powerupRect1.colliderect (char3Jetpack): #Power-Up collide w/ Jetpack
            return False 
        
def powerup2Collide3 (powerUpX2,powerUpY2,location): #Collision with Character 3     
    char3Face, char3Nose, char3HairS, char3HairON, char3Hand, char3Leg, char3Shoe, char3Jetpack = createChar3(location)    
        
    #Power-Up 2 Collisions w/ Character 3
    for count2 in range (0,len(powerUpY2)):   #collideList
        powerupRect2 = Rect(powerUpX2[count2],powerUpY2[count2],70,50) 
        
        #Character parts being checked for collisions
        if powerupRect2.colliderect (char3Face): #Power-Up collide w/ face
            return False #Returning False to confirm collision
        if powerupRect2.colliderect (char3Nose): #Power-Up collide w/ nose
            return False
        if powerupRect2.colliderect (char3HairS): #Power-Up collide w/ Hair(Standing)
            return False
        if powerupRect2.colliderect (char3HairON): #Power-Up collide w/ Hair(on head)
            return False     
        if powerupRect2.colliderect (char3Hand): #Power-Up collide w/ Hand
            return False            
        if powerupRect2.colliderect (char3Leg): #Power-Up collide w/ Leg
            return False         
        if powerupRect2.colliderect (char3Shoe): #Power-Up collide w/ Shoe
            return False  
        if powerupRect2.colliderect (char3Jetpack): #Power-Up collide w/ Jetpack
            return False     
                
def moveBullets(bulletsX,bulletsY):
    for index in range(len(bulletsX) - 1, -1, -1):
        bulletsX[index] += 5 # will move the bullets right
        if bulletsX[index] > width: # if gone off the horizon, remove
            del(bulletsX[index]) #x-value
            del(bulletsY[index]) #y-value

def drawBullets(bulletsX,bulletsY):
    for bullet in range (0,len(bulletsY)): #Draws the bullets
        draw.rect(screen, YELLOW, (bulletsX[bullet],bulletsY[bullet],20,6))
        
def bulletCollide (enemiesX1,enemiesY1,enemiesX2,enemiesY2,bulletsX,bulletsY,location): #Collision with Enemies         

    #Making enemy1 list
    enemy1Rects = []
    for count in range(0, len(enemiesX1)):
        enemyRect1 = Rect(enemiesX1[count],enemiesY1[count],60,50)
        enemy1Rects.append(enemyRect1)
             
    #Power-Up 2 (Bullets) Collisions w/ Enemies
    for count in range (len(bulletsY)-1, -1, -1): #collideList
        bulletRect = Rect(bulletsX[count],bulletsY[count],20,6) #Bullet Rect
        hit = bulletRect.collidelist(enemy1Rects)  #Checking through all enemy rectangles
        if hit != -1:
            #If hit,...
            del(enemiesX1[hit]) #remove enemy
            del(enemiesY1[hit])
            del(bulletsX[count]) #remove bullets
            del(bulletsY[count])  

def mainScreen (button,mouseX,mouseY): #Main Menu
    state = MAINSTATE
    
    #Buttons
    playButton = Rect(375,300,250,250) #Play Button
    customButton = Rect(150,350,150,150) #Customization Button
    instructButton = Rect(700,350,150,150) #Instruction Button   
    
    #Main Screen Options
    textTitle1 = fontTitle.render("E-Waste", 20, GREEN) 
    screen.blit(textTitle1, Rect(345,70,0,0)) #First word of title
    textTitle2 = fontTitle.render("Apocalypse", 20, RED) 
    screen.blit(textTitle2, Rect(260,170,0,0)) #Second word of title
    
    draw.rect (screen, LIME, playButton) #Play Button
    draw.rect (screen, MAROON, playButton,5) #Play Border   
    draw.rect (screen, GREEN, customButton) #Cutomization Button
    draw.rect (screen, MAROON, customButton,5) #Cutomization Border
    draw.rect (screen, GREEN, instructButton) #Instruction Button
    draw.rect (screen, MAROON, instructButton,5) #Instruction Border
    
    draw.polygon (screen, BLACK, [(475,380),(475,460),(540,420)]) #Play Button Tri
    
    draw.rect (screen, YELLOW, (180,380,90,90)) #Custom Face
    draw.rect (screen, BLACK, (195,400,20,20)) #Eye 1
    draw.rect (screen, BLACK, (235,400,20,20)) #Eye 2
    draw.rect (screen, BLACK, (235,400,20,20)) #Eye 2
    draw.rect (screen, BLACK, (200,440,50,10)) #Mouth
    
    draw.rect (screen, YELLOW, (735,375,80,100)) #Instruction book
    draw.rect (screen, BLACK, (765,420,20,40)) #i
    draw.circle(screen,BLACK, (775,400),10) #dot for i
     
    #Collisions w/ buttons 
    if button == 1:
        if playButton.collidepoint (mouseX,mouseY): #Play Button
            state = GAMESTATE #Plays Game
        elif customButton.collidepoint (mouseX,mouseY): #Custom Button
            state = CUSTOMSTATE #Customize Character
        elif instructButton.collidepoint (mouseX,mouseY): #Instruction Button
            state = INSTRUCTSTATE #Instructions
     
    return state

def instructionMenu (button, mouseX, mouseY): #Instruction/Story Menu
    state = INSTRUCTSTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button
    controlButton = Rect(825,590,135,40) #Controls Button
    powerUpButton = Rect(650,590,155,40) #Power-Ups Button
    
    draw.rect (screen, LIME, (20,20,960,660)) #Background
    draw.rect (screen, BROWN, (20,20,960,660),5) #Background Border 
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen, BLACK, controlButton) #Controls Button
    ControlSign = fontSigns.render("Controls", 20, WHITE) 
    screen.blit(ControlSign, Rect(832,597,0,0)) #Control Text       
    
    draw.rect (screen, BLACK, powerUpButton) #Power-Up Button
    ControlSign = fontSigns.render("Power-Ups", 20, WHITE) 
    screen.blit(ControlSign, Rect(660,597,0,0)) #Power-up Text        
    
    instructTitle = fontNormal.render("Welcome to the Electronic Waste Apocalypse!", 20, RED) 
    screen.blit(instructTitle, Rect(50,120,0,0)) #Title for Instructions     
    Instruct1 = fontInstruct.render("While sleeping in my brand new pyjamas, I did not realize that the end of our world had come.", 20, BLACK) 
    screen.blit(Instruct1, Rect(50,200,0,0)) #Instructions 1 
    Instruct2 = fontInstruct.render("I barely managed to get out of bed and escape the apocalypse.", 20, BLACK) 
    screen.blit(Instruct2, Rect(50,240,0,0)) #Instructions 2   
    Instruct3 = fontInstruct.render("We, humans, have long misused our wonderful planet by disposing electronic waste incorrectly.", 20, BLACK) 
    screen.blit(Instruct3, Rect(50,280,0,0)) #Instructions 3     
    Instruct4 = fontInstruct.render("Now, the time has come for us to pay back for our mistake.", 20, BLACK) 
    screen.blit(Instruct4, Rect(50,320,0,0)) #Instructions 4
    Instruct5 = fontInstruct.render("So, you'll be playing as me, a completely ordinary person, except the fact that I have a jetpack.", 20, BLACK) 
    screen.blit(Instruct5, Rect(50,400,0,0)) #Instructions 5
    Instruct6 = fontInstruct.render("Why, you ask. I don't really know, I just kind of had one laying around...", 20, BLACK) 
    screen.blit(Instruct6, Rect(50,440,0,0)) #Instructions 6 
    Instruct7 = fontInstruct.render("Our goal is to withstand the apocalypse as long as we can.", 20, BLACK) 
    screen.blit(Instruct7, Rect(50,480,0,0)) #Instructions 7
    Instruct8 = fontInstruct.render("You also might want to keep in mind that I don't want to get my brand new pyjamas dirty.", 20, BLACK) 
    screen.blit(Instruct8, Rect(50,520,0,0)) #Instructions 7 
    Instruct9 = fontNormal.render("HAVE FUN!", 20, RED) 
    screen.blit(Instruct9, Rect(50,600,0,0)) #Instructions 7       
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint (mouseX,mouseY): #Back Button
            state = MAINSTATE #Back to Main Menu
        elif controlButton.collidepoint (mouseX, mouseY): #Control Button
            state = CONTROLSTATE #Explains controls
        elif powerUpButton.collidepoint (mouseX, mouseY): #Power-Up Button
            state = POWERUPSTATE #Explain power-ups
      
    return state

def customChar ():
    #Character Display (Bigger Version)
    draw.rect (screen, SKINCOLOUR, (700,230,100,98)) #Face
    draw.rect (screen, SKINCOLOUR, (800,270,10,14)) #Nose
    draw.rect (screen, WHITE, (765,240,20,28)) #Eye
    draw.rect (screen, EYECOLOUR, (775,240,10,28)) #Blue Eye
    draw.rect (screen, HAIRCOLOUR, (690,213,130,17)) #Hair on head
    draw.rect (screen, HAIRCOLOUR, (800,200,20,13)) #Standing Hair
    draw.rect (screen, HAIRCOLOUR, (690,230,55,65)) #Back Hair    
    
    draw.line (screen, PYJAMACOLOUR, (744,410), (833,500),56) #Leg 1
    draw.line (screen, PYJAMACOLOUR, (750,410), (650,480),50) #Leg 2    
    
    draw.rect (screen, PYJAMACOLOUR, (700,328,88,98)) #Body
    draw.line (screen, PYJAMACOLOUR, (788,375), (800,375),20) #Arm Cloth
    draw.rect (screen, SKINCOLOUR, (800,365,10,20)) #Hand
    draw.line (screen, BLACK, (700,328), (735,385),5) #Arm Line 1
    draw.line (screen, BLACK, (720,328), (745,365),5) #Arm Line 2
    draw.line (screen, BLACK, (735,385), (800,385),5) #Arm Line 1 Straight
    draw.line (screen, BLACK, (745,365), (800,365),5) #Arm Line 2 Straight
    
    #draw.rect (screen, BLACK, (807,500,55,15))
    draw.line (screen, GRAY, (800,510),(855,485),15) #Cover up 
    draw.rect (screen, GRAY, (830,490,32,15)) #Cover up
    draw.line (screen, SHOECOLOUR, (806,507),(850,480),17) #Shoe 1
    draw.rect (screen, SHOECOLOUR, (635,455,15,50)) #Shoe 2       

    draw.line (screen, BLACK, (700,420), (787,420),5) #ShirtPant Divider
    
    draw.rect (screen, SLATE, (660,324,40,100)) #Jetpack  
    draw.polygon (screen, YELLOW, [(660,324),(680,300),(700,324)]) #Top
    draw.rect (screen, BLACK, (660,424,40,15)) #Bottom  

def customMenu (button,mouseX,mouseY):
    state = CUSTOMSTATE
       
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button 
    skinButton = Rect(100,40,300,100) #Skin Button
    eyeButton = Rect(100,170,300,100) #Eye Button
    hairButton = Rect(100,300,300,100) #Hair Button
    pyjamaButton = Rect(100,430,300,100) #Pyjamas Button
    shoeButton = Rect(100,560,300,100) #Shoe Button
    
    draw.rect (screen, LIME, (0,0,width/2,height)) #Green Background
    draw.rect (screen, GRAY, (width/2,height/height,width/2,height)) #Gray Background
    draw.rect (screen, GREY, (550,550,400,5)) #Gray Line
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen, PURPLE, skinButton) #Skin Box
    SkinSign = fontCustoms.render("Skin", 20, WHITE) 
    screen.blit(SkinSign, Rect(188,60,0,0)) #Text  
    
    draw.rect (screen, PURPLE, eyeButton) #Eye Colour Box
    EyeSign = fontCustoms.render("Eye", 20, WHITE) 
    screen.blit(EyeSign, Rect(200,191,0,0)) #Text  
    
    draw.rect (screen, PURPLE, hairButton) #Hair Box
    HairSign = fontCustoms.render("Hair", 20, WHITE) 
    screen.blit(HairSign, Rect(185,322,0,0)) #Text  
    
    draw.rect (screen, PURPLE, pyjamaButton) #Pyjamas Box
    PyjamasSign = fontCustoms.render("Pyjama", 20, WHITE) 
    screen.blit(PyjamasSign, Rect(145,452,0,0)) #Text  
    
    draw.rect (screen, PURPLE, shoeButton) #Shoes Box
    ShoeSign = fontCustoms.render("Shoe", 20, WHITE) 
    screen.blit(ShoeSign, Rect(177,580,0,0)) #Text  
           
    customChar() #Character Display (Bigger Version)
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint(mouseX,mouseY): #Back Button
            state = MAINSTATE #Back to Main Menu    
        elif skinButton.collidepoint (mouseX,mouseY): #Skin Button
            state = SKINSTATE #Skin Customization
        elif eyeButton.collidepoint(mouseX,mouseY): #Eye Button
            state = EYESTATE #Eye Customization
        elif hairButton.collidepoint(mouseX,mouseY): #Hair Button
            state = HAIRSTATE #Hair Customization
        elif pyjamaButton.collidepoint(mouseX,mouseY): #Pyjama Button
            state = PYJAMASTATE #Pyjama Customization
        elif shoeButton.collidepoint(mouseX,mouseY): #Shoe Button
            state = SHOESTATE #Shoe Customization
            
    return state

def skinMenu (button,mouseX,mouseY):
    global SKINCOLOUR
    state = SKINSTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button 
    skinColour = Rect(200,100,100,100) #Skin Colour Button
    peruColour = Rect(200,300,100,100) #Peru Colour Button
    darkbrownColour = Rect(200,500,100,100) #Maroon Colour Button
    
    draw.rect (screen, LIME, (0,0,width/2,height)) #Green Background
    draw.rect (screen, GRAY, (width/2,height/height,width/2,height)) #Gray Background
    draw.rect (screen, GREY, (550,550,400,5)) #Grey Line

    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen,SKIN,skinColour) #Light Skin      
    draw.rect (screen,PERU,peruColour) #Brown Skin
    draw.rect (screen,DARKBROWN,darkbrownColour) #Dark Skin      
    
    #Collisions
    if skinColour.collidepoint (mouseX,mouseY): #Collide with skin colour
        SKINCOLOUR = SKIN
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,SKIN,skinColour) #Light Skin
        draw.rect (screen,WHITE,skinColour,3) #White Border      
        draw.rect (screen,PERU,peruColour) #Brown Skin
        draw.rect (screen,DARKBROWN,darkbrownColour) #Dark Skin 
        
    if peruColour.collidepoint (mouseX,mouseY): #Collide with peru colour
        SKINCOLOUR = PERU
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,SKIN,skinColour) #Light Skin   
        draw.rect (screen,PERU,peruColour) #Brown Skin
        draw.rect (screen,WHITE,peruColour,3) #White Border   
        draw.rect (screen,DARKBROWN,darkbrownColour) #Dark Skin  
        
    if darkbrownColour.collidepoint (mouseX,mouseY): #Collide with darkbrown colour
        SKINCOLOUR = DARKBROWN
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,SKIN,skinColour) #Light Skin   
        draw.rect (screen,PERU,peruColour) #Brown Skin  
        draw.rect (screen,DARKBROWN,darkbrownColour) #Dark Skin  
        draw.rect (screen,WHITE,darkbrownColour,3) #White Border 
              
    customChar() #Character Display (Bigger Version)
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint(mouseX,mouseY): #Back Button
            state = CUSTOMSTATE #Back to customization options  
            
    return state

def eyeMenu (button,mouseX,mouseY):
    global EYECOLOUR
    state = EYESTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button 
    blueColour = Rect(200,100,100,100) #Blue Eye Colour Button
    blackColour = Rect(200,300,100,100) #Black Eye Colour Button
    greenColour = Rect(200,500,100,100) #Green Eye Colour Button    
    
    draw.rect (screen, LIME, (0,0,width/2,height)) #Green Background
    draw.rect (screen, GRAY, (width/2,height/height,width/2,height)) #Gray Background
    draw.rect (screen, GREY, (550,550,400,5)) #Grey Line
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen,BLUE,blueColour) #Blue Eye Colour     
    draw.rect (screen,BLACK,blackColour) #Black Eye Colour 
    draw.rect (screen,GREEN,greenColour) #Green Eye Colour 
    
    #Collisions
    if blueColour.collidepoint (mouseX,mouseY): #Collide with blue colour
        EYECOLOUR = BLUE
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BLUE,blueColour) #Blue Eye Colour 
        draw.rect (screen,WHITE,blueColour,3) #White Border
        draw.rect (screen,BLACK,blackColour) #Black Eye Colour 
        draw.rect (screen,GREEN,greenColour) #Green Eye Colour 
        
    if blackColour.collidepoint (mouseX,mouseY): #Collide with black colour
        EYECOLOUR = BLACK
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BLUE,blueColour) #Blue Eye Colour 
        draw.rect (screen,BLACK,blackColour) #Black Eye Colour 
        draw.rect (screen,WHITE,blackColour,3) #White Border
        draw.rect (screen,GREEN,greenColour) #Green Eye Colour   
        
    if greenColour.collidepoint (mouseX,mouseY): #Collide with green colour
        EYECOLOUR = GREEN
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BLUE,blueColour) #Blue Eye Colour 
        draw.rect (screen,BLACK,blackColour) #Black Eye Colour 
        draw.rect (screen,GREEN,greenColour) #Green Eye Colour 
        draw.rect (screen,WHITE,greenColour,3) #White Border
            
    customChar() #Character Display (Bigger Version)
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint(mouseX,mouseY): #Back Button
            state = CUSTOMSTATE #Back to customization options    
            
    return state

def hairMenu (button,mouseX,mouseY):
    global HAIRCOLOUR
    state = HAIRSTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button 
    brownColour = Rect(200,100,100,100) #Brown Colour Button
    blackColour = Rect(200,300,100,100) #Black Colour Button
    yellowColour = Rect(200,500,100,100) #Yellow Colour Button    
    
    draw.rect (screen, LIME, (0,0,width/2,height)) #Green Background
    draw.rect (screen, GRAY, (width/2,height/height,width/2,height)) #Gray Background
    draw.rect (screen, GREY, (550,550,400,5)) #Grey Line
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen,BROWN,brownColour) #Brown Colour     
    draw.rect (screen,BLACK,blackColour) #Black Colour 
    draw.rect (screen,YELLOW,yellowColour) #Yellow Colour 
    
    #Collisions
    if brownColour.collidepoint (mouseX,mouseY): #Collide with brown colour
        HAIRCOLOUR = BROWN
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BROWN,brownColour) #Brown Colour   
        draw.rect (screen,WHITE,brownColour,3) #White border
        draw.rect (screen,BLACK,blackColour) #Black Colour 
        draw.rect (screen,YELLOW,yellowColour) #Yellow Colour
        
    if blackColour.collidepoint (mouseX,mouseY): #Collide with black colour
        HAIRCOLOUR = BLACK
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BROWN,brownColour) #Brown Colour   
        draw.rect (screen,BLACK,blackColour) #Black Colour 
        draw.rect (screen,WHITE,blackColour,3) #White Border
        draw.rect (screen,YELLOW,yellowColour) #Yellow Colour 
        
    if yellowColour.collidepoint (mouseX,mouseY): #Collide with yellow colour
        HAIRCOLOUR = YELLOW
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BROWN,brownColour) #Brown Colour   
        draw.rect (screen,BLACK,blackColour) #Black Colour 
        draw.rect (screen,YELLOW,yellowColour) #Yellow Colour 
        draw.rect (screen,WHITE,yellowColour,3) #White Border    
    
    customChar() #Character Display (Bigger Version)
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint(mouseX,mouseY): #Back Button
            state = CUSTOMSTATE #Back to customization options   
            
    return state

def pyjamaMenu (button,mouseX,mouseY):
    global PYJAMACOLOUR
    state = PYJAMASTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button
    blueColour = Rect(200,100,100,100) #Blue Colour Button
    greenColour = Rect(200,300,100,100) #Green Colour Button
    orangeColour = Rect(200,500,100,100) #Orange Colour Button        
    
    draw.rect (screen, LIME, (0,0,width/2,height)) #Green Background
    draw.rect (screen, GRAY, (width/2,height/height,width/2,height)) #Gray Background
    draw.rect (screen, GREY, (550,550,400,5)) #Grey Line
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen,DARKBLUE,blueColour) #Blue Colour     
    draw.rect (screen,GREEN,greenColour) #Green Colour 
    draw.rect (screen,ORANGE,orangeColour) #Orange Colour  
    
    #Collisions
    if blueColour.collidepoint (mouseX,mouseY): #Collide with blue colour
        PYJAMACOLOUR = DARKBLUE
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,DARKBLUE,blueColour) #Blue Colour 
        draw.rect (screen,WHITE,blueColour,3) #White Border
        draw.rect (screen,GREEN,greenColour) #Green Colour 
        draw.rect (screen,ORANGE,orangeColour) #Orange Colour
        
    if greenColour.collidepoint (mouseX,mouseY): #Collide with green colour
        PYJAMACOLOUR = GREEN
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,DARKBLUE,blueColour) #Blue Colour 
        draw.rect (screen,GREEN,greenColour) #Green Colour 
        draw.rect (screen,WHITE,greenColour,3) #White Border
        draw.rect (screen,ORANGE,orangeColour) #Orange Colour
        
    if orangeColour.collidepoint (mouseX,mouseY): #Collide with orange colour
        PYJAMACOLOUR = ORANGE
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,DARKBLUE,blueColour) #Blue Colour 
        draw.rect (screen,GREEN,greenColour) #Green Colour 
        draw.rect (screen,ORANGE,orangeColour) #Orange Colour  
        draw.rect (screen,WHITE,orangeColour,3) #White Border
            
    customChar() #Character Display (Bigger Version)
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint(mouseX,mouseY): #Back Button
            state = CUSTOMSTATE #Back to customization options     
            
    return state

def shoeMenu (button,mouseX,mouseY):
    global SHOECOLOUR
    state = SHOESTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button 
    blackColour = Rect(200,100,100,100) #Black Colour Button
    brownColour = Rect(200,300,100,100) #Brown Colour Button
    purpleColour = Rect(200,500,100,100) #Purple Colour Button       
    
    draw.rect (screen, LIME, (0,0,width/2,height)) #Green Background
    draw.rect (screen, GRAY, (width/2,height/height,width/2,height)) #Gray Background
    draw.rect (screen, GREY, (550,550,400,5)) #Grey Line
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen,BLACK,blackColour) #Black Colour     
    draw.rect (screen,BROWN,brownColour) #Brown Colour 
    draw.rect (screen,PURPLE,purpleColour) #Purple Colour  
    
    #Collisions
    if blackColour.collidepoint (mouseX,mouseY): #Collide with black colour
        SHOECOLOUR = BLACK
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BLACK,blackColour) #Black Colour
        draw.rect (screen,WHITE,blackColour,3) #White Border
        draw.rect (screen,BROWN,brownColour) #Brown Colour 
        draw.rect (screen,PURPLE,purpleColour) #Purple Colour  
        
    if brownColour.collidepoint (mouseX,mouseY): #Collide with brown colour
        SHOECOLOUR = BROWN
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BLACK,blackColour) #Black Colour
        draw.rect (screen,BROWN,brownColour) #Brown Colour 
        draw.rect (screen,WHITE,brownColour,3) #White Border
        draw.rect (screen,PURPLE,purpleColour) #Purple Colour  
        
    if purpleColour.collidepoint (mouseX,mouseY): #Collide with purple colour
        SHOECOLOUR = PURPLE
        draw.rect (screen,LIME,(0,0,width/2,height)) #Green Background       
        draw.rect (screen,BLACK,blackColour) #Black Colour
        draw.rect (screen,BROWN,brownColour) #Brown Colour 
        draw.rect (screen,PURPLE,purpleColour) #Purple Colour  
        draw.rect (screen,WHITE,purpleColour,3) #White Border
            
    customChar() #Character Display (Bigger Version)
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint(mouseX,mouseY): #Back Button
            state = CUSTOMSTATE #Back to customization options    
            
    return state

def controlMenu (button, mouseX, mouseY): #Controls Menu
    state = CONTROLSTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button
    storyButton = Rect(825,590,135,40) #Instruction/Story Button
    powerUpButton = Rect(650,590,155,40) #Power-Up Button      
    
    draw.rect (screen, LIME, (20,20,960,660)) #Background
    draw.rect (screen, BROWN, (20,20,960,660),5) #Background Border
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text   
    
    draw.rect (screen, BLACK, storyButton) #Instruction/Story Button
    ControlSign = fontSigns.render("Story", 20, WHITE) 
    screen.blit(ControlSign, Rect(853,597,0,0)) #Instruction/Story Text       
    
    draw.rect (screen, BLACK, powerUpButton) #Power-Up Button
    ControlSign = fontSigns.render("Power-Ups", 20, WHITE) 
    screen.blit(ControlSign, Rect(660,597,0,0)) #Power-up Text  
    
    textControlTitle = fontCustoms.render("Controls", 20, BLACK) 
    screen.blit(textControlTitle, Rect(365,70,0,0)) #Spacebar Text    
    
    draw.rect (screen, BLACK, (275,180,450,80),5) #Space Bar
    textSpacebar = fontNormal.render("SPACE BAR", 20, BLACK) 
    screen.blit(textSpacebar, Rect(417,203,0,0)) #Spacebar Text
    
    spaceControls = fontNormal.render("Hold to fly up & Release to fly down", 20, RED) 
    screen.blit(spaceControls, Rect(190,280,0,0)) #Power-up Text
    
    draw.rect (screen, BLACK, (150,380,180,180),5) #Right Key Box
    textKeyRight1 = fontNormal.render("Right", 20, BLACK) 
    textKeyRight2 = fontNormal.render("Key", 20, BLACK) 
    screen.blit(textKeyRight1, Rect(195,435,0,0)) #Right Key Text
    screen.blit(textKeyRight2, Rect(210,475,0,0)) #Right Key Text
    
    keyControls = fontNormal.render("Press right key to shoot", 20, RED) 
    screen.blit(keyControls, Rect(380,460,0,0)) #Right Key Text 
    warningControls = fontSigns.render("Only when activated though...", 20, BLACK) 
    screen.blit(warningControls, Rect(395,510,0,0)) #Letting you know text       
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint (mouseX,mouseY): #Back Button
            state = MAINSTATE #Back to Main Menu
        elif storyButton.collidepoint (mouseX, mouseY): #Story Button
            state = INSTRUCTSTATE #Explains instructions/story
        elif powerUpButton.collidepoint (mouseX, mouseY): #Power-Up Button
            state = POWERUPSTATE #Explains power-ups       

    return state    
    
def controlGO (button, mouseX, mouseY): #Controls Menu
    state = CONTROLGO
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button
    storyButton = Rect(825,590,135,40) #Instruction/Story Button
    powerUpButton = Rect(650,590,155,40) #Power-Up Button      
    
    draw.rect (screen, LIME, (20,20,960,660)) #Background
    draw.rect (screen, BROWN, (20,20,960,660),5) #Background Border
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text   
       
    textControlTitle = fontCustoms.render("Controls", 20, BLACK) 
    screen.blit(textControlTitle, Rect(365,70,0,0)) #Spacebar Text    
    
    draw.rect (screen, BLACK, (275,180,450,80),5) #Space Bar
    textSpacebar = fontNormal.render("SPACE BAR", 20, BLACK) 
    screen.blit(textSpacebar, Rect(417,203,0,0)) #Spacebar Text
    
    spaceControls = fontNormal.render("Hold to fly up & Release to fly down", 20, RED) 
    screen.blit(spaceControls, Rect(190,280,0,0)) #Power-up Text
    
    draw.rect (screen, BLACK, (150,380,180,180),5) #Right Key Box
    textKeyRight1 = fontNormal.render("Right", 20, BLACK) 
    textKeyRight2 = fontNormal.render("Key", 20, BLACK) 
    screen.blit(textKeyRight1, Rect(195,435,0,0)) #Right Key Text
    screen.blit(textKeyRight2, Rect(210,475,0,0)) #Right Key Text
    
    keyControls = fontNormal.render("Press right key to shoot", 20, RED) 
    screen.blit(keyControls, Rect(380,460,0,0)) #Right Key Text 
    warningControls = fontSigns.render("Only when activated though...", 20, BLACK) 
    screen.blit(warningControls, Rect(395,510,0,0)) #Letting you know text       
    
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint (mouseX,mouseY): #Back Button
            state = GOSTATE #Back to Main Menu 
        
    return state
    
def powerupMenu (button, mouseX, mouseY): #Power-Up Menu
    state = POWERUPSTATE
    
    #Buttons
    backButton = Rect(850,40,110,40) #Back Button
    controlButton = Rect(825,590,135,40) #Control Button
    storyButton = Rect(650,590,155,40) #Instruction/Story Button       
    
    draw.rect (screen, LIME, (20,20,960,660)) #Background
    draw.rect (screen, BROWN, (20,20,960,660),5) #Background Border 
    
    draw.rect (screen, BLACK, backButton) #Back Button
    BackSign = fontSigns.render("Back", 20, WHITE) 
    screen.blit(BackSign, Rect(874,48,0,0)) #Back Text 
    
    draw.rect (screen, BLACK, controlButton) #Controls Button
    ControlSign = fontSigns.render("Controls", 20, WHITE) 
    screen.blit(ControlSign, Rect(832,597,0,0)) #Control Text       
    
    draw.rect (screen, BLACK, storyButton) #Instruction/Story Button
    ControlSign = fontSigns.render("Story", 20, WHITE) 
    screen.blit(ControlSign, Rect(690,597,0,0)) #Instruction/Story Text 
    
    powerupTitle = fontCustoms.render("Power Ups", 20, RED) 
    screen.blit(powerupTitle, Rect(350,70,0,0)) #Instruction/Story Text     
    
    #Speed Power-Up
    draw.rect (screen, GREEN, (100,160,250,180)) #Green Rect
    draw.rect (screen, BROWN, (100,160,250,180),3) #Brown Border
    draw.rect (screen, YELLOW, (205,180,40,140)) #Speed Plus Sign 1
    draw.rect (screen, YELLOW, (150,230,150,40)) #Speed Plus Sign 2
    
    #Speed Power-Up Text
    powerup1Instruct1 = fontInstruct.render("This power-up speeds me up significantly.", 20, BLACK) 
    screen.blit(powerup1Instruct1, Rect(360,175,0,0)) #Power-Up 1 Explanation      
    powerup1Instruct2 = fontInstruct.render("This increase of speed helps me get past the enemies quickly.", 20, BLACK) 
    screen.blit(powerup1Instruct2, Rect(360,215,0,0)) #Power-Up 1 Explanation  
    powerup1Instruct3 = fontInstruct.render("However, the sudden increase in speed might make me go crazy.", 20, BLACK) 
    screen.blit(powerup1Instruct3, Rect(360,255,0,0)) #Power-Up 1 Explanation   
    powerup1Instruct4 = fontInstruct.render("You need to have some pretty great skills to use this professionally!", 20, BLACK) 
    screen.blit(powerup1Instruct4, Rect(360,295,0,0)) #Power-Up 1 Explanation         
    
    #Gun Power-Up
    draw.rect (screen, RED, (100,390,250,180)) #Red Rect
    draw.rect (screen, BROWN, (100,390,250,180),3) #Brown Rect
    draw.rect (screen, YELLOW, (190,470,70,20)) #Bullet
    
    #Gun Power-Up Text
    powerup1Instruct1 = fontInstruct.render("The Vaporizing Electronic Waste Gun.", 20, DARKBLUE) 
    screen.blit(powerup1Instruct1, Rect(360,410,0,0)) #Power-Up 1 Explanation      
    powerup1Instruct2 = fontInstruct.render("The Power-Up that lets me shoot bullets out my hand!", 20, BLACK) 
    screen.blit(powerup1Instruct2, Rect(360,450,0,0)) #Power-Up 1 Explanation  
    powerup1Instruct3 = fontInstruct.render("Don't get too use to the privelegde though.", 20, BLACK) 
    screen.blit(powerup1Instruct3, Rect(360,490,0,0)) #Power-Up 1 Explanation   
    powerup1Instruct4 = fontInstruct.render("These bullets don't work on the special enemy...", 20, BLACK) 
    screen.blit(powerup1Instruct4, Rect(360,530,0,0)) #Power-Up 1 Explanation     
   
    #Collisions w/ buttons
    if button == 1:
        if backButton.collidepoint (mouseX,mouseY): #Back Button
            state = MAINSTATE #Back to Main Menu
        elif controlButton.collidepoint (mouseX, mouseY): #Control Button
            state = CONTROLSTATE #Explains controls
        elif storyButton.collidepoint (mouseX, mouseY): #Story Button
            state = INSTRUCTSTATE #Explain instructions/story     

    return state     
            
def playAgain (button,mouseX,mouseY,Counter): #Game Over Menu
    state = GOSTATE
       
    #Buttons
    MMButton = Rect(250,370,130,100)
    playAgainButton = Rect(435,370,130,100)
    controlGOButton = Rect(620,370,130,100)
    
    draw.rect (screen, BLACK, (0,0,width,height)) #Background
    draw.rect (screen, LIME, (200,180,600,340)) #Game Over Box
    draw.rect (screen, GREEN, (200,180,600,340),15) #Game Over Border
    draw.rect (screen, YELLOW, MMButton) #Main Menu Button
    draw.rect (screen, YELLOW, playAgainButton) #Play Again Button
    draw.rect (screen, YELLOW, controlGOButton) #Controls Button

    textScore = fontCustoms.render("Score: %i" %Counter, 20, WHITE) 
    screen.blit(textScore, Rect(340,280,0,0)) #Score for the game
    
    highScoreFile = open("highScore.dat", "r") #Reading from highscore file
    highscore = highScoreFile.readline() #Read the highscore saved
    highscore = highscore.rstrip("\n")  #Remove new line character
    counterList.append(Counter) #Append score gotten in game to list
    counterList.append(int(highscore)) #Append the highscore saved
    counterList.sort() #Check whether highscore was beaten or not
    highScore = counterList[-1] #Last number is the greatest
    del counterList[0:-1] #Deletes rest from the list
    highScoreFile.close() #To prevent crashing
    
    highScoreFile = open("highScore.dat", "w") #Meant for if highscore was beaten
    highScoreFile.write(str(highScore) + "\n") #Writing it into file
    highScoreFile.close() #To prevent crashing
    
    textHighScore = fontNormal.render("HighScore: %i" %highScore, 20, RED)
    screen.blit(textHighScore, Rect(350,220,0,0)) #HighScore
    
    draw.rect (screen, BLACK, (295,383,70,20)) #Rect 1 (MM)
    draw.circle(screen, BLACK, (273,393),9) #Circle 1 (MM)
    draw.rect (screen, BLACK, (295,410,70,20)) #Rect 2 (MM)
    draw.circle(screen, BLACK, (273,420),9) #Circle 2 (MM)
    draw.rect (screen, BLACK, (295,437,70,20)) #Rect 3 (MM)
    draw.circle(screen, BLACK, (273,447),9) #Circle 3 (MM)
    
    draw.polygon (screen, BLACK, [(470,380),(470,460),(535,420)]) #Play Button Tri
    
    draw.rect (screen, BLACK, (670,380,30,80)) #Rect 1 (Controller)
    draw.rect (screen, BLACK, (645,405,80,30)) #Rect 2 (Controller)
    draw.polygon (screen, WHITE, [(685,387),(678,398),(692,398)]) #Tri1(Controller)
    draw.polygon (screen, WHITE, [(685,453),(678,442),(692,442)]) #Tri2(Controller)
    draw.polygon (screen, WHITE, [(718,420),(707,413),(707,427)]) #Tri3(Controller)
    draw.polygon (screen, WHITE, [(652,420),(663,413),(663,427)]) #Tri2(Controller)

    #Setting up states 
    if button == 1: #If mouse clicked
        if playAgainButton.collidepoint(mouseX,mouseY):
            state = GAMESTATE #Back into game
        elif MMButton.collidepoint(mouseX,mouseY):
            state = MAINSTATE #Back to Main Menu
        elif controlGOButton.collidepoint(mouseX,mouseY):
            state = CONTROLGO #To controls menu
            
    return state    

State = MAINSTATE #Default state    
button = mx = my = 0 #Value of buttons & mouses

mixer.music.play(-1) #Plays music
                               
running = True #Keeps program running

while running:
    
    button = 0 #So that it doesn't affect other states
       
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False #Quits programs if you click X
        
        #Creating the mouse      
        if evnt.type == MOUSEBUTTONDOWN: #check if mouse button is pushed            
            mx, my = evnt.pos #saves position         
            button = evnt.button #checks for button pushed or not        
        
        #Moving character up
        if evnt.type == KEYDOWN:   
            if evnt.key == K_SPACE:
                KEY_SPACE = True #Pressing the space key 
                
            if evnt.key == K_RIGHT: #For bullets
                keys = key.get_pressed() #So that you can't hold
                if keys[K_RIGHT]:
                    newBullet = 119 #x-value
                    newplayerY = playerY-23 #y-value
                    bulletList.append(newBullet) #List to keep track    
                    playerYList.append(newplayerY) #of bullets
                
        #Moving character down
        if evnt.type == KEYUP:   
            if evnt.key == K_SPACE:
                KEY_SPACE = False #Releasing the space key             
    
    #Moving character up
    if KEY_SPACE == True:
        playerY = playerY - playerSpeed     
        
        #If player reaches top of the screen
        if playerY <= topScreen:
            playerY = topScreen #Can't go further up
        
    #Moving character down
    if KEY_SPACE == False:
        playerY = playerY + playerSpeed
        
        #If player reaches platform
        if playerY >= platformY: 
            playerY = platformY #Can't go further down
    
    #Background                  
    drawBG (cloudX,cloudY,factoryX) 
    cloudX -= 2 #Moves cloud (side-scrolling effect)
    factoryX -= 4 #Moves factory (side-scrolling effect)
    
    #To make cloud reappear 
    if cloudX + 445 < 0:
        cloudX = 1000
        cloudY = randint (20,50)
    
    #To make factory reappear
    if factoryX + 1000 < 0:
        factoryX = 1000 
    
    #Checking for States
    if State == MAINSTATE:
        State = mainScreen (button,mx,my) #Main Menu
        
    elif State == INSTRUCTSTATE: 
        State = instructionMenu(button,mx,my) #Instruction/Story Menu
        
    elif State == CONTROLSTATE:
        State = controlMenu (button,mx,my) #Controls Menu
    
    elif State == CONTROLGO:
        State = controlGO (button,mx,my) #Game Over Controls Menu
        
    elif State == POWERUPSTATE:
        State = powerupMenu (button,mx,my) #Power-Up Info Menu
        
    elif State == CUSTOMSTATE:
        State = customMenu (button,mx,my) #Customization Menu
        
    elif State == SKINSTATE:
        State = skinMenu (button,mx,my) #Skin Customization Menu
        
    elif State == EYESTATE:
        State = eyeMenu (button,mx,my) #Eye Customization Menu
        
    elif State == HAIRSTATE:
        State = hairMenu (button,mx,my) #Hair Customization Menu
        
    elif State == PYJAMASTATE:
        State = pyjamaMenu (button,mx,my) #Pyjama Customization Menu
        
    elif State == SHOESTATE:
        State = shoeMenu (button,mx,my) #Shoe Customization Menu
        
    elif State == GAMESTATE: #Playing Game     
        #Enemies
        enemyMaker (enemyListX1, enemyListY1, enemyListX2, enemyListY2) #Repeat enemies & controls speed/AS
        moveEnemies(enemyListX1, enemyListY1, enemyListX2, enemyListY2) #Movement of enemies 
        drawEnemy (enemyListX1, enemyListY1, enemyListX2, enemyListY2, playerY) #Draws enemy  
        
        #Power-Ups
        powerUpMaker (powerupListX1,powerupListY1,powerupListX2,powerupListY2) #Repeat power-ups & controls speed/AS
        movePowerUps(powerupListX1, powerupListY1,powerupListX2,powerupListY2) #Movement of power-ups
        drawPowerup(powerupListX1,powerupListY1,powerupListX2,powerupListY2,playerY) #Draws power-ups
                      
        #Character        
        movingChar() #Slows down the running effect
        bulletCollide (enemyListX1,enemyListY1,enemyListX2,enemyListY2,bulletList,playerYList,playerY) 
        #Bullet Collision w/ enemies
        
        #To make running effect    
        if charCount%2 == 0: #Even & Odd (so back and forth spontaneously)
            charPos = True 
        else:
            charPos = False
        
        if playerY == platformY:
            if charPos == True:
                createChar1(playerY) #Character (running)    
                if enemyCollide1 (enemyListX1,enemyListY1,enemyListX2,enemyListY2,playerY) == False:
                    State = GOSTATE #Character 2 w/ enemy collisions
                    
                if powerup1Collide1 (powerupListX1,powerupListY1,playerY) == False:
                    speedUse = True #Character 1 w/ power-up 1 collisions
                    del (powerupListX1[0]) #Delete power-up
                    del (powerupListY1[0]) #Making it look like you picked it up
                    
                if powerup2Collide1 (powerupListX2,powerupListY2,playerY) == False:
                    bulletUse = True #Character 1 w/ power-up 2 collisions
                    del (powerupListX2[0]) #Delete power-up
                    del (powerupListY2[0]) #Making it look like you picked it up        
            else:
                createChar2(playerY) #Character (bent)
                if enemyCollide2 (enemyListX1,enemyListY1,enemyListX2,enemyListY2,playerY) == False:
                    State = GOSTATE #Character 2 w/ enemy collisions 
                    
                if powerup1Collide2 (powerupListX1,powerupListY1,playerY) == False:
                    speedUse = True #Character 2 w/ power-up 1 collisions
                    del (powerupListX1[0]) #Delete power-up
                    del (powerupListY1[0]) #Making it look like you picked it up                
                    
                if powerup2Collide2 (powerupListX2,powerupListY2,playerY) == False:
                    bulletUse = True  #Character 2 w/ power-up 2 collisions
                    del (powerupListX2[0]) #Delete power-up
                    del (powerupListY2[0]) #Making it look like you picked it up 
                    
        elif playerY <= platformY:
            createChar3(playerY) #Character (flying)
            if enemyCollide3 (enemyListX1,enemyListY1,enemyListX2,enemyListY2,playerY) == False:
                State = GOSTATE #Character 3 w/ enemy collisions
                
            if powerup1Collide3 (powerupListX1,powerupListY1,playerY) == False:
                speedUse = True #Character 3 w/ power-up 1 collisions
                del (powerupListX1[0]) #Delete power-up
                del (powerupListY1[0]) #Making it look like you picked it up            
                
            if powerup2Collide3 (powerupListX2,powerupListY2,playerY) == False:
                bulletUse = True  #Character 2 w/ power-up 2 collisions
                del (powerupListX2[0]) #Delete power-up
                del (powerupListY2[0]) #Making it look like you picked it up 
           
        #To make boost appear only when flying up
        if KEY_SPACE == True:
            jetpackBoost(playerY)
        
        if speedUse == True: #if collide w/ power-up 1
            playerSpeed = 10 #New character speed
            speedTimer += 1 #Duration of power-up
            powerupCount1 = powerupAS2+1 #Stops more power-up 1 from appearing
    
            if speedTimer == speedDuration: #if timer reaches certain #
                speedUse = False #Power-Up 1 deactivates
                playerSpeed = 5 #Back to normal speed
                powerupCount1 = 0 #To make power-up 1 appear again        
                speedTimer = 0 #Reseting counter        
        
        #Bullet Use
        if bulletUse == False: #delets any bullets created during false phase
            del (bulletList[0:])
            del (playerYList[0:])     
            
        if bulletUse == True:
            moveBullets (bulletList,playerYList) #Moving bullets
            drawBullets (bulletList,playerYList) #Drawing bullets
            bulletTimer += 1 #Duration of power-up
            powerupCount2 = powerupAS2+1 #Stops more power-up 2 from appearing
            
            if bulletTimer == bulletDuration: #if timer reaches certain #
                bulletUse = False #Power-Up 2 deactivates
                powerupCount2 = 0 #To make power-up 2 appear again
                bulletTimer = 0 #Resets timer
                del (bulletList[0:]) #Deletes any remaining bullets
                del (playerYList[0:])            
                                               
        drawCounter() #Score Count    
        counter += 1 #Moving the score up
        realCounter = counter
    
    elif State == GOSTATE: #Game Over Menu
        State = playAgain (button,mx,my,realCounter)
        
        #Reseting all variables
        counter = 0 #Main score conter
        playerY = height//1.14 #y position of character
        enemyAS1 = 10 #Enemy1 Speed
        enemySpeed1 = 12 #For the speed of enemies appearing
        enemySpeed2 = 19 #For the speed of enemies appearing
        enemyCount2 = 0 #Enemy2 counter
        powerupCount1 = 0 #PowerUp1 counter
        powerupCount2 = 0 #PowerUp2 counter  
        
        del (enemyListX1[0:]) #delete all enemy 1s
        del (enemyListY1[0:])
        del (enemyListX2[0:]) #delete all enemy 2s
        del (enemyListY2[0:])        
        del (powerupListX1[0:]) #deletes powerups1
        del (powerupListY1[0:]) 
        del (powerupListX2[0:]) #deletes powerups2
        del (powerupListY2[0:]) 
        
        speedUse = False #Power-Up 1 deactivates
        playerSpeed = 5 #Back to normal speed
        powerupCount1 = 0 #To make power-up 1 appear again        
        speedTimer = 0 #Reseting counter  
        bulletUse = False #Power-Up 2 deactivates
        powerupCount2 = 0 #To make power-up 2 appear again
        bulletTimer = 0 #Resets timer
        del (bulletList[0:]) #Deletes any remaining bullets
        del (playerYList[0:])         
              
    display.flip()
    myClock.tick(FPS) #Clock speed
    
quit()

        
        