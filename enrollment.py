import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    data["total_enrollment"] = data["TOT_ENR_F"] + data["TOT_ENR_M"]
    
    hisp_m_sum = data["SCH_ENR_HI_M"].sum()
    hisp_f_sum =data["SCH_ENR_HI_F"].sum()
    ameri_m_sum = data["SCH_ENR_AM_M"].sum()
    ameri_f_sum = data["SCH_ENR_AM_F"].sum()
    asian_m_sum = data["SCH_ENR_AS_M"].sum()
    asian_f_sum = data["SCH_ENR_AS_F"].sum()
    hawa_m_sum = data["SCH_ENR_HP_M"].sum()
    hawa_f_sum = data["SCH_ENR_HP_F"].sum()
    black_m_sum = data["SCH_ENR_BL_M"].sum()
    black_f_sum = data["SCH_ENR_BL_F"].sum()
    white_m_sum = data["SCH_ENR_WH_M"].sum()
    white_f_sum = data["SCH_ENR_WH_F"].sum()
    two_m_sum = data["SCH_ENR_TR_M"].sum()
    two_f_sum = data["SCH_ENR_TR_F"].sum()
    
    all_enrollment = data["total_enrollment"].sum()
    
    hisp1 = hisp_m_sum / all_enrollment
    hisp2 = hisp_f_sum / all_enrollment
    ameri1 = ameri_m_sum / all_enrollment
    ameri2 = ameri_f_sum / all_enrollment
    asian1 = asian_m_sum /all_enrollment
    asian2 = asian_f_sum /all_enrollment
    hawa1 = hawa_m_sum / all_enrollment
    hawa2 = hawa_f_sum / all_enrollment
    black1 = black_m_sum / all_enrollment
    black2 = black_f_sum / all_enrollment
    white1 = white_m_sum / all_enrollment
    white2 = white_f_sum / all_enrollment
    two1 = two_m_sum / all_enrollment
    two2 = two_f_sum / all_enrollment
    
    print(hisp1)
    print(hisp2)
    print(ameri1)
    print(ameri2)
    print(asian1)
    print(asian2)
    print(hawa1)
    print(hawa2)
    print(black1)
    print(black2)
    print(white1)
    print(white2)
    print(two1)
    print(two2)