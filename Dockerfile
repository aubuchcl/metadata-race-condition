FROM alpine
VOLUME /root/temp/data
RUN apk add --update python3 py3-pip py3-deepdiff
WORKDIR /app
COPY . .
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["/bin/sh"]
