FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /etc/nginx/ssl
RUN chmod 700 /etc/nginx/ssl
COPY ssl /etc/nginx/ssl
