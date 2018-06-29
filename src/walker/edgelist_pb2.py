# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edgelist.proto

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
  name='edgelist.proto',
  package='func2vec',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x65\x64gelist.proto\x12\x08\x66unc2vec\"\xa8\x02\n\x08\x45\x64gelist\x12%\n\x04\x65\x64ge\x18\x01 \x03(\x0b\x32\x17.func2vec.Edgelist.Edge\x12\x36\n\x0bid_to_label\x18\x02 \x03(\x0b\x32!.func2vec.Edgelist.IdToLabelEntry\x1aY\n\x04\x45\x64ge\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\r\n\x05label\x18\x03 \x01(\t\x12\x10\n\x08label_id\x18\x05 \x03(\x05\x12\x10\n\x08location\x18\x04 \x01(\t\x1a\x16\n\x05Label\x12\r\n\x05label\x18\x01 \x01(\t\x1aJ\n\x0eIdToLabelEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.func2vec.Edgelist.Label:\x02\x38\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EDGELIST_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='func2vec.Edgelist.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='func2vec.Edgelist.Edge.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='func2vec.Edgelist.Edge.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='func2vec.Edgelist.Edge.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_id', full_name='func2vec.Edgelist.Edge.label_id', index=3,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='func2vec.Edgelist.Edge.location', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=136,
  serialized_end=225,
)

_EDGELIST_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='func2vec.Edgelist.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='func2vec.Edgelist.Label.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=227,
  serialized_end=249,
)

_EDGELIST_IDTOLABELENTRY = _descriptor.Descriptor(
  name='IdToLabelEntry',
  full_name='func2vec.Edgelist.IdToLabelEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='func2vec.Edgelist.IdToLabelEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='func2vec.Edgelist.IdToLabelEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=325,
)

_EDGELIST = _descriptor.Descriptor(
  name='Edgelist',
  full_name='func2vec.Edgelist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge', full_name='func2vec.Edgelist.edge', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id_to_label', full_name='func2vec.Edgelist.id_to_label', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EDGELIST_EDGE, _EDGELIST_LABEL, _EDGELIST_IDTOLABELENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=325,
)

_EDGELIST_EDGE.containing_type = _EDGELIST
_EDGELIST_LABEL.containing_type = _EDGELIST
_EDGELIST_IDTOLABELENTRY.fields_by_name['value'].message_type = _EDGELIST_LABEL
_EDGELIST_IDTOLABELENTRY.containing_type = _EDGELIST
_EDGELIST.fields_by_name['edge'].message_type = _EDGELIST_EDGE
_EDGELIST.fields_by_name['id_to_label'].message_type = _EDGELIST_IDTOLABELENTRY
DESCRIPTOR.message_types_by_name['Edgelist'] = _EDGELIST

Edgelist = _reflection.GeneratedProtocolMessageType('Edgelist', (_message.Message,), dict(

  Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
    DESCRIPTOR = _EDGELIST_EDGE,
    __module__ = 'edgelist_pb2'
    # @@protoc_insertion_point(class_scope:func2vec.Edgelist.Edge)
    ))
  ,

  Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(
    DESCRIPTOR = _EDGELIST_LABEL,
    __module__ = 'edgelist_pb2'
    # @@protoc_insertion_point(class_scope:func2vec.Edgelist.Label)
    ))
  ,

  IdToLabelEntry = _reflection.GeneratedProtocolMessageType('IdToLabelEntry', (_message.Message,), dict(
    DESCRIPTOR = _EDGELIST_IDTOLABELENTRY,
    __module__ = 'edgelist_pb2'
    # @@protoc_insertion_point(class_scope:func2vec.Edgelist.IdToLabelEntry)
    ))
  ,
  DESCRIPTOR = _EDGELIST,
  __module__ = 'edgelist_pb2'
  # @@protoc_insertion_point(class_scope:func2vec.Edgelist)
  ))
_sym_db.RegisterMessage(Edgelist)
_sym_db.RegisterMessage(Edgelist.Edge)
_sym_db.RegisterMessage(Edgelist.Label)
_sym_db.RegisterMessage(Edgelist.IdToLabelEntry)


_EDGELIST_IDTOLABELENTRY.has_options = True
_EDGELIST_IDTOLABELENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
