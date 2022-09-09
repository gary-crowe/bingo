FROM python
LABEL description="Bingo Ticket Generator" \
      version="0.1" \
      creationDate="09-09-2022"

USER 1001

RUN mkdir /service
RUN chgrp -R 1001 /service && \
    chmod -R g=u /service

COPY protobufs/ /service/protobufs/
COPY generator/ /service/generator/
WORKDIR /service/generator
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]
