from guizero import *

#if the images look small on whatever device you are viewing my code on, the full size pictures would not fit on my laptop screen.
#open original size infographic.gif to see the full sized image

#variable for password check
passcount = 0

def infographicwindow():
    '''function for window with infographic'''
    def questionwindow():
        '''function for window with the questions'''
        def awardwindow(window3textbox1, window3textbox2, window3textbox3):
            '''function for window if the user got most (or not a lot of) questions correct'''
            answer1 = window3textbox1.value
            answer2 = window3textbox2.value
            answer3 = window3textbox3.value
            name = window1input1.value
            answercount = 0
            #Sees how many of the questions the user answered correctly
            if answer1.lower == "2 billion" or answer1.lower == "two billion" or answer1 == "2,000,000,000" or answer1 == "2000000000" or answer1 == "2 000 000 000":
                answercount += 1
            if answer2 == "9" or answer2.lower == "nine":
                answercount += 1
            if answer3 == "1" or answer3.lower == "one":
                answercount += 1
            #if user answers 2 or more answers correctly
            if answercount >= 1:
                window3.hide()
                window4 = Window(window1, title="You Won!",width=550,height=500)
                window4text1 = Text(window4, text="\nYou got two or more questions correct!")
                window4picture1 = Picture(window4, image="award.gif")
                window4text2 = Text(window4, text="Congratulations")
                window4text3 = Text(window4, text=name)
            #if user enters 1 or less answers correctly
            else:
                window3.hide()
                window4 = Window(window1, title="You Lost!",width=500,height=125)
                window4text1 = Text(window4, text="\nYou Failed!\n")
                window4text2 = Text(window4, text="You got one or less questions correct.")
                window4text4 = Text(window4, text="Try again.")
        #window for the questions
        window2.hide()
        window3 = Window(window1, title="Questions", width=700,height=350)
        window3text1 = Text(window3, text="\nHow many people don't have access to waste collection services?\n")
        window3textbox1 = TextBox(window3, width = 10)
        window3text2 = Text(window3, text="\nOut of 10, how many urban residents breathe polluted air?\n")
        window3textbox2 = TextBox(window3, width = 10)
        window3text3 = Text(window3, text="\nOut of 4, how many urban residents live in slum-like conditions?\n")
        window3textbox3 = TextBox(window3, width = 10)
        spacing = Text(window3, text=" ")
        window3buttion1 = PushButton(window3, text = "Enter", command=awardwindow, args=[window3textbox1, window3textbox2, window3textbox3])     
    #window for the infographic
    window1.hide()
    window2 = Window(window1, title="Infographic", width=400,height=650)
    window2text1 = Text(window2, text="Analyze this infographic.")
    window2picture1 = Picture(window2, image="infographic.gif")
    window2text2 = Text(window2, text="\nReady to answer the question?\n")
    window2button1 = PushButton(window2, text="Yes", command=questionwindow)

def nameNumCheck(window1input1):
    '''Checks for numbers in name'''
    for character in window1input1:
        if not character.isdecimal():
            return True
        else:
            error = info(title="Error", text="Name contains numbers") 
                
def nameCapitalCheck(window1input1):
    '''Checks for a capital letter'''
    if window1input1.istitle():
        return True
    else:
        error = info(title="Error", text="Invalid name")
        
def namecheck(window1input1):
    '''Base name checking function'''
    nameCheck1 = nameNumCheck(window1input1)
    nameCheck2 = nameCapitalCheck(window1input1)
    if nameCheck1 == True and nameCheck2 == True:
        return True
            
def nameNumCheck(window1input1):
    '''Checks if the user put numbers in the name'''
    for character in window1input1:
        if not character.isdecimal():
            return True
        else:
            error = info(title="Error", text="Name contains numbers") 
        
def nameCapitalCheck(window1input1):
    '''Checks if there are capitals in the password'''
    if window1input1.istitle():
        return True
    else:
        error = info(title="Error", text="Invalid name")

def namecheck(window1input1):
    '''base name checker'''
    nameCheck1 = nameNumCheck(window1input1)
    nameCheck2 = nameCapitalCheck(window1input1)
    
    if nameCheck1 == True and nameCheck2 == True:
        return True
    
def passworduppercheck(window1input2):
    '''checks if password contains any uppercase letters'''
    uppercount = 0
    for character in window1input2:
        if character.isupper():
            uppercount += 1
            if uppercount >= 1:
                return True
            else:
                return False

def passwordnumcheck(window1input2):
    '''checks if password contains any numbers'''
    numcount = 0
    for character in window1input2:
        if character.isdecimal():
            numcount += 1
            if numcount <=2:
                return True
            else:
                return False

def passwordlencheck(window1input2):
    '''checks if password is long enough'''
    if len(window1input2) >=6:
        return True
    else:
        return False
            
def passwordcheck(window1input2):
    '''checks if the password that the user entered is valid'''
    global passcount
    check1 = passwordlencheck(window1input2)
    check2 = passwordnumcheck(window1input2)
    check3 = passworduppercheck(window1input2)
    
    if check1 == True and check2 == True and check3 == True:
        return True
    else:
        error = info(title="Invalid", text ="You have entered an invalid password.\n\nThe passworld should be at least six characters long, and include two numbers and one uppercase letter.")
        passcount += 1
        if passcount == 3:
            end = warn(title = "Error", text = "You have entered the password incorrectly too many times. Please try again.")
            window1.destroy()


def button1(window1input1,window1input2):
    '''function for the button in the first window'''
    window1input1 = window1input1.value
    window1input2 = window1input2.value
    if namecheck(window1input1) == True:
        if passwordcheck(window1input2) == True:
            infographicwindow()



#base window
window1 = App(title="Log In", width=300,height=250)
window1text1 = Text(window1, text="\nEnter your full name.\n")
window1input1 = TextBox(window1, width=20)
window1text2 = Text(window1, text="\nEnter the password to continue.\n")
window1input2 = TextBox(window1, width=20)
spacing = Text(window1, text=" ")
window1button1 = PushButton(window1, text = "Enter", command=button1, args=[window1input1,window1input2])
window1.display()