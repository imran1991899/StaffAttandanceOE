import streamlit as st
import pandas as pd

st.set_page_config(page_title="Team Attendance Dashboard", layout="wide")

st.title("📊 Team Attendance Dashboard")

# Function to read the specific columns from your existing Excel
@st.cache_data
def load_data():
    # We use 'usecols' to pick D, G, and H specifically by their index (D=3, G=6, H=7)
    df = pd.read_excel("attendance.xlsx", usecols=[3, 6, 7], header=0)
    df.columns = ["Staff Name", "CheckIn Location", "CheckIn Time"]
    return df

try:
    df = load_data()

    # Create a layout for the teams
    teams = [
        "Team QualEx Central", "Team QualEx Northern", 
        "Team InnoSync", "Team EngageX", "Team CoFast", "Admin"
    ]

    # Show 2 teams per row for better readability
    cols = st.columns(2)
    
    for index, team_name in enumerate(teams):
        # Determine which column to place the team card in
        with cols[index % 2]:
            st.markdown(f"### 📍 {team_name}")
            
            # Filter data for this specific team
            team_df = df[df["CheckIn Location"] == team_name]
            
            if not team_df.empty:
                # Apply styling: if time is 'MC', it stays as text
                st.table(team_df[["Staff Name", "CheckIn Time"]].reset_index(drop=True))
            else:
                st.info(f"No data for {team_name}")

except Exception as e:
    st.error("Error: Please ensure your file is named 'attendance.xlsx' and columns D, G, and H contain the data.")
    st.info("Technical details: " + str(e))
