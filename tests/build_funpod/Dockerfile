FROM python:2.7

ENV DOCKER=1 \
    DOCKER_BRIDGE_IP=  \
    JOBLIB_TEMP_FOLDER=/tmp/joblib \
    RUNDIR=/app

# create unprivileged user
# RUN adduser -D -g '' myuser

RUN test -d $JOBLIB_TEMP_FOLDER || mkdir -p $JOBLIB_TEMP_FOLDER && \
    test -d $RUNDIR || mkdir -p $RUNDIR

COPY ./ $RUNDIR
RUN pip install --upgrade docker mlpods


# tell the port number the container should expose
EXPOSE 9998


WORKDIR $RUNDIR

CMD ./run.sh
