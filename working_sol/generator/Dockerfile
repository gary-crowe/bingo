FROM registry.fedoraproject.org/f33/python3

LABEL description="Bingo Ticket Generator" \
      version="0.1" \
      creationDate="09-09-2022"

USER 0
COPY . ./

RUN chown -R 1001:0 ./
USER 1001

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]
