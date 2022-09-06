# recommendations/recommendations.py
from concurrent import futures
import random
import grpc
import tabulate
import numpy as np

from bingo_pb2 import (
    TicketCreate,
    TicketResponse
)

import bingo_pb2_grpc

def gen():
    ticket =np.full(27,1).reshape(9,3)
    ticket[:4,:] *=0
    [np.random.shuffle(ticket[:,i]) for i in range(3)]
    for i in range(9):
        nums =np.arange(1+10*i,11+10*i)
        np.random.shuffle(nums)
        ticket[i,:] *= np.sort(nums[:3])
    print(tabulate.tabulate(ticket.T))

class TicketService(bingo_pb2_grpc.TicketsServicer):
    def Recommend(self, user_id, no_of_tickets):

        board = gen()  # Generate ticket need to process number here

        return TicketResponse(ticketgenerated=board)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bingo_pb2_grpc.add_TicketsServicer_to_server(
        TicketService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
