import grpc
from concurrent import futures
import json
import showtime_pb2
import showtime_pb2_grpc
from typing import List

from models import ShowTime

class ShowTimeServicer(showtime_pb2_grpc.ShowTimeServicer):
    
    def __init__(self) -> None:
        with open('{}/data/times.json'.format('.'),"r") as jsf:
            self.db : List[ShowTime] = json.load(jsf)["schedule"]
        print(f"Loaded {len(self.db)} schedule time from JSON")

    def GetShowTimeByDate(self, request, context):
        for showtime in self.db:
            if showtime['date'] == request.date:
                print("Showtime found !")
                return showtime_pb2.ShowTimeData(
                    date = showtime['date'],
                    movies = showtime['movies']
                )
        return showtime_pb2.ShowTimeData(
            date = "", movies = []
        )

    def GetShowTimes(self, request, context):
        for showtime in self.db:
            yield showtime_pb2.ShowTimeData(
                date=showtime['date'],  
                movies=showtime['movies']
            )
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowTimeServicer_to_server(ShowTimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
    