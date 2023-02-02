# Summary

This project intends to do 3 key goals:
1. Query MongoDB through Apache Superset 2.0.1
2. Create an embedded dashboard and a demonstration how to do it through a React App
3. Build a simple and reusable docker-compose file so that quick start a Superset instance with Trino

# Steps 

1. Clone current repository
    ```bash
    git clone https://github.com/zhaoyongjie/superset-containerization.git
    ```
2. edit `mongodb.connection-url` in `docker/mongodb.properties`, fills up corresponding mongodb URI. 
3. Startup Superset via docker-compose, notice that 1)There are some environment variables to declare in the `docker/.env-non-dev`. 2) the file `superset_home/superset_config.py` will override the `config.py` and read Database and Redis config from the `docker/.env-non-dev`.
    ```
    cd superset-containerization
    docker compose up -d
    ```
4. Use account `admin`/`admin` to login Superset.
5. Create a new Database in Superset, the SQLAlchemy URI is `trino://admin@trino:8080/mongodb`.
6. Add a `Gamma` role to `admin` user.
7. Generate Embedded dashboard uuid. Click `embed dashboard` on the three dots in a dashboard. Notice that `Allowed Domains` in the `embed` model could leave empty first.
8. Get `guest_token` for embedded dashboard. To make it easier to generate http requests, we use the `httpie` to request
    ```bash
    # request a JWT token for admin user
    echo '{"password": "admin", "username": "admin", "provider": "db"}' | http post http://localhost:8088/api/v1/security/login
    
    # request a guest token for embedded dashboard
    echo '{"user": {"username": "admin"}, "resources": [{"type": "dashboard", "id": "<fill up a dashboard id>"}], "rls": []}' | http post http://localhost:8088/api/v1/security/guest_token/ -A bearer -a "<fill up JWT token from previous step>"
    ```
9. fill `embedded uuid` and `guest token` in `embedded_superset/src/App.jsx`
10. run `npm i` in `embedded_superset`
11. run `npm run build` in `embedded_superset`
12. open a http server in `embedded_superset/dist`
    ```bash
    cd embedded_superset/dist
    python3 -m http.server 5000
    ```
13. open a browser and explore `localhost:5000`, the embedded dashboard should be showed.
