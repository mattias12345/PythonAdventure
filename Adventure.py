import random



def leta():
  print("I grottan finns det inget otäckt. Du hittar däremot ett alvsvärd som ökar ditt stridsvärde i strid.")
  

def combat():
  print("Dvärgen kastar sig skrikandes mot dig!")
  val =input("Har du ett magiskt alvsvärd?(y/n)")
  if val == "y":
    print("Din stridsförmåga höjs med 8 stridspoäng")
    äventyrare =(random.randint(0,10)+8)
    AI =random.randint(0,10)
  else:
    print("Otur. Striden börjar.")
    äventyrare =random.randint(0,10)
    AI =random.randint(0,10)
  if äventyrare > AI:
    print("Din stridspoäng är", äventyrare, "och dvärgens är", AI, "Du vinner striden!")
  elif äventyrare < AI:
    print("Din stridspoäng är", äventyrare, "och dvärgens är", AI, "Dvärgen vinner! Äventyret är över.")
    return
  
    



def playGame():
  name =input("Vad heter du?")
  print("Hej",name,". Du är en äventyrare som tröttnade på din vardag och lämnade allt för att finna bortglömda skatter.")


  val1 =input("Du står vid en väg. Långt borta i fjärran ser du åskmoln närma sig. Vill du fortsätta vägen rakt fram(f) eller undersöka en grotta i närheten?(g)")
  if val1 =="g":
    leta()
    

  val2 =input("Lite längre fram dyker en dvärg upp och vill slåss. Vill du ta en annan väg?(y/n)")
  if val2 == "y":
    print("Du tar en annan väg")
  else: combat()

  print("Du går vidare. Över ett vattendrag finns en bro men där står också en trollkarl som vaktar övergången med magi. Du kan inte slå dig förbi honom.")
  print("Han säger: Den som över floden vill gå, en gåta att svara måste få.")
  svar =input("Gåtan lyder som så: Vad är det som går och går men aldrig kommer någonvart?(tiden/SJ/karriären")
  while svar != "SJ":
     svar =input("Nej! Det är fel! Odugligt.Du får ett nytt försök säger trollkarlen.(tiden/SJ/karriären")
  print("Svaret är korrekt.Du får gå över bron.")
  print("I en dal ser du skatten glimra i en skattkista.Mwn den vaktas av en ondsint enhörning.Enda chansen att besegra enhörningen är att gissa rätt tal, mellan 1 och 5.Du har 20% chans.")
  gissa =input("Gissa:")
  AI =str(random.randint(1,1))
  if gissa == AI:
    print("type ", type(AI), type(gissa))
    print("Grattis! Du har gissat rätt tal och vinner skatten. Spelet är slut")
    return
  else:
    print("Tyvärr.Du gissade",gissa, "och rätt svar var",AI,",enhörningen mosade dig. Äventyret är över.")
    
        

if __name__ == '__main__':
  
  playGame()

  beslut ="y"
  while beslut =="y":
  
    beslut =input("Vill du speka igen?(y/n)")
  
    if beslut =="y":
      playGame()
  



  print("Hej då")


      
  
  


  


