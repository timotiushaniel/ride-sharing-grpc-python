from concurrent import futures
import math
import logging

import grpc

from server import read_json

from proto import ride_sharing_pb2, ride_sharing_pb2_grpc

editedDriver = []


def get_user(user_db, point):
    for user in user_db:
        if user.location == point:
            return user
    return None


def get_user_latitude(self):
    for user in self.user:
        latitude = user.location.latitude
        return latitude


def get_user_longitude(self):
    for user in self.user:
        latitude = user.location.longitude
        return latitude


# Mendapatkan jarak antar daerah yang diberikan
def calculate_distance(lat1, lon1, lat2, lon2):
    coord_factor = 10000000.0
    lat_1 = lat1 / coord_factor
    lat_2 = lat2 / coord_factor
    lon_1 = lon1 / coord_factor
    lon_2 = lon2 / coord_factor
    lat_rad_1 = math.radians(lat_1)
    lat_rad_2 = math.radians(lat_2)
    delta_lat_rad = math.radians(lat_2 - lat_1)
    delta_lon_rad = math.radians(lon_2 - lon_1)

    # Formula is based on http://mathforum.org/library/drmath/view/51879.html
    a = (pow(math.sin(delta_lat_rad / 2), 2) +
         (math.cos(lat_rad_1) * math.cos(lat_rad_2) *
          pow(math.sin(delta_lon_rad / 2), 2)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 6371000  # Radius bumi dalam meter
    # metres
    return R * c


class RideShareServicer(ride_sharing_pb2_grpc.RideShareServicer):

    def __init__(self):
        self.driver = read_json.read_json_driver()
        self.user = read_json.read_json_user()

    def GetUserLocation(self, request, context):  # Fungsi untuk mendapatkan user sesuai dengan database
        user = get_user(self.user, request)  # Mengambil daerah dari file user.json lalu me-assign ke var user
        if user is None:  # Kalau user nya tidak ada
            return ride_sharing_pb2.User(user_id="", username="",
                                         location_name="", location=request)
        else:  # Kalau user nya ada
            xx = user
            return user  # Return user tersebut

    def ListDriver(self, request, context):
        left = min(request.lo.longitude, request.hi.longitude)
        right = max(request.lo.longitude, request.hi.longitude)
        top = max(request.lo.latitude, request.hi.latitude)
        bottom = min(request.lo.latitude, request.hi.latitude)
        for driver in self.driver:
            if (driver.location.longitude >= left and
                    driver.location.longitude <= right and
                    driver.location.latitude >= bottom and
                    driver.location.latitude <= top):
                driver_distance = calculate_distance(get_user_latitude(self), get_user_longitude(self),
                                                     driver.location.latitude,
                                                     driver.location.longitude)
                driver.distance = driver_distance
                test_distance = driver.distance
                yield driver

    def ChooseDriver(self, request_iterator, context):
        for message in request_iterator:
            print(message)
            yield message

    def GiveRating(self, request_iterator, context):
        for message in request_iterator:
            yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ride_sharing_pb2_grpc.add_RideShareServicer_to_server(
        RideShareServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
