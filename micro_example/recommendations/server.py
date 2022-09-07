# recommendations/recommendations.py
from concurrent import futures
import random
import numpy as np
import grpc
import tabulate

from recommendations_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse,
)
import recommendations_pb2_grpc

# #######################
# Generate the bingo card. At the moment just a single card. Need to parse number required.
# #######################

def gen():
    ticket =np.full(27,1).reshape(9,3)
    ticket[:4,:] *=0
    [np.random.shuffle(ticket[:,i]) for i in range(3)]
    for i in range(9):
        nums =np.arange(1+10*i,11+10*i)
        np.random.shuffle(nums)
        ticket[i,:] *= np.sort(nums[:3])
    return(np.array2string(ticket.T, separator=','))
    #return(tabulate.tabulate(ticket.T))
    #return (ticket.T)

class RecommendationService(
    recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        books_by_category = {
            BookCategory.MYSTERY: [
                BookRecommendation(id=1, title=str(gen())),
                BookRecommendation(id=2, title=str(gen())),
                BookRecommendation(id=3, title=str(gen())), 
                BookRecommendation(id=4, title=str(gen())), 
                BookRecommendation(id=5, title=str(gen())), 
                BookRecommendation(id=6, title=str(gen())), 
            ],
        }

#       books_for_category = books_by_category[request.category]
        books_for_category = books_by_category[BookCategory.MYSTERY]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(
            books_for_category, num_results
        )

        return RecommendationResponse(recommendations=books_to_recommend)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
