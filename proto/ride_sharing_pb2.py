# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/ride_sharing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/ride_sharing.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\034io.grpc.examples.ridesharingB\020RideSharingProtoP\001\242\002\003RTG',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18proto/ride_sharing.proto\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"3\n\tRectangle\x12\x12\n\x02lo\x18\x01 \x01(\x0b\x32\x06.Point\x12\x12\n\x02hi\x18\x02 \x01(\x0b\x32\x06.Point\"\xbd\x01\n\x06\x44river\x12\x11\n\tdriver_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x64river_name\x18\x02 \x01(\t\x12\x0b\n\x03\x63\x61r\x18\x03 \x01(\t\x12\x15\n\rpolice_number\x18\x04 \x01(\t\x12\x0e\n\x06rating\x18\x05 \x01(\x02\x12\x14\n\x0c\x61vailability\x18\x06 \x01(\x08\x12\x18\n\x08location\x18\x07 \x01(\x0b\x32\x06.Point\x12\x15\n\rlocation_name\x18\x08 \x01(\t\x12\x10\n\x08\x64istance\x18\t \x01(\x02\"Z\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x18\n\x08location\x18\x03 \x01(\x0b\x32\x06.Point\x12\x15\n\rlocation_name\x18\x04 \x01(\t\"\x1f\n\x0c\x44riverChosen\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0bRatingGiven\x12\x0f\n\x07message\x18\x01 \x01(\t2\xbc\x01\n\tRideShare\x12\"\n\x0fGetUserLocation\x12\x06.Point\x1a\x05.User\"\x00\x12%\n\nListDriver\x12\n.Rectangle\x1a\x07.Driver\"\x00\x30\x01\x12\x32\n\x0c\x43hooseDriver\x12\r.DriverChosen\x1a\r.DriverChosen\"\x00(\x01\x30\x01\x12\x30\n\nGiveRating\x12\r.DriverChosen\x1a\r.DriverChosen\"\x00(\x01\x30\x01\x42\x38\n\x1cio.grpc.examples.ridesharingB\x10RideSharingProtoP\x01\xa2\x02\x03RTGb\x06proto3'
)




_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Point.latitude', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Point.longitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=72,
)


_RECTANGLE = _descriptor.Descriptor(
  name='Rectangle',
  full_name='Rectangle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lo', full_name='Rectangle.lo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hi', full_name='Rectangle.hi', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=125,
)


_DRIVER = _descriptor.Descriptor(
  name='Driver',
  full_name='Driver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver_id', full_name='Driver.driver_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='driver_name', full_name='Driver.driver_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='car', full_name='Driver.car', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='police_number', full_name='Driver.police_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rating', full_name='Driver.rating', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='availability', full_name='Driver.availability', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='Driver.location', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location_name', full_name='Driver.location_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='Driver.distance', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=317,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='User.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='User.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='User.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location_name', full_name='User.location_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=409,
)


_DRIVERCHOSEN = _descriptor.Descriptor(
  name='DriverChosen',
  full_name='DriverChosen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='DriverChosen.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=442,
)


_RATINGGIVEN = _descriptor.Descriptor(
  name='RatingGiven',
  full_name='RatingGiven',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='RatingGiven.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=474,
)

_RECTANGLE.fields_by_name['lo'].message_type = _POINT
_RECTANGLE.fields_by_name['hi'].message_type = _POINT
_DRIVER.fields_by_name['location'].message_type = _POINT
_USER.fields_by_name['location'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Rectangle'] = _RECTANGLE
DESCRIPTOR.message_types_by_name['Driver'] = _DRIVER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['DriverChosen'] = _DRIVERCHOSEN
DESCRIPTOR.message_types_by_name['RatingGiven'] = _RATINGGIVEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'proto.ride_sharing_pb2'
  # @@protoc_insertion_point(class_scope:Point)
  })
_sym_db.RegisterMessage(Point)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), {
  'DESCRIPTOR' : _RECTANGLE,
  '__module__' : 'proto.ride_sharing_pb2'
  # @@protoc_insertion_point(class_scope:Rectangle)
  })
_sym_db.RegisterMessage(Rectangle)

Driver = _reflection.GeneratedProtocolMessageType('Driver', (_message.Message,), {
  'DESCRIPTOR' : _DRIVER,
  '__module__' : 'proto.ride_sharing_pb2'
  # @@protoc_insertion_point(class_scope:Driver)
  })
_sym_db.RegisterMessage(Driver)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'proto.ride_sharing_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

DriverChosen = _reflection.GeneratedProtocolMessageType('DriverChosen', (_message.Message,), {
  'DESCRIPTOR' : _DRIVERCHOSEN,
  '__module__' : 'proto.ride_sharing_pb2'
  # @@protoc_insertion_point(class_scope:DriverChosen)
  })
_sym_db.RegisterMessage(DriverChosen)

RatingGiven = _reflection.GeneratedProtocolMessageType('RatingGiven', (_message.Message,), {
  'DESCRIPTOR' : _RATINGGIVEN,
  '__module__' : 'proto.ride_sharing_pb2'
  # @@protoc_insertion_point(class_scope:RatingGiven)
  })
_sym_db.RegisterMessage(RatingGiven)


DESCRIPTOR._options = None

_RIDESHARE = _descriptor.ServiceDescriptor(
  name='RideShare',
  full_name='RideShare',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=477,
  serialized_end=665,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserLocation',
    full_name='RideShare.GetUserLocation',
    index=0,
    containing_service=None,
    input_type=_POINT,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListDriver',
    full_name='RideShare.ListDriver',
    index=1,
    containing_service=None,
    input_type=_RECTANGLE,
    output_type=_DRIVER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChooseDriver',
    full_name='RideShare.ChooseDriver',
    index=2,
    containing_service=None,
    input_type=_DRIVERCHOSEN,
    output_type=_DRIVERCHOSEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GiveRating',
    full_name='RideShare.GiveRating',
    index=3,
    containing_service=None,
    input_type=_DRIVERCHOSEN,
    output_type=_DRIVERCHOSEN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RIDESHARE)

DESCRIPTOR.services_by_name['RideShare'] = _RIDESHARE

# @@protoc_insertion_point(module_scope)