# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

import json
cards = []

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)

def flatten(l):
    return [item for sublist in l for item in sublist]

@app.route("/")
def render_homepage():
    # Request new bingo board
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=6
    )
    # Read response
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )

    cards = []
    for loop in recommendations_response.recommendations:
        cards.append(json.loads(loop.title))

    # Flatten to list of all numbers
    # https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    board=sum(flatten(cards), [])

    return render_template( "homepage.html", myboard=board,)
