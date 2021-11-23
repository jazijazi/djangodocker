FROM nginx:latest

#RUN groupadd -r jazi && useradd -g jazi jazi && \
#    chown -R jazi:jazi /var /etc/nginx
#USER jazi

# install curl for healthcheck
RUN apt-get update && apt-get install -y curl \
        && rm -rf /var/lib/apt/lists/*
HEALTHCHECK --interval=20s --timeout=10s --start-period=5s --retries=3 \
        CMD curl --fail http://localhost:80 || exit 1

RUN rm /etc/nginx/conf.d/default.conf
ADD default.conf /etc/nginx/conf.d/default.conf