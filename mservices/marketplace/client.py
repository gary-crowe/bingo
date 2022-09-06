# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from bingo_pb2 import BookCategory, TicketRequest
from bingo_pb2_grpc import GenerationsStub

app = Flask(__name__)

generatedtickets_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
generatedtickets_channel = grpc.insecure_channel(
    f"{generatedtickets_host}:50051"
)
generatedtickets_client = GenerationsStub(generatedtickets_channel)


@app.route("/")
def render_homepage():
    generatedtickets_request = TicketRequest(
        user_id="gary", category=BookCategory.MYSTERY, max_cards=3)

    generatedtickets_response = generatedtickets_client.Generate(
        generatedtickets_request
    )

    return render_template(
        "homepage.html",
        generatedtickets=generatedtickets_response.generatedtickets,
    )
