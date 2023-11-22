import csv
import json
allData = []
allQuestion = {
      "12":2.1,
      "3":2,
      "14":1.9,
      "11":1.8,
      "4":1.7,
      "8":1.6,
      "5":1.5,
      "9":1.4,
      "13":1.3,
      "7":1.2,
      "6":1.1,
      "10":1}

max = 17.6

BinaryQuestion = [3,4,5,6,7,8,10,13,14]
BinaryAnswer = {"3":{"WIFI":1,"4G / 3G":0},"8":{"Oui":0,"Non":1}}
OtherAnswer = {"11":{"Oui":1,"Parfois":0.5,"Non":0},"12":{"1 an":0,"2 ans":0.5,"3 ans":0.75,"plus de 3 ans":1},"9":{"Oui":1,"Non":0,"/":0}}
QuestionAnswer = {}
QUestionIndex = [13]
CritereIndex = 2

with open("resultat.csv",newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            allData.append(row[1:])
score = []
for questionActuelle in QUestionIndex:
        QuestionAnswer[questionActuelle] = {}
        for reponseActuelle in allData[1:]:
            if QuestionAnswer[questionActuelle].get(reponseActuelle[CritereIndex]) == None:
                QuestionAnswer[questionActuelle][reponseActuelle[CritereIndex]] = {"Oui":0,"Non":0}
            if reponseActuelle[questionActuelle] == "Oui":
                QuestionAnswer[questionActuelle][reponseActuelle[CritereIndex]]["Oui"] += 1
            if reponseActuelle[questionActuelle] == "Non":
                QuestionAnswer[questionActuelle][reponseActuelle[CritereIndex]]["Non"] += 1
print(QuestionAnswer)


for ReponseActuelle in allData[1:]:
    temp = []
    somme = 0
    for indexQuestion in range(3,14):
        coef = allQuestion[str(indexQuestion)]
        if BinaryQuestion.count(indexQuestion) != 0:
            if BinaryAnswer.get(str(indexQuestion)) != None:
                somme += BinaryAnswer[str(indexQuestion)][ReponseActuelle[indexQuestion]] * coef
            else:
                 if ReponseActuelle[indexQuestion] == "Oui":
                      somme += coef
        else:
             somme += OtherAnswer[str(indexQuestion)][ReponseActuelle[indexQuestion]] * coef
    score.append(somme)

scoreNotFiltred = score.copy()
score.sort(reverse=True)

AgeReponse = ["moins de 18 ans","18 - 25 ans","26 - 35 ans","36 - 50 ans","51 - 60 ans","plus de 60 ans"]
GenreReponse = ["Homme","Femme"]
ActiviteReponse = ["Chef d'entreprise","Etudiant / lycéen","Ouvrier","Retraité","Profession intermédiaire","En recherche d'emploi","Cadre"]

LesIndex = [0,2]

AllReponse = [AgeReponse,ActiviteReponse]

AllMoyenne = {}

for ChoiceIndex in range(len(AllReponse)):
        for index,value in enumerate(AllReponse[ChoiceIndex]):
            AllMoyenne[value] = {}
            allSum = {}
            currentIndex = []
            for index2,Data in enumerate(allData):
                if Data[LesIndex[ChoiceIndex]] == value:
                    currentIndex.append(index2)
            currentSomme = 0
            for x in currentIndex:
                currentSomme += (scoreNotFiltred[x-1]/max * 10)
            if len(currentIndex) > 0:
                AllMoyenne[value] = (currentSomme/len(currentIndex))

#print(AllMoyenne)