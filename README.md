# SNMP collector project 

This is a project for course ETRS011 in master 2 at USMB.
Link to the app : `https://github.com/NicolasBoulard/soup`

## How to use this app ?
Just go to `http://{you ip}/`, then login and enter you're host/services

### Without docker
1. Clone this repo `git clone https://github.com/Dede1441/electric_roadapp_etrs013.git`
2. Create venv `python -m venv .venv`
3. Activate venv `.venv\Script\Activate`
4. Install requirements `pip install -r requirements.txt`
5. Launch The APP
4. Run the collektor : `python snmp_interrogate.py`


### With docker 🐋
1. Build collecktor : `docker build . --tag souptor-collektor`
2. Run containers : `docker container start souptor-collektor`


### Simulated clients
If you have no snmp equipements to supervise, you can use the docker-compose in simulated-client : `docker-compose up -d` 
This will startup 2 ubuntu container with the snmpv2 open on your host port 162 & 163, with the community **soup**.