# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

import json
# json.loads(s)
# [[0, 11, 22, 0, 0, 51, 62, 0, 85], [3, 0, 0, 36, 48, 54, 64, 0, 0], [0, 18, 30, 39, 0, 0, 67, 0, 87]]

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=6
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )

    tickets=recommendations_response.recommendations
    for loop in tickets:
        print(json.loads(loop))

    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations,
    )
