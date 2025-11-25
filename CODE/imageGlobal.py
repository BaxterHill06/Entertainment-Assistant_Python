from tkinter import *
def GlobalImageFile(selMovie):
    global imgShrek, imgRiseOfTheGuardians, imgShrek2, imgShrektheThird, imgTheWizardofOz, imgJourneyBacktoOz, imgOzTheGreatandPowerful, imgReturntoOz, imgBacktotheFuture, imgBacktotheFuturePartII, imgBacktotheFuturePartIII, imgJourneytotheCenteroftheEarth, imgJourney2TheMysteriousIsland, imgHalloween, imgHalloweenII, imgHalloweenIIISeasonoftheWitch, imgHalloween4TheReturnofMichaelMyers, imgHalloween5TheRevengeofMichaelMyers, imgHalloweenTheCurseofMichaelMyers, imgHalloweenH2020YearsLater, imgHalloweenResurrection, imgHalloween2018, imgHalloweenKills, imgHalloweenEnds, imgSpiderMan, imgSpiderMan2, imgSpiderMan3, imgTheAmazingSpiderMan, imgTheAmazingSpiderMan2
    imgShrek = PhotoImage(file='Movie Covers/Shrek.png')
    imgRiseOfTheGuardians = PhotoImage(file='Movie Covers/Rise of the Guardians.png')
    imgShrek2 = PhotoImage(file='Movie Covers/Shrek 2.png')
    imgShrektheThird = PhotoImage(file='Movie Covers/Shrek the Third.png')
    imgTheWizardofOz = PhotoImage(file='Movie Covers/The Wizard of Oz.png')
    imgJourneyBacktoOz = PhotoImage(file='Movie Covers/Journey Back to Oz.png')
    imgOzTheGreatandPowerful = PhotoImage(file='Movie Covers/Oz The Great and Powerful.png')
    imgReturntoOz = PhotoImage(file='Movie Covers/Return to Oz.png')
    imgBacktotheFuture = PhotoImage(file='Movie Covers/Back to the Future.png')
    imgBacktotheFuturePartII = PhotoImage(file='Movie Covers/Back to the Future Part II.png')
    imgBacktotheFuturePartIII = PhotoImage(file='Movie Covers/Back to the Future Part III.png')
    imgJourneytotheCenteroftheEarth = PhotoImage(file='Movie Covers/Journey to the Center of the Earth.png')
    imgJourney2TheMysteriousIsland = PhotoImage(file='Movie Covers/Journey 2 The Mysterious Island.png')
    imgHalloween = PhotoImage(file='Movie Covers/Halloween.png')
    imgHalloweenII = PhotoImage(file='Movie Covers/Halloween II.png')
    imgHalloweenIIISeasonoftheWitch = PhotoImage(file='Movie Covers/Halloween III Season of the Witch.png')
    imgHalloween4TheReturnofMichaelMyers = PhotoImage(file='Movie Covers/Halloween 4 The Return of Michael Myers.png')
    imgHalloween5TheRevengeofMichaelMyers = PhotoImage(file='Movie Covers/Halloween 5 The Revenge of Michael Myers.png')
    imgHalloweenTheCurseofMichaelMyers = PhotoImage(file='Movie Covers/Halloween The Curse of Michael Myers.png')
    imgHalloweenH2020YearsLater = PhotoImage(file='Movie Covers/Halloween H20 20 Years Later.png')
    imgHalloweenResurrection = PhotoImage(file='Movie Covers/Halloween Resurrection.png')
    imgHalloween2018 = PhotoImage(file='Movie Covers/Halloween(2018).png')
    imgHalloweenKills = PhotoImage(file='Movie Covers/Halloween Kills.png')
    imgHalloweenEnds = PhotoImage(file='Movie Covers/Halloween Ends.png')
    imgSpiderMan = PhotoImage(file='Movie Covers/Spider-Man.png')
    imgSpiderMan2 = PhotoImage(file='Movie Covers/Spider-Man 2.png')
    imgSpiderMan3 = PhotoImage(file='Movie Covers/Spider-Man 3.png')
    imgTheAmazingSpiderMan = PhotoImage(file='Movie Covers/The Amazing Spider-Man.png')
    imgTheAmazingSpiderMan2 = PhotoImage(file='Movie Covers/The Amazing Spider-Man 2.png')
    if 'Shrek' == selMovie:
        mov = imgShrek
    elif 'Rise Of The Guardians' == selMovie:
        mov = imgRiseOfTheGuardians
    elif 'Shrek 2' == selMovie:
        mov = imgShrek2
    elif 'Shrek the Third' == selMovie:
        mov = imgShrektheThird
    elif 'The Wizard of Oz' == selMovie:
        mov = imgTheWizardofOz
    elif 'Journey Back to Oz' == selMovie:
        mov = imgJourneyBacktoOz
    elif 'Oz The Great and Powerful' == selMovie:
        mov = imgOzTheGreatandPowerful
    elif 'Return to Oz' == selMovie:
        mov = imgReturntoOz
    elif 'Back to the Future' == selMovie:
        mov = imgBacktotheFuture
    elif 'Back to the Future Part II' == selMovie:
        mov = imgBacktotheFuturePartII
    elif 'Back to the Future Part III' == selMovie:
        mov = imgBacktotheFuturePartIII
    elif 'Journey to the Center of the Earth' == selMovie:
        mov = imgJourneytotheCenteroftheEarth
    elif 'Journey 2 The Mysterious Island' == selMovie:
        mov = imgJourney2TheMysteriousIsland
    elif 'Halloween' == selMovie:
        mov = imgHalloween
    elif 'Halloween II' == selMovie:
        mov = imgHalloweenII
    elif 'Halloween III Season of the Witch' == selMovie:
        mov = imgHalloweenIIISeasonoftheWitch
    elif 'Halloween 4 The Return of Michael Myers' == selMovie:
        mov = imgHalloween4TheReturnofMichaelMyers
    elif 'Halloween 5 The Revenge of Michael Myers' == selMovie:
        mov = imgHalloween5TheRevengeofMichaelMyers
    elif 'Halloween The Curse of Michael Myers' == selMovie:
        mov = imgHalloweenTheCurseofMichaelMyers
    elif 'Halloween H20 20 Years Later' == selMovie:
        mov = imgHalloweenH2020YearsLater
    elif 'Halloween Resurrection' == selMovie:
        mov = imgHalloweenResurrection
    elif 'Halloween(2018)' == selMovie:
        mov = imgHalloween2018
    elif 'Halloween Kills' == selMovie:
        mov = imgHalloweenKills
    elif 'Halloween Ends' == selMovie:
        mov = imgHalloweenEnds
    elif 'Spider-Man' == selMovie:
        mov = imgSpiderMan
    elif 'Spider-Man 2' == selMovie:
        mov = imgSpiderMan2
    elif 'Spider-Man 3' == selMovie:
        mov = imgSpiderMan3
    elif 'The Amazing Spider-Man' == selMovie:
        mov = imgTheAmazingSpiderMan
    elif 'The Amazing Spider-Man 2' == selMovie:
        mov = imgTheAmazingSpiderMan2
    return mov