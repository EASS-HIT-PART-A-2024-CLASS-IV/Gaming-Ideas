import streamlit as st
import requests


def main():
    st.title("Welcome to my Video Gaming store")
    st.write("Write the newest game you would like to buy:")
    new_game = st.text_input("New Game")
    if st.button("Submit"):
        response = requests.post('http://backend:8000/games/', json={'name': new_game})
        if response.status_code == 200:
            st.success("New game submitted successfully!")
        else:
            st.error(f"An error occurred while submitting the game: {response.text}")

if __name__ == "__main__":
    main()

