import atextgamestory, Utility, pygame, time, sys



# INIZIO DEL PRIMO EPISODIO   (prima scena)

# INIZIO DEL PRIMO EPISODIO
def scena1():
    #starting del file audio
    #file = 'Piscio.mp3'
    #pygame.mixer.init()
    #pygame.mixer.music.load(file)
    #pygame.mixer.music.play()
    #time.sleep(0.5)
    #starting della prima frase
    frase1 = (
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\EPISODIO 1\n\n\ni tuoi occhi si aprono a fatica.......... \ncome se non li aprissi da anni......\nti senti stanco..... assonnato... e  non sai dove ti trovi............ \npercepisci che l'ambiente intorno a te è grande............ "
        "\nquando qualcosa inizia a fare del rumore...... \n"
        "lo senti che si avvicina \ncorrendo .......... \ninizi a sentire il suo respiro \n"
        "percepisci che è vicino  \nmolto vicino..... con uno scatto involontario balzi indietro \n"
        "urti con il braccio destro un oggetto solido \ndi forma cubica, spigolosa \n"
        "l'animale indietreggia quasi come se fosse lui più spaventato di te \n"
        "e proprio in quel momento una voce metallica inizia a parlare alla tua destra \n"
        "dice :'nome dell'animale, pacifico, età 3 anni, un piccolo quadrupede simile ad un gatto, pelo schiumoso e leggermente pennato,\n"
        "agile e veloce si preda principalmente di piccoli animali \n"
        "a quel punto per istinto allunghi la mano in un gesto amichevole verso la creatura \n"
        "lui struscia quello che sembra il suo muso sul tuo arto \n"
        "così come per magia la tua mente si dimentica........\n "
        "di ogni cosa, di ogni dubbio, paura, insicurezza \n"
        "così per un momento la tua vita diviene magnifica.....................\n ")
    # modulo di scrittura

    for char in frase1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.007)
    # aggiunta del valore 1
    global salvataggio_progressi
    Utility.saving_crea()
    Utility.saving_aggiungi()
    # richiamo motore di saving
    Utility.saving()
    domanda = input ("premi 1 per   continuare con il prossimo episodio oppure premi INVIO per tornare al menù")

    if domanda == "1":
        atextgamestory.scena2()
    else:
        atextgamestory.menù()
