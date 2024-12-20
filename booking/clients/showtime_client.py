import grpc
import showtime_pb2
import showtime_pb2_grpc
import os 

class ShowtimeClient:
    """
    Client for interacting with the ShowTime gRPC service.
    """
    def __init__(self):
        self.SHOWTIME_URL = os.getenv("SHOWTIME_CLIENT")
        self.channel = grpc.insecure_channel(self.SHOWTIME_URL)
        self.stub = showtime_pb2_grpc.ShowTimeStub(self.channel)

    def get_showtime_by_date(self, date: str):
        """
        Retrieves showtime data for a specific date.
        """
        showtime_request = showtime_pb2.ShowTimeDate(date=date)
        try:
            return self.stub.GetShowTimeByDate(showtime_request, timeout=10)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise ValueError("Showtimes not found for the given date")
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                raise ConnectionError("ShowTime service is unavailable")
            else:
                raise Exception(f"Failed to retrieve showtimes: {e.details()}")