import streamlit as st
import requests

def fetch_game_data():
    url = "http://localhost:8501/game/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Failed to fetch game data from the server.")
        return None

def main():
    st.set_page_config(page_title="My Gaming Store", layout="wide")

    st.subheader("Welcome to My Gaming Store! :video_game:")
    st.write("Explore our collection of video games.")

    game_data = fetch_game_data()

    if game_data:
        st.write("Game Data:")
        st.write(game_data)
    else:
        st.warning("No game data available.")

if __name__ == "__main__":
    main()
