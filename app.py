import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import io

# Define location data
locations = [
    {"location": 'Agam', "number": '211'},
            {"location": 'AldineTX', "number": '61'},
            {"location": 'AliceSprings', "number": '129'},
            {"location": 'Altzomoni', "number": '65'},
            {"location": 'ArlingtonTX', "number": '207'},
            {"location": 'Athens-NOA', "number": '119'},
            {"location": 'AtlantaGA-Conyers', "number": '158'},
            {"location": 'AtlantaGA-GATech', "number": '173'},
            {"location": 'AtlantaGA-SouthDeKalb', "number": '237'},
            {"location": 'AtlantaGA', "number": '158'},
            {"location": 'AustinTX', "number": '257'},
            {"location": 'Bandung', "number": '210'},
            {"location": 'Bangkok', "number": '190'},
            {"location": 'Banting', "number": '78'},
            {"location": 'BayonneNJ', "number": '38'},
            {"location": 'Beijing-RADI', "number": '171'},
            {"location": 'BeltsvilleMD', "number": '80'},
            {"location": 'Berlin', "number": '132'},
            {"location": 'BlueHillMA', "number": '139'},
            {"location": 'BostonMA', "number": '155'},
            {"location": 'BoulderCO-NCAR', "number": '204'},
            {"location": 'BoulderCO', "number": '57'},
            {"location": 'Bremen', "number": '21'},
            {"location": 'BristolPA', "number": '134'},
            {"location": 'BronxNY', "number": '147'},
            {"location": 'Brussels-Uccle', "number": '162'},
            {"location": 'Bucharest', "number": '111'},
            {"location": 'BuenosAires', "number": '114'},
            {"location": 'BuffaloNY', "number": '206'},
            {"location": 'Busan', "number": '20'},
            {"location": 'Cabauw', "number": '118'},
            {"location": 'Calakmul', "number": '141'},
            {"location": 'CambridgeBay', "number": '281'},
            {"location": 'CambridgeMA', "number": '26'},
            {"location": 'CameronLA', "number": '260'},
            {"location": 'CapeElizabethME', "number": '184'},
            {"location": 'Cebu', "number": '225'},
            {"location": 'ChapelHillNC', "number": '166'},
            {"location": 'CharlesCityVA', "number": '31'},
            {"location": 'ChelseaMA', "number": '153'},
            {"location": 'ChiangMai', "number": '213'},
            {"location": 'ChicagoIL', "number": '249'},
            {"location": 'Cologne', "number": '67'},
            {"location": 'ComodoroRivadavia', "number": '124'},
            {"location": 'Cordoba', "number": '113'},
            {"location": 'CornwallCT', "number": '179'},
            {"location": 'CorpusChristiTX', "number": '258'},
            {"location": 'Daegu', "number": '229'},
            {"location": 'Dalanzadgad', "number": '217'},
            {"location": 'Davos', "number": '120'},
            {"location": 'DearbornMI', "number": '39'},
            {"location": 'DeBilt', "number": '82'},
            {"location": 'Dhaka', "number": '76'},
            {"location": 'Downsview', "number": '103'},
            {"location": 'EastProvidenceRI', "number": '185'},
            {"location": 'EdwardsCA', "number": '74'},
            {"location": 'Egbert', "number": '108'},
            {"location": 'EssexMD', "number": '75'},
            {"location": 'Eureka-0PAL', "number": '280'},
            {"location": 'Eureka-PEARL', "number": '144'},
            {"location": 'FairbanksAK', "number": '174'},
            {"location": 'Fajardo', "number": '60'},
            {"location": 'FortMcKay', "number": '122'},
            {"location": 'FortYatesND', "number": '205'},
            {"location": 'Fukuoka', "number": '199'},
            {"location": 'Gongju-KNU', "number": '230'},
            {"location": 'Granada', "number": '238'},
            {"location": 'GrandForksND', "number": '200'},
            {"location": 'GreenbeltMD', "number": '2'},
            {"location": 'Haldwani-ARIES', "number": '250'},
            {"location": 'HamptonVA-HU', "number": '156'},
            {"location": 'HamptonVA', "number": '37'},
            {"location": 'Heidelberg', "number": '133'},
            {"location": 'Helsinki', "number": '105'},
            {"location": 'HoustonTX-SanJacinto', "number": '261'},
            {"location": 'HoustonTX', "number": '25'},
            {"location": 'HuntsvilleAL', "number": '66'},
            {"location": 'Ilocos', "number": '219'},
            {"location": 'Incheon-ESC', "number": '189'},
            {"location": 'Innsbruck', "number": '106'},
            {"location": 'IowaCityIA-WHS', "number": '246'},
            {"location": 'Islamabad-NUST', "number": '73'},
            {"location": 'Izana', "number": '101'},
            {"location": 'Jeonju', "number": '241'},
            {"location": 'Juelich', "number": '30'},
            {"location": 'KenoshaWI', "number": '167'},
            {"location": 'Kobe', "number": '198'},
            {"location": 'Kosetice', "number": '239'},
            {"location": 'LaPaz', "number": '283'},
            {"location": 'LaPorteTX', "number": '11'},
            {"location": 'LapwaiID', "number": '188'},
            {"location": 'LibertyTX', "number": '143'},
            {"location": 'Lindenberg', "number": '130'},
            {"location": 'LondonderryNH', "number": '183'},
            {"location": 'LynnMA', "number": '107'},
            {"location": 'MadisonCT', "number": '186'},
            {"location": 'ManhattanKS', "number": '165'},
            {"location": 'ManhattanNY-CCNY', "number": '135'},
            {"location": 'MaunaLoaHI', "number": '56'},
            {"location": 'MexicoCity-UNAM', "number": '142'},
            {"location": 'MexicoCity-Vallejo', "number": '157'},
            {"location": 'MiamiFL-FIU', "number": '256'},
            {"location": 'MountainViewCA', "number": '34'},
            {"location": 'Nagoya', "number": '197'},
            {"location": 'Nainital-ARIES', "number": '251'},
            {"location": 'NewBrunswickNJ', "number": '69'},
            {"location": 'NewHavenCT', "number": '64'},
            {"location": 'NewLondonCT', "number": '236'},
            {"location": 'NewOrleansLA-XULA', "number": '85'},
            {"location": 'NyAlesund', "number": '152'},
            {"location": 'OldFieldNY', "number": '51'},
            {"location": 'Palau', "number": '131'},
            {"location": 'Palawan', "number": '221'},
            {"location": 'PhiladelphiaPA', "number": '166'},
            {"location": 'PhnomPenh', "number": '215'},
            {"location": 'PittsburghPA', "number": '187'},
            {"location": 'Pontianak', "number": '212'},
            {"location": 'Potchefstroom-METSI', "number": '53'},
            {"location": 'QueensNY', "number": '55'},
            {"location": 'QuezonCity', "number": '224'},
            {"location": 'RichmondCA', "number": '52'},
            {"location": 'Rome-IIA', "number": '138'},
            {"location": 'Rome-ISAC', "number": '115'},
            {"location": 'Rome-SAP', "number": '117'},
            {"location": 'Rotterdam-Haven', "number": '84'},
            {"location": 'SaltLakeCityUT-Hawthorne', "number": '72'},
            {"location": 'SaltLakeCityUT', "number": '154'},
            {"location": 'SanJoseCA', "number": '181'},
            {"location": 'Sapporo', "number": '195'},
            {"location": 'Seosan', "number": '164'},
            {"location": 'Seoul-KU', "number": '235'},
            {"location": 'Seoul-SNU', "number": '149'},
            {"location": 'Seoul', "number": '27'},
            {"location": 'Singapore-NUS', "number": '77'},
            {"location": 'Songkhla', "number": '214'},
            {"location": 'SouthJordanUT', "number": '139'},
            {"location": 'StGeorge', "number": '109'},
            {"location": 'StonyPlain', "number": '123'},
            {"location": 'Suwon-USW', "number": '231'},
            {"location": 'SWDetroitMI', "number": '147'},
            {"location": 'Tel-Aviv', "number": '182'},
            {"location": 'Thessaloniki', "number": '240'},
            {"location": 'Tokyo-Sophia', "number": '192'},
            {"location": 'Tokyo-TMU', "number": '194'},
            {"location": 'Toronto-CNTower', "number": '243'},
            {"location": 'Toronto-Scarborough', "number": '145'},
            {"location": 'Toronto-West', "number": '108'},
            {"location": 'Trollhaugen', "number": '242'},
            {"location": 'Tsukuba-NIES-West', "number": '163'},
            {"location": 'Tsukuba-NIES', "number": '176'},
            {"location": 'Tsukuba', "number": '193'},
            {"location": 'TubaCityAZ', "number": '254'},
            {"location": 'TucsonAZ', "number": '253'},
            {"location": 'TurlockCA', "number": '248'},
            {"location": 'TylerTX', "number": '259'},
            {"location": 'Ulaanbaatar', "number": '216'},
            {"location": 'Ulsan', "number": '150'},
            {"location": 'Vientiane', "number": '218'},
            {"location": 'VirginiaBeachVA-CBBT', "number": '255'},
            {"location": 'WacoTX', "number": '207'},
            {"location": 'Wakkerstroom', "number": '159'},
            {"location": 'WallopsIslandVA', "number": '40'},
            {"location": 'Warsaw-UW', "number": '270'},
            {"location": 'WashingtonDC', "number": '140'},
            {"location": 'WestportCT', "number": '177'},
            {"location": 'WhittierCA', "number": '247'},
            {"location": 'Windsor-West', "number": '208'},
            {"location": 'WrightwoodCA', "number": '68'},
            {"location": 'Yokosuka', "number": '146'},
            {"location": 'Yongin', "number": '232'}
]

