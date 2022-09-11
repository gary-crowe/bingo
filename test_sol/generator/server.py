# generated/generated.py
from concurrent import futures
import random
import numpy as np
import grpc
import tabulate

from generated_pb2 import (
    BingoCategory,
    BingoTicket,
    BingoTicketResponse,
)
import generated_pb2_grpc

# #######################
# Generate the bingo card. At the moment just a single card. Need to parse number required.
# #######################

# Add function to generate USA, Words & Pictures player card

def genUK():
    ticket =np.full(27,1).reshape(9,3)
    ticket[:4,:] *=0
    [np.random.shuffle(ticket[:,i]) for i in range(3)]
    for i in range(9):
        nums =np.arange(1+10*i,11+10*i)
        np.random.shuffle(nums)
        ticket[i,:] *= np.sort(nums[:3])
    return(np.array2string(ticket.T, separator=','))

class TicketsationService(generated_pb2_grpc.GeneratedServicer):
    def Tickets(self, request, context):
        # Add logic here for Pictures and words bingo
        tickets_by_category = {
            BingoCategory.UKBINGO: [
                BingoTicket(id=1, title=str(genUK())),
                BingoTicket(id=2, title=str(genUK())),
                BingoTicket(id=3, title=str(genUK())), 
                BingoTicket(id=4, title=str(genUK())), 
                BingoTicket(id=5, title=str(genUK())), 
                BingoTicket(id=6, title=str(genUK())), 
            ],
            BingoCategory.USBingo: [
                BingoTicket(id=1, title=str(genUK())),
                BingoTicket(id=2, title=str(genUK())),
                BingoTicket(id=3, title=str(genUK())), 
                BingoTicket(id=4, title=str(genUK())), 
                BingoTicket(id=5, title=str(genUK())), 
            ],
        }

#       tickets_for_category = tickets_by_category[request.category]
        tickets_for_category = tickets_by_category[BingoCategory.UKBINGO]
        num_results = min(request.max_results, len(tickets_for_category))
        players_tickets = random.sample(
            tickets_for_category, num_results
        )

        return BingoTicketResponse(generated=players_tickets)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    generated_pb2_grpc.add_GeneratedServicer_to_server(
        TicketsationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
