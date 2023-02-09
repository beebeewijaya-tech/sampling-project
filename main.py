import pandas as pd


def get_file():
    data = pd.read_csv("./data.csv")
    return data


# Get 12 sample from Junior
def get_junior_sample():
    data = get_file()
    j = data[data["Level"] == "Junior"]
    
    # SRS to get 12 sample
    j_sample = j.sample(n=12)
    return j_sample
    

# Get 11 sample from Mid Level
def get_mid_level():
    data = get_file()
    m = data[data["Level"] == "Mid Level"]
    
    # SRS to get 12 sample
    m_sample = m.sample(n=11)
    return m_sample
    
    
# Get 7 sample from Senior Level
def get_senior_level():
    data = get_file()
    s = data[data["Level"] == "Senior"]
    
    # SRS to get 12 sample
    s_sample = s.sample(n=7)
    return s_sample
    
def main():
    junior = get_junior_sample()
    midlevel = get_mid_level()
    senior = get_senior_level()
    
    
    sampled = pd.concat([junior, midlevel, senior], ignore_index=True, sort=False)
    sample_data = sampled[["Nama", "Umur", "Departement", "Gaji", "Level", "Gender"]]

    print(sample_data)
    
    
main()