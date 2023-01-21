# Setup Apache Superset via Docker-compose and config embedded Dashboard

1. Clone current repository
```bash
git clone https://github.com/zhaoyongjie/superset-containerization.git
```

2. Startup Superset via docker-compose, notice that 1)There are some environment variables to declare in the `docker/.env-non-dev`. 2) the file `superset_home/superset_config.py` will override the `config.py` and read Database and Redis config from the `docker/.env-non-dev`.

```
cd superset-containerization
docker compose up -d
```

3. Use account `admin`/`admin` to login Superset.

4. Add a `Gamma` role to `admin` user.

5. Generate Embedded dashboard uuid. Click `embed dashboard` on the three dots in a dashboard. Notice that `Allowed Domains` in the `embed` model could leave empty first.

6. Get `guest_token` for embedded dashboard. To make it easier to generate http requests, we use the `httpie` to request

```bash
# request a JWT token for admin user
echo '{"password": "admin", "username": "admin", "provider": "db"}' | http post http://localhost:8088/api/v1/security/login

# request a guest token for embedded dashboard
echo '{"user": {"username": "admin"}, "resources": [{"type": "dashboard", "id": "<fill up a dashboard id>"}], "rls": []}' | http post http://localhost:8088/api/v1/security/guest_token/ -A bearer -a "<fill up JWT token from previous step>"
```

7. fill `embedded uuid` and `guest token` in `embedded_superset/src/App.jsx`

8. run `npm i` in `embedded_superset`

9. run `npm run build` in `embedded_superset`

10. open a http server in `embedded_superset/dist`
```bash
cd embedded_superset/dist
python3 -m http.server 5000
```

11. open a browser and explore `localhost:5000`, the embedded dashboard should be showed.





