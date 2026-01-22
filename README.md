# TeamProject_Ergo2
Codebase for team project Experiential learning in immersive nature

- Tomas Rojka 
- Maxim Rooms 
- Gražvydas Stalmokas

Creating an immersive 3D environment with voice commands in a 360° projector room.

# Getting started
## Required programs
- Install openssl https://slproweb.com/products/Win32OpenSSL.html (Needed for generating our ssl certificate)
- Install Docker Desktop https://docs.docker.com/get-started/introduction/get-docker-desktop/ (Needed for running our container image applications that process the speech-to-text)
- Install Ollama https://ollama.com/download (Needed to run our large language model locally on the separate computer that also has Docker)
- Install Ollama large language model: after installing Ollama you can open your terminal and type ```ollama pull llama3.2:3b``` to download, wait until this is complete. After installing you can start the large language model service using ```ollama serve``` in the terminal

## Setting up the backend
1. Generate a self-signed ssl certificate for your localhost for nginx using this command that generates a key and a certificate that is signed by you to tell Unity the connection is safe. 
Run the install file, only option that matters is to copy OpenSSL DLLs to the OpenSSL binaries directory.
Open terminal in administrator.
Go to install directory (cd "C:\Program Files\OpenSSL-Win64\bin") to run the command for generating our certificates.
This certificate and key stay valid for the number of days specified in the command after the argument -days.
```openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout fastapi.key -out fastapi.crt```
Press enter for all questions except for the common name, which should be: "localhost".
Place the fastapi.crt and fastapi.key files in a new folder /server/nginx/ssl/.

2. Clone this repository if you haven't already, into an empty folder: e.g. /experiential learning/ using the terminal with the command ```git clone https://github.com/StalmokasGrazvydas/TeamProject_Ergo2.git```

3. Navigate into the server folder: ```cd TeamProject_Ergo2/server```  and build/run the docker compose stack: ```docker-compose up --build```
  3.1 You only have to build once for the first time you run the project. Afterwards you can start/stop the backend within the Docker Desktop program.

## Setting up the frontend
4. Once the server is running you can connect using the Unity project by entering your local ip in the input at the main menu
  4.1. To know your local ip type ```ipconfig``` in the command line for Windows, ```ipconfig getifaddr en0``` in the terminal for Mac, or ```ifconfig``` on Linux
  4.2. Local ips usually have this structure: 192.168.x.x or 172.x.x.x or 10.x.x.x