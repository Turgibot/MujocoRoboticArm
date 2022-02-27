# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UnityStreamer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='UnityStreamer.proto',
  package='unitystreamer',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13UnityStreamer.proto\x12\runitystreamer\"u\n\tUnityData\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x12\n\nimage_data\x18\x03 \x01(\x0c\x12\x12\n\ndepth_data\x18\x04 \x01(\x0c\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x12\x0e\n\x06params\x18\x06 \x03(\x05\"\x1d\n\x08Received\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x32T\n\rUnityStreamer\x12\x43\n\nStreamData\x12\x18.unitystreamer.UnityData\x1a\x17.unitystreamer.Received\"\x00(\x01\x62\x06proto3'
)




_UNITYDATA = _descriptor.Descriptor(
  name='UnityData',
  full_name='unitystreamer.UnityData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='unitystreamer.UnityData.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='unitystreamer.UnityData.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_data', full_name='unitystreamer.UnityData.image_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth_data', full_name='unitystreamer.UnityData.depth_data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='unitystreamer.UnityData.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='unitystreamer.UnityData.params', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=38,
  serialized_end=155,
)


_RECEIVED = _descriptor.Descriptor(
  name='Received',
  full_name='unitystreamer.Received',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='unitystreamer.Received.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=157,
  serialized_end=186,
)

DESCRIPTOR.message_types_by_name['UnityData'] = _UNITYDATA
DESCRIPTOR.message_types_by_name['Received'] = _RECEIVED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityData = _reflection.GeneratedProtocolMessageType('UnityData', (_message.Message,), {
  'DESCRIPTOR' : _UNITYDATA,
  '__module__' : 'UnityStreamer_pb2'
  # @@protoc_insertion_point(class_scope:unitystreamer.UnityData)
  })
_sym_db.RegisterMessage(UnityData)

Received = _reflection.GeneratedProtocolMessageType('Received', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVED,
  '__module__' : 'UnityStreamer_pb2'
  # @@protoc_insertion_point(class_scope:unitystreamer.Received)
  })
_sym_db.RegisterMessage(Received)



_UNITYSTREAMER = _descriptor.ServiceDescriptor(
  name='UnityStreamer',
  full_name='unitystreamer.UnityStreamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=188,
  serialized_end=272,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamData',
    full_name='unitystreamer.UnityStreamer.StreamData',
    index=0,
    containing_service=None,
    input_type=_UNITYDATA,
    output_type=_RECEIVED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UNITYSTREAMER)

DESCRIPTOR.services_by_name['UnityStreamer'] = _UNITYSTREAMER

# @@protoc_insertion_point(module_scope)