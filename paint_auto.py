import pyautogui

import time

pyautogui.moveTo(233, 749, 2) # move to search bar
time.sleep(1)
pyautogui.click()
time.sleep(1)

pyautogui.typewrite("paint", interval = 0.4) #Search "paint"
time.sleep(1)

pyautogui.moveTo(192, 202, duration = 2) #move to paint
time.sleep(1)
pyautogui.click()

time.sleep(2)
pyautogui.moveTo(674, 107, duration = 2) #go to brush size
time.sleep(1)
pyautogui.click()

time.sleep(1)
pyautogui.moveTo(709, 256, duration = 1) #select brush size
time.sleep(1)
pyautogui.click()

#1st Draw

time.sleep(1)
pyautogui.moveTo(227, 244, duration = 1)
time.sleep(2)

distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, 0.5) # Move Right
    distance = distance - 25
    pyautogui.dragRel(0, distance, 0.5) # Move Down
    pyautogui.dragRel(-distance, 0, 0.5) # Move Left
    distance = distance - 25
    pyautogui.dragRel(0, -distance, 0.5) #Move Up


time.sleep(1)
pyautogui.moveTo(871, 96, duration = 2) #select red color
time.sleep(1)
pyautogui.click()

#2nc Draw

time.sleep(1)
pyautogui.moveTo(494, 244, duration = 1) #start a new drawing
time.sleep(1)

distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, 0.5) # Move Right
    distance = distance - 25
    pyautogui.dragRel(0, distance, 0.5) # Move Down
    pyautogui.dragRel(-distance, 0, 0.5) # Move Left
    distance = distance - 25
    pyautogui.dragRel(0, -distance, 0.5) #Move Up


time.sleep(1)
pyautogui.moveTo(933, 93, duration = 2) #select green color
time.sleep(1)
pyautogui.click()

#3rd Draw

time.sleep(1)
pyautogui.moveTo(769, 244, duration = 1) #start a new drawing
time.sleep(1)

distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, 0.5) # Move Right
    distance = distance - 25
    pyautogui.dragRel(0, distance, 0.5) # Move Down
    pyautogui.dragRel(-distance, 0, 0.5) # Move Left
    distance = distance - 25
    pyautogui.dragRel(0, -distance, 0.5) #Move Up


#Thank You For Watching

time.sleep(1)
pyautogui.moveTo(233, 749, 2) # move to search bar
time.sleep(1)
pyautogui.click()
time.sleep(1)

pyautogui.typewrite("word", interval = 0.4) #Search "word"
time.sleep(1)

pyautogui.moveTo(192, 202, duration = 2) #move to word 2013
time.sleep(1)
pyautogui.click()

time.sleep(5)
pyautogui.moveTo(485, 232, duration = 2)
time.sleep(1)
pyautogui.click() # open blank document

time.sleep(1)
pyautogui.moveTo(293, 74, duration = 2)
time.sleep(1)
pyautogui.click() # select font size

time.sleep(1)
pyautogui.moveTo(273, 360, duration = 2)
time.sleep(1)
pyautogui.click() # select font size

time.sleep(1)
pyautogui.moveTo(471, 368, duration = 1)
time.sleep(1)
pyautogui.click() # Select the word area

time.sleep(1)
pyautogui.typewrite("Thank You", interval = 0.2)
pyautogui.typewrite(["enter"], interval = 0.3)
pyautogui.typewrite(["enter"], interval = 0.3)
time.sleep(1)
pyautogui.typewrite("#Let's_Connect", interval = 0.2)
