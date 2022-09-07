# generatedtickets/generatedtickets.py
from concurrent import futures
import numpy as np
import random
import grpc
import tabulate

from bingo_pb2 import (
    TicketGeneration,
    TicketResponse,
)
import bingo_pb2_grpc

# Generate the bingo card. At the moment just a single card. Need to parse number required.

def gen():
    ticket =np.full(27,1).reshape(9,3)
    ticket[:4,:] *=0
    [np.random.shuffle(ticket[:,i]) for i in range(3)]
    for i in range(9):
        nums =np.arange(1+10*i,11+10*i)
        np.random.shuffle(nums)
        ticket[i,:] *= np.sort(nums[:3])
    print(ticket.T)
    return("This is the string")
#   return (ticket.T)

# 
class GenerateationService( bingo_pb2_grpc.GenerationsServicer):
    def Generate(self, request, context):

        board=TicketGeneration(card1=gen(),card2=gen())
        return TicketResponse(generatedtickets=board)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bingo_pb2_grpc.add_GenerationsServicer_to_server(
        GenerateationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
