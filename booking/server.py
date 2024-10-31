import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json
from models import Booking, BookingDate
from typing import List

import showtime_pb2_grpc
import showtime_pb2
from grpc_reflection.v1alpha import reflection


SHOWTIME_URL = "localhost:3002"

def write(bookings):
   data =  {
      "bookings" : bookings
   }
   with open('{}/data/bookings.json'.format("."), 'w') as f:
      json.dump(data, f, indent=2)

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db : List[Booking] = json.load(jsf)["bookings"]
        print(f"Loaded {len(self.db)} bookings from JSON")

        self.showtime_channel = grpc.insecure_channel(SHOWTIME_URL)
        self.showtime_stub = showtime_pb2_grpc.ShowTimeStub(self.showtime_channel)


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
    
    def GetBookings(self, request, context):
        print("Get All Bookings")
        for booking in self.db:
            yield booking_pb2.BookingResponse(
                userid = booking["userid"],
                dates = booking["dates"]
            )

    def AddBookingByUser(self, request, context):
        print("Add Booking by User")
        userid = request.userid

        showtime_request = showtime_pb2.ShowTimeDate(date=request.date)
        try:
            showtime_response = self.showtime_stub.GetShowTimeByDate(showtime_request, timeout = 10)
            print("Showtime response received:")
            print(showtime_response.date)
            print(showtime_response.movies)
            
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                return booking_pb2.AddBookingResponse(
                    status="error",
                    message="Showtimes not found for the given date"
                )
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                return booking_pb2.AddBookingResponse(
                    status="error",
                    message="ShowTime service is unavailable"
                )
            else:
                return booking_pb2.AddBookingResponse(
                    status="error",
                    message=f"Failed to retrieve showtimes: {e.details()}"
                )

        current_user = next((b for b in self.db if b['userid'] == userid), None)
        if not current_user:
            return booking_pb2.AddBookingResponse(
                status="error",
                message="User not found"
            )
        
        for booking in self.db:
            for i,date in enumerate(booking["dates"]):
                if date["date"] == str(showtime_response.date):
                    for movie_id in date["movies"]:
                        if movie_id == request.movieid:
                            return booking_pb2.AddBookingResponse(
                                status="error",
                                message="An existing booking already exists"
                            )
                    
                    if booking == current_user:
                        current_user["dates"][i]["movies"].append(request.movieid)
                        # write in json here
                        write(self.db)
                        return booking_pb2.AddBookingResponse(
                            status="success",
                            message="Booking created"
                        )
                    

        current_user["dates"].append({
            "date" : request.date,
            "movies": [request.movieid]
        })
        write(self.db)
        return booking_pb2.AddBookingResponse(
            status="success",
            message="Booking created"
        )

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    
    
    SERVICE_NAMES = (
        booking_pb2.DESCRIPTOR.services_by_name['Booking'].full_name,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
