from __future__ import print_function

import logging

import grpc
from proto import ride_sharing_pb2, ride_sharing_pb2_grpc

driverId = []
driverName = []
driverCar = []
driverPoliceNo = []
driverAvail = []
driverRating = []
driverLocation = []
driverDist = []

messageToServer = []
ratingForDriver = []


def get_user(stub, point):
    user = stub.GetUserLocation(point)  # Mengambil nama lokasi dan me-assign ke var feature
    if not user.location:
        print("Server returned incomplete location")
        return

    if user.location_name:
        print("User Name: %s" % (user.username))
        print("Location: %s \n" % (user.location_name))

    else:
        print("Unknown user")


def set_user_location(stub):
    get_user(stub, ride_sharing_pb2.Point(latitude=-69169245,
                                          longitude=1076120849))


def list_driver(stub):
    rectangle = ride_sharing_pb2.Rectangle(
        lo=ride_sharing_pb2.Point(latitude=-70000000, longitude=1000000000),
        hi=ride_sharing_pb2.Point(latitude=-60000000, longitude=1100000000))
    # print("Looking for features between -7, 100 and -6, 110")

    drivers = stub.ListDriver(rectangle)
    driverDistTemp = driverDist
    for driver in drivers:
        driverId.append(driver.driver_id)
        driverName.append(driver.driver_name)
        driverCar.append(driver.car)
        driverPoliceNo.append(driver.police_number)
        driverAvail.append(driver.availability)
        driverRating.append(driver.rating)
        driverLocation.append(driver.location_name)
        driverDist.append(driver.distance)

        print("Driver " + str(driver.driver_id))
        print("Driver Name: %s" % (driver.driver_name))
        print("Driver Car: %s (%s)" % (driver.car, driver.police_number))
        print("Availability: %r " % (driver.availability))
        print("Rating: %f" % (driver.rating))
        print("Location at %s" % (driver.location_name))
        print("Distance: %i meters \n" % int((driver.distance)))

    tempDist = 0.0
    nearestDriverIndex = 0
    nearestDistance = 0.0
    sortedDist = sorted(driverDistTemp)
    for i in range(len(driverDist)):
        if driverDist[i] > sortedDist[0]:
            tempDist = driverDist[i]
        else:
            distance = driverDist[i]
            tempDist = distance
            nearestDriverIndex = i
            nearestDistance = distance
            break

    print("\n-------------- Nearest Driver --------------")
    print("Driver " + str(driverId[nearestDriverIndex]))
    print("Driver Name: %s" % (driverName[nearestDriverIndex]))
    print("Driver Car: %s (%s)" % (driverCar[nearestDriverIndex], driverPoliceNo[nearestDriverIndex]))
    print("Availability: %r " % (driverAvail[nearestDriverIndex]))
    print("Rating: %f" % (driverRating[nearestDriverIndex]))
    print("Location at %s" % (driverLocation[nearestDriverIndex]))
    print("Distance: %i meters \n" % int(nearestDistance))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ride_sharing_pb2_grpc.RideShareStub(channel)
        print("-------------- Your Location --------------")
        set_user_location(stub)
        print("-------------- Driver List --------------")
        list_driver(stub)

        endTrip = "no"
        while endTrip != 'yes':
            driverChosen = int(input("Choose the driver: "))
            # driverChosen = 2
            print("You choose driver: " + str(driverChosen))

            print("-------------- Your Driver Data --------------")
            print("Driver %s" % (driverId[driverChosen - 1]))
            print("Driver Name: %s" % (driverName[driverChosen - 1]))
            print("Driver Car: %s (%s)" % (driverCar[driverChosen - 1], driverPoliceNo[driverChosen - 1]))
            print("Availability: %r " % (driverAvail[driverChosen - 1]))
            print("Rating: %f" % (driverRating[driverChosen - 1]))
            print("Location at %s" % (driverLocation[driverChosen - 1]))
            print("Distance: %i meters \n" % int(driverDist[driverChosen - 1]))

            messageToServer.append(driverName[driverChosen - 1])
            messageToServer.append(str(driverDist[driverChosen - 1]))
            messageToServer.append(str(driverId[driverChosen - 1]))

            server_response_driver(stub)

            endTrip = input("Finish your trip (yes/no): ")
            # endTrip = "yes"
            if endTrip == "yes":
                ratingInput = int(input("Rate our driver rating (1-5): "))
                ratingForDriver.append(driverName[driverChosen - 1])
                ratingForDriver.append(str(ratingInput))
                ratingForDriver.append(str(driverRating[driverChosen - 1]))
                server_response_rating(stub)
            else:
                messageToServer.clear()
                ratingForDriver.clear()


def choose_driver(message):
    return ride_sharing_pb2.DriverChosen(
        message=message
    )


def finalize_driver():
    messages = []
    for i in range(len(messageToServer)):
        messages.append(choose_driver(messageToServer[i]))
    for msg in messages:
        # print("Hello Server Sending you the %s" % msg.message)
        yield msg


def server_response_driver(stub):
    responses = stub.ChooseDriver(finalize_driver())
    index = 0
    for response in responses:
        if index == 0:
            print("Our Driver, %s, already on the way to you." % response.message)
            index += 1
        elif index == 1:
            estimatedTimeArrival = int(float(response.message) / 60)
            print("We will arrive in %i minutes.\n" % estimatedTimeArrival)
            index += 1
        else:
            print("")
            index += 1


def make_rating(message):
    return ride_sharing_pb2.RatingGiven(
        message=message
    )


def send_rating():
    messages = []
    for i in range(len(ratingForDriver)):
        messages.append(make_rating(ratingForDriver[i]))
    for msg in messages:
        # print("Hello Server Sending you the %s" % msg.message)
        yield msg


def server_response_rating(stub):
    global currentRate, driverNameResponse
    responses = stub.GiveRating(send_rating())
    index = 0
    for response in responses:
        if index == 0:
            driverNameResponse = response.message
            index += 1
        elif index == 1:
            print("\nThank you for give our driver, %s, a rating %s / 5" % (driverNameResponse, response.message))
            currentRate = response.message
            index += 1
        elif index == 2:
            driverRating = (float(response.message) + float(currentRate)) / 2
            print("Final Driver Rate %i" % int(driverRating))
            index += 1
        else:
            print("")


if __name__ == '__main__':
    logging.basicConfig()
    run()
