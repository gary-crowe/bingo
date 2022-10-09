# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from generated_pb2 import BingoCategory, TicketRequest
from generated_pb2_grpc import GeneratedStub

import json
import itertools

#define our variables
cards = []

player_name = ""        # Populate with player name
ticket_type = "UKBINGO" # Populate with type of card required

app = Flask(__name__)

generated_host = os.getenv("GENERATOR_HOST", "localhost")
generated_channel = grpc.insecure_channel(
    f"{generated_host}:50051"
)
generated_client = GeneratedStub(generated_channel)

# Define our functions here
def flatten(l):
    return [item for sublist in l for item in sublist]

@app.route("/")
def render_homepage():
    # Request new bingo board
    generated_request = TicketRequest(
        user_id=1, category=BingoCategory.UKBINGO, max_results=6
    )
    # Read response
    generated_response = generated_client.Tickets(
        generated_request
    )

    cards = []
    for loop in generated_response.generated:
        cards.append(json.loads(loop.title))

    # Flatten to list of all numbers
    board=sum(flatten(cards), [])

    return render_template( "homepage.html", myboard=list(itertools.chain.from_iterable(board)))
