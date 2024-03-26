WELCOME TO Shira's project - Ideas to games

Have you ever found yourself reminiscing about your favorite childhood games?
My platform provides the perfect opportunity for gamers and game enthusiasts to contribute to the ever-evolving world of video gaming.

The purpose is to create an interactive platform where users can submit their ideas for video games.

Getting Started
To view the project, follow these steps:

Clone the repository to your local machine.
Navigate to the project directory.
Usage:
Running the Project:

Ensure that Docker and Docker Compose are installed on your system.
Navigate to the project directory in your terminal.
Run the command: docker-compose up --build
This will build and start the containers defined in the docker-compose.yml file.
Accessing the Application:

Once the containers are up and running, you can access the application through your web browser.
Visit the provided Network URL (e.g., http://192.168.160.4:8501) to view the Streamlit app.
Submitting Game Ideas:

In the Streamlit app, you'll find input fields where you can submit your game ideas.
Fill in the details such as the name of the game, platform, and main actions of the game.


Testing Individual Containers:
Backend Container:

To check the status and logs of the backend container:
bash

docker ps          # To get the container ID or name
docker logs <container_id or container_name>
Frontend Container:

To check the status and logs of the frontend container:
bash

docker ps          # To get the container ID or name
docker logs <container_id or container_name>
PostgreSQL Database Container:

To interact with the PostgreSQL database container:
bash

docker exec -it <container_id or container_name> psql -U postgres

