# marketplace/marketplace.py

from flask import Flask, render_template
import grpc

from generated_pb2 import BingoCategory, TicketRequest
from generated_pb2_grpc import GeneratedStub

import os
import json
import itertools

#define our variables
cards = []

player_name = "Gary"    # Populate with player name
ticket_type = "UKBINGO" # Populate with type of card required

app = Flask(__name__)

generated_host = os.getenv("GENERATOR_HOST", "localhost")   # Assume localhost unless var is set
generated_channel = grpc.insecure_channel(
    f"{generated_host}:50051"
)
generated_client = GeneratedStub(generated_channel)

# Define our functions here
def flatten(l):
    return [item for sublist in l for item in sublist]

# ################# #
# Main landing page
# ################# #
@app.route("/")
def render_homepage():
    # Request new bingo board
    generated_request = TicketRequest(
        user_id=1, category=BingoCategory.UKBINGO
    )
    # Read response
    generated_response = generated_client.Tickets(
        generated_request
    )

    cards = []
    print(generated_response.generated)
    for loop in generated_response.generated:
        cards.append(json.loads(loop.title))

    # Flatten to list of all numbers
    board=sum(flatten(cards), [])

    # Pass 1, very big, 1d list of numbers
    return render_template( "homepage.html", myboard=list(itertools.chain.from_iterable(board)))

@app.route("/usa")
def render_usabingo():
    # Request new bingo board
    generated_request = TicketRequest(
        user_id=1, category=BingoCategory.USBINGO
    )
    # Read response
    generated_response = generated_client.Tickets(
        generated_request
    )

    cards = []
    for loop in generated_response.generated:
        cards.append(json.loads(loop.title))

    board=sum(flatten(cards), [])

    return render_template( "usa.html", myboard=board)

@app.route("/images")
def render_imagesbingo():
    # Request new bingo board
    generated_request = TicketRequest(
        user_id=1, category=BingoCategory.IMAGES
    )
    # Read response
    generated_response = generated_client.Tickets(
        generated_request
    )

    cards = []
    for loop in generated_response.generated:
        cards.append(json.loads(loop.title))

    board=sum(flatten(cards), [])

    return render_template( "images.html", myboard=board)
