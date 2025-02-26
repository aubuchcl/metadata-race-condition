FROM alpine
VOLUME /root/temp/data
RUN apk add --update python3 py3-pip
WORKDIR /app
COPY . .
ENTRYPOINT ["entrypoint.sh"]
CMD ["/bin/sh"]
