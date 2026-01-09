# TeamProject_Ergo2
Codebase for team project Experiential learning in immersive nature

- Tomas Rojka 
- Maxim Rooms 
- Gražvydas Stalmokas

Creating an immersive 3D environment with voice commands in a 360° projector room.

# Getting started
1) Generate a self-signed ssl certificate for your localhost using nginx
```openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout fastapi.key -out fastapi.crt```
place the fastapi.crt and fastapi.key files in a new folder /server/nginx/ssl/
(This is required so the Unity program trusts the server connection)

2) Navigate into the server folder: ```cd``` server and build/run the docker compose stack: ```docker-compose up --build```
2.1) Prerequisites: Docker Desktop installed: https://docs.docker.com/desktop/setup/install/windows-install/
2.2) Prerequisites: Ollama installed: https://ollama.com/download
2.3) Prerequisites: Ollama must have the model for the llm interpretation, you can download this by running ```ollama pull llama3.2:3b``` in a command line. Ollama must be running the endpoint for the model, do this by running ```ollama serve``` in the command line.

3) Once the server is running you can connect using the Unity project by entering your local ip in the input at the main menu
3.1) To know your local ip type ```ipconfig``` in the command line for Windows, ```ipconfig getifaddr en0``` in the terminal for Mac, or ```ifconfig``` on Linux
3.2) Local ips usually have this structure: 192.168.x.x or 172.x.x.x or 10.x.x.x