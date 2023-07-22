FROM nginx:1.25.1-alpine
COPY default.conf /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/static
COPY static /var/www/static
RUN chown -R nginx:nginx /var/www/static