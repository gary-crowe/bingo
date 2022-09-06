# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from bingo_pb2 import TicketRequest
from bingo_pb2_grpc import TicketsStub

app = Flask(__name__)

ticket_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
ticket_channel = grpc.insecure_channel(
    f"{ticket_host}:50051"
)
ticket_client = TicketsStub(ticket_channel)


@app.route("/")
def render_homepage():
    ticket_request = TicketRequest( user_id="Gary", no_of_tickets=1)
    ticket_response = ticket_client.Ticket(ticket_request)
    return render_template( "homepage.html", generatedticket=ticket_response.Ticket,)
