import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]
        print(f"Loaded {len(self.db)} bookings from JSON")


    def GetBookingFromUserId(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.userid:
                print("Booking found !")

                return booking_pb2.BookingResponse(
                    userid = booking["userid"],
                    dates = booking["dates"]
                )

        return booking_pb2.BookingResponse(
            userid = "",
            dates = []
        )
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