df = pd.DataFrame(locations)
# Define a mapping of L2 file types to user-friendly names
l2_file_types = {
    "rfuh5p1-8": "Formaldehyde Unvalidated",
    "rfus5p1-8": "Formaldehyde Official",
    "rnvh3p1-8": "Nitrogen Dioxide Official, Water Vapor Unvalidated",
    "rnvs3p1-8": "Nitrogen Dioxide Official",
    "rout2p1-8": "Ozone Official",
    "rsus1p1-8": "Sulfur Dioxide Official",
    "rwvt1p1-8": "Water Vapor Official"
}

# Streamlit UI
st.title("Pandora L2 Data Checker")
st.write("Select a Pandora location, number, and L2 file type to view data.")

# Dropdown for selecting location
selected_location = st.selectbox("Select Pandora Number", df["number"].tolist())

# Get the selected location data
selected_data = df[df["number"] == selected_location].iloc[0]

# Dropdown for selecting L2 file type with human-readable names
selected_l2_label = st.selectbox("Select L2 File Type", list(l2_file_types.values()))

# Get the corresponding file type identifier from the selected label
selected_l2_type = [key for key, value in l2_file_types.items() if value == selected_l2_label][0]

# Construct L2 file URL based on user selection
l2_url = f"https://data.ovh.pandonia-global-network.org/{selected_data['location']}/Pandora{selected_data['number']}s1/L2/Pandora{selected_data['number']}s1_{selected_data['location']}_L2_{selected_l2_type}.txt"
st.write(f"Generated L2 URL: [Click to Open]({l2_url})")
st.write(f"**Selected Location:** {selected_data['location']}")
st.write(f"**Pandora Number:** {selected_data['number']}")


