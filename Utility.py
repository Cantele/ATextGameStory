import atextgamestory

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
    salvataggio_progressi = []
    saving = open("saving.txt", "w")
    saving.write(str(salvataggio_progressi))
    saving.close()
    print("SV-OK")
    return saving
def saving_aggiungi():
    global salvataggio_progressi

    if "1" in salvataggio_progressi == True:
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
def saving_load():
    progressi_scena1 = ["1"]
    lettura = open ("saving.txt", "r")
    lettura2 = str (lettura.read ())
    global salvataggio_progressi
    salvataggio_progressi = list (lettura2.split (","))
    lettura.close ()

#SETUPPARE COLLEGAMENTO TRA LISTE DI FILE DIVERSI