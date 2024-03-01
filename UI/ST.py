import streamlit as st
import requests

def fetch_game_price(game, platform, edition):
    response = requests.post("http://backend:8000/get_game_price", json={"game": game, "platform": platform, "edition": edition})
    return response.json()

def main():
    st.set_page_config(page_title="Gaming Store UI", layout="wide")
    st.title("Welcome to Our Gaming Store")

    st.markdown("## Explore Our Collection :video_game:")
    st.write("Get ready for an epic gaming experience!")

    game = st.selectbox("Select a game", ["FIFA 24", "Call of Duty: Warzone", "LOL"])
    platform = st.text_input("Enter platform (PC, PS4, Xbox)")
    edition = st.text_input("Enter edition (standard, deluxe, etc.)")

    if st.button("Get Price"):
        price_info = fetch_game_price(game, platform, edition)
        st.write(f"Price for {game} ({edition}) on {platform}: ${price_info['price']} - {price_info['message']}")

    st.markdown("## Game Recommendations")
    st.write("Can't decide what to play? Check out our recommendations below:")
    st.write("- **FIFA 24**: Experience the thrill of football like never before.")
    st.write("- **Call of Duty: Warzone**: Immerse yourself in intense combat action.")
    st.write("- **League of Legends**: Join millions of players in this popular MOBA.")

    st.markdown("## Contact Us")
    st.write("Have questions or need assistance? Reach out to our support team:")
    st.write("- Email: support@gamingstore.com")
    st.write("- Phone: 1-800-GAME-HELP")

    st.markdown("---")
    st.write("© 2024 Gaming Store. All rights reserved.")

if __name__ == "__main__":
    main()

    
