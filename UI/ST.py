import streamlit as st
import psycopg2
import pandas as pd


def fetch_data():
    con = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="postgresdb"   
    )
    query = "SELECT * FROM games"
    df = pd.read_sql(query, con=con)
    con.close() 
    return df


def main():
    st.set_page_config(page_title="Gaming Store UI", layout="wide")
    st.title("Welcome to Our Gaming Store")

    st.markdown("## Explore Our Collection :video_game:")
    st.write("Get ready for an epic gaming experience!")

    df = fetch_data()
    st.write("## Games Catalog:")
    st.write(df)

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
