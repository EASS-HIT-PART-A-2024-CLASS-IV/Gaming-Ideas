import streamlit as st

# Streamlit UI code
def main():
    st.title("Welcome to my Video Gaming store")
    st.write("Write the newest game you would like to buy:")
    new_game = st.text_input("New Game")
    if st.button("Submit"):
        st.write(f"New game submitted: {new_game}")

if __name__ == "__main__":
    main()
