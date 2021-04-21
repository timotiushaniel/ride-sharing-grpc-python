# ride-sharing-grpc-python
Simple ride sharing application using gRPC in Python (Server and multiclient)

Requirements for simple ride sharing application using gRPC:
1. Find the closest drivers using server-side streaming model.
2. Select a driver
3. Reports the driver current position
4. Gives stars for a driver

The server may store the static data in a database. Use sample data for drivers, their position, and client position.

Client-server interaction using CLI:
1. Run client
2. Request to server to find the closest drivers, display all drivers along with their current position and their stars.
3. Select a driver based on the result from the server. Client request to select a driver and server marks the driver as being selected.