# Function to extract column names dynamically
def extract_column_names(file_content):
    column_names = []
    seen_names = {}
    for line in file_content:
        if line.strip().startswith("Column") and not line.strip().startswith("From"):
            parts = line.split(":", 1)
            if len(parts) > 1:
                base_name = parts[1].strip().split(",")[0]
                if base_name in seen_names:
                    seen_names[base_name] += 1
                    unique_name = f"{base_name}_{seen_names[base_name]}"
                else:
                    seen_names[base_name] = 0
                    unique_name = base_name
                column_names.append(unique_name)
    return column_names

# Function to fetch and process L2 data
def fetch_l2_data(url):
    try:
        response = requests.get(url)
        st.write(f"Server Response Code: {response.status_code}")
        if response.status_code == 200:
            data = response.content.decode("utf-8", errors="ignore").splitlines()
            return data
        else:
            return None
    except Exception as e:
        st.write(f"Error fetching data: {e}")
        return None

l2_data = fetch_l2_data(l2_url)

if l2_data:
    st.write("L2 Data Retrieved Successfully! Processing...")
    
    # Detect the start of the data section
    data_section = None
    for i, line in enumerate(l2_data):
        if line.strip().startswith("202"):
            data_section = "\n".join(l2_data[i:])
            break
    else:
        st.write("No valid data found in the file.")
        data_section = None

    if data_section:
        df_l2 = pd.read_csv(
            io.StringIO(data_section),
            delim_whitespace=True,
            on_bad_lines="skip"
        )

        # Ensure datetime conversion
        timestamp_column = df_l2.columns[0]
        df_l2[timestamp_column] = pd.to_datetime(df_l2[timestamp_column], format="%Y%m%dT%H%M%S.%fZ", errors="coerce")
        df_l2.dropna(subset=[timestamp_column], inplace=True)
        df_l2.sort_values(by=timestamp_column, inplace=True)

        # Plot stacked subplots
        fig, axes = plt.subplots(6, 1, figsize=(12, 8), sharex=True)
        axes[0].plot(df_l2[timestamp_column], df_l2.iloc[:, 1], 'k.')
        axes[0].set_title("DQ [%]")
        
        axes[1].bar(df_l2[timestamp_column], df_l2.iloc[:, 2], color='blue')
        axes[1].set_title(f"vc_{selected_l2_label} [mmol/m^2]")
        
        axes[2].plot(df_l2[timestamp_column], df_l2.iloc[:, 3], 'ro')
        axes[2].set_title("wrms_lnd.sun")
        
        axes[3].plot(df_l2[timestamp_column], df_l2.iloc[:, 4], 'bo')
        axes[3].set_title("wl_shift_total [pm]")
        
        axes[4].plot(df_l2[timestamp_column], df_l2.iloc[:, 5], 'r.')
        axes[4].set_title("wl_temp [dgC]")
        
        axes[5].plot(df_l2[timestamp_column], df_l2.iloc[:, 6], 'r.')
        axes[5].set_title("mean_value_fitting_window")
        
        for ax in axes:
            ax.grid(True)
        
        plt.xticks(rotation=45)
        st.pyplot(fig)
else:
    st.write("Failed to fetch L2 data or data unavailable.")
