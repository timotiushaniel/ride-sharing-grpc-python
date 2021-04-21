import json
from proto import ride_sharing_pb2


def read_json_driver():
    """Reads the route guide database.

  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  """
    driver_list = []
    with open("driver.json") as raw_data_file:
        for item in json.load(raw_data_file):
            driver = ride_sharing_pb2.Driver(
                driver_id=item["driver_id"],
                driver_name=item["driver_name"],
                car=item["car"],
                police_number=item["police_number"],
                rating=item["rating"],
                availability=item["availability"],
                location=ride_sharing_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"]),
                location_name=item["location_name"],
                distance=item["distance"]
            )
            driver_list.append(driver)
    # print(driver_list)
    return driver_list


def read_json_user():
    """Reads the route guide database.

  Returns:
    The full contents of the route guide database as a sequence of
      route_guide_pb2.Features.
  """
    user_list = []
    with open("user.json") as user_raw_data_file:
        for item in json.load(user_raw_data_file):
            user = ride_sharing_pb2.User(
                user_id=item["user_id"],
                username=item["username"],
                location=ride_sharing_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"]),
                location_name=item["location_name"]
            )
            user_list.append(user)
    # print(user_list)
    return user_list


# if __name__ == '__main__':
#     read_json()
#     read_json_user()
