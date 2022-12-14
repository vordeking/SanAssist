from .WaterGetScore import GetScoreWater
from .GetScore  import GetScoreAir
import statistics as st
import pandas as pd

def make_dico(tresh):
    dico={}
    for index, i in tresh.iterrows() :
        dico[i["name"]]=i["recommandations"]
    return dico

def LaunchAlgo(ville):

    Scoretotal = []
    scoreair = GetScoreAir(ville)
    scorewater = GetScoreWater(ville)
    Scoretotal+=scoreair
    Scoretotal+=scorewater
    DicoAIR={"CO":scoreair[0],"NO2":scoreair[1],"PPM10":scoreair[2],"PPM2.5":scoreair[3]}
    DicoWater = {"Nitrate":scorewater[0],"Nitrite":scorewater[1]}
    FinalScore = st.mean(Scoretotal)
    df_threshold = pd.read_csv("/Users/alchambron/Documents/Coding_Project/hackatton/sanassist/sanassist/home/ThreshDB.csv")
    dico_reco= make_dico(df_threshold)

    FinalList=[FinalScore,DicoAIR,DicoWater,dico_reco]

    return FinalList

print(LaunchAlgo("Paris"))
