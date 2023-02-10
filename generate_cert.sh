# reference: https://mindsers.blog/post/https-using-nginx-certbot-docker/

docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d <example.org>