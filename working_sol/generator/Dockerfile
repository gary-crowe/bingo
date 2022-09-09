FROM python
LABEL description="Bingo Ticket Generator" \
      version="0.1" \
      creationDate="09-09-2022"

USER 1001

RUN mkdir /usr/src/app
RUN chgrp -R 1001 /usr/src/app && \
    chmod -R g=u /usr/src/app

COPY protobufs/ /usr/src/app/protobufs/
COPY generator/ /usr/src/app/generator/
WORKDIR /usr/src/app/generator
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]
