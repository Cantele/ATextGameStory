import atextgamestory, sys, time





# motore di salvataggio
salvataggio_progressi = []
def saving_crea():
    try:
        saving = open("saving.txt", "w")
    except:
        saving = open("saving.txt", "x")
    saving.close()
# METTERE A POSTO STA ROBA
def saving():
    saving = open("saving.txt", "w")
    saving.write(str(salvataggio_progressi))
    saving.close()
    print("SV-OK")
    return saving
def saving_aggiungi():
    global salvataggio_progressi

    if "1" in salvataggio_progressi :
        domanda = input("premi 1 per   continuare con il prossimo episodio oppure premi INVIO per tornare al menù")
        if domanda == "1":
            atextgamestory.scena2()
        # richiamo menu
        else:
            atextgamestory.menù()
    else:
        salvataggio_progressi.append("1")

        # richiamo motore di saving
        saving()
        domanda = input ("premi 1 per   continuare con il prossimo episodio oppure premi INVIO per tornare al menù")

        if domanda == "1":
            atextgamestory.scena2()
        else:
            atextgamestory.menù()
def continuer():
    global salvataggio_progressi
    if "1" in salvataggio_progressi:
        Capitolo_2.scena2()
    else:
        print("prima di poter accedere all'episodio 2 devi aver completato l'episodio 1")
        atextgamestory.menù()

#SETUPPARE COLLEGAMENTO TRA LISTE DI FILE DIVERSI