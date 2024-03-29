# 🎮 Welcome to Shira's Project - Ideas to Games! 🕹️
Are you longing for the good old days of your favorite childhood games? 
Well, you're lucky!
My platform offers an exciting opportunity for gamers and enthusiasts to contribute to the ever-evolving world of video gaming.

The aim is simple: to create an interactive space where users can submit their imaginative ideas for video games.

## Getting Started 🚀
To dive into the project, follow these simple steps:

1 .Clone the Repository: 
  Grab a copy of the repository to your local machine.


  
2. Navigate to the Project Directory: Move to the project directory in your terminal.

## Usage 🎮
To run the project:

1.Make sure you have Docker and Docker Compose installed on your system.
2.Navigate to the Project Directory: 
3.Head over to the project directory in your terminal.
4.Run the Command: 
  docker-compose up

This will build and start the containers defined in the docker-compose.yml file.


## Accessing the Application 🌐

Once the containers are up and running, you can access the application through your web browser:

Visit the Provided Network URL: Go to the provided Network URL (e.g., http://localhost:8501) to view the Streamlit app.
Submitting Game Ideas 🎮💡
In the Streamlit app, you'll discover intuitive input fields where you can submit your brilliant game ideas. Simply fill in the details such as the name of the game, platform, and main actions of the game.

## Testing Individual Containers 🛠️
Backend Container:
To check the status and logs of the backend container, use the following commands:

bash
Copy code
docker ps # To get the container ID or name
docker logs <container_id or container_name>
Frontend Container:
To check the status and logs of the frontend container, use the following commands:

bash
Copy code
docker ps # To get the container ID or name
docker logs <container_id or container_name>
PostgreSQL Database Container:
To interact with the PostgreSQL database container, use the following command:

bash
Copy code
docker exec -it <container_id or container_name> psql -U postgres

