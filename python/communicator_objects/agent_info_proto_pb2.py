# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communicator_objects/agent_info_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='communicator_objects/agent_info_proto.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n+communicator_objects/agent_info_proto.proto\x12\x14\x63ommunicator_objects\"\x95\x02\n\x0e\x41gentInfoProto\x12\"\n\x1astacked_vector_observation\x18\x01 \x03(\x02\x12\x1b\n\x13visual_observations\x18\x02 \x03(\x0c\x12\x18\n\x10text_observation\x18\x03 \x01(\t\x12\x1d\n\x15stored_vector_actions\x18\x04 \x03(\x02\x12\x1b\n\x13stored_text_actions\x18\x05 \x01(\t\x12\x10\n\x08memories\x18\x06 \x03(\x02\x12\x0e\n\x06reward\x18\x07 \x01(\x02\x12\x0c\n\x04\x64one\x18\x08 \x01(\x08\x12\x18\n\x10max_step_reached\x18\t \x01(\x08\x12\n\n\x02id\x18\n \x01(\x05\x12\x16\n\x0emasked_actions\x18\x0b \x03(\x08\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
)




_AGENTINFOPROTO = _descriptor.Descriptor(
  name='AgentInfoProto',
  full_name='communicator_objects.AgentInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stacked_vector_observation', full_name='communicator_objects.AgentInfoProto.stacked_vector_observation', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visual_observations', full_name='communicator_objects.AgentInfoProto.visual_observations', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_observation', full_name='communicator_objects.AgentInfoProto.text_observation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stored_vector_actions', full_name='communicator_objects.AgentInfoProto.stored_vector_actions', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stored_text_actions', full_name='communicator_objects.AgentInfoProto.stored_text_actions', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memories', full_name='communicator_objects.AgentInfoProto.memories', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward', full_name='communicator_objects.AgentInfoProto.reward', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='communicator_objects.AgentInfoProto.done', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_step_reached', full_name='communicator_objects.AgentInfoProto.max_step_reached', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='communicator_objects.AgentInfoProto.id', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='masked_actions', full_name='communicator_objects.AgentInfoProto.masked_actions', index=10,
      number=11, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=347,
)

DESCRIPTOR.message_types_by_name['AgentInfoProto'] = _AGENTINFOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentInfoProto = _reflection.GeneratedProtocolMessageType('AgentInfoProto', (_message.Message,), dict(
  DESCRIPTOR = _AGENTINFOPROTO,
  __module__ = 'communicator_objects.agent_info_proto_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.AgentInfoProto)
  ))
_sym_db.RegisterMessage(AgentInfoProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\034MLAgents.CommunicatorObjects'))
# @@protoc_insertion_point(module_scope)
