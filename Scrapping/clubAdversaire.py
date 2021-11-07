
def linkConstructor(lien):
    lienSplit = lien.split("/")
    x="-".join(lienSplit[-1].split("-")[3:])
    link = "/".join(lienSplit[:7])+"/vs_opp/Historiques-"+x+"-contre-ses-adversaires"
    return link

# Fon ction qui crée les liens pour accéder à la page ou extraire 
def linkCoatchExtractor(lien ):
    link= "/".join(lien.split("/")[:6])+"/Statistiques"+ lien.split("Stats-et-historique-de")[1]
    return link



def adversaireExrtract(link):
  page = requests.get(link)
  soup = BeautifulSoup(page.content, "html.parser")
  soupbody= soup.find("tbody")
  soupbody_tr = soupbody.findAll("tr")
  tr_size= len(soupbody_tr)

  # Création du lien
  clubName= soup.find("p").get_text().split(":")[1]

  df_All_Advers = []
  for i in range(0,tr_size):
      soupbody_tr_i  =  soupbody_tr[i]
  
      #--------------------------------------------- Début d'extration ---------------------------------------
      soupbody_tri_th = soupbody_tr_i.find("th")
      NomAdversaire = soupbody_tri_th.find("a").get_text()

      #print("NomAdversaire: "+NomAdversaire)
      soupbody_tri_td = soupbody_tr_i.findAll("td")
     # print(len(soupbody_tri_td))
      if(len(soupbody_tri_td)==10):
          nbMatchJoue = soupbody_tri_td[1].get_text()
          #print(nbMatchJoue)
          nbVictoire = soupbody_tri_td[2].get_text()
          #print("nbVictoire: " + nbVictoire)
          nbNull = soupbody_tri_td[3].get_text()
          #print("nbNull: "+ nbNull)
          nbDefaite = soupbody_tri_td[4].get_text()
          #print(nbDefaite)
          nbButMarque = soupbody_tri_td[5].get_text()
          #print(nbButMarque)
          ButEncaisse= soupbody_tri_td[6].get_text()
          #print(ButEncaisse)
          DifferenceDeBut= soupbody_tri_td[7].get_text()
        # print(DifferenceDeBut)
          PointDuMatch = soupbody_tri_td[8].get_text()
        #  print(PointDuMatch)
          match = clubName + "  VS  "+ NomAdversaire
      dico = {
              "match": [match],
              "Nom_Adversaire":[NomAdversaire],
              "Nombre_de_matche Joué":[nbMatchJoue],
              "Victoire":[nbVictoire],
              "Match_nul":[nbNull],
              "Défaite":[nbDefaite],
              "But_marque":[nbButMarque],
              "But_encaisse":[ButEncaisse],
              "Diffence_de_but":[DifferenceDeBut],
              "Point_dumatch":[PointDuMatch]

      }
      df_advers= pd.DataFrame(dico)
      df_All_Advers.append(df_advers)

  df_All_Advers= pd.concat(df_All_Advers)
  return  df_All_Advers
