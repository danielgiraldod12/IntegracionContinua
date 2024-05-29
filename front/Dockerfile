FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY index.html /usr/share/nginx/html/
COPY index.js /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]