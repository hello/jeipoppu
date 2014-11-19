# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio_classifcation.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='audio_classifcation.proto',
  package='',
  serialized_pb='\n\x19\x61udio_classifcation.proto\"\xe7\x01\n\x12\x61udio_class_result\x12\x13\n\x0bprobability\x18\x01 \x03(\x02\x12\x30\n\x07\x63lasses\x18\x02 \x03(\x0e\x32\x1f.audio_class_result.audio_class\x12\x31\n\x08\x64\x65\x63ision\x18\x03 \x01(\x0e\x32\x1f.audio_class_result.audio_class\"W\n\x0b\x61udio_class\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04NULL\x10\x01\x12\x0b\n\x07TALKING\x10\x02\x12\n\n\x06\x43RYING\x10\x03\x12\x0b\n\x07SNORING\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05\"T\n\x13\x61udio_energy_result\x12#\n\x1bmax_decibel_over_background\x18\x01 \x01(\x02\x12\x18\n\x10num_disturbances\x18\x02 \x01(\x05\"\xa8\x01\n\x1b\x61udio_classifcation_message\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x11\n\tunix_time\x18\x02 \x01(\x05\x12\x15\n\rclassifer_key\x18\x03 \x01(\t\x12&\n\x08\x65nergies\x18\x04 \x01(\x0b\x32\x14.audio_energy_result\x12$\n\x07\x63lasses\x18\x05 \x01(\x0b\x32\x13.audio_class_resultB7\n\x1a\x63om.hello.suripu.api.audioB\x19\x41udioClassificationProtos')



_AUDIO_CLASS_RESULT_AUDIO_CLASS = _descriptor.EnumDescriptor(
  name='audio_class',
  full_name='audio_class_result.audio_class',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NULL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TALKING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRYING', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNORING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VEHICLE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=174,
  serialized_end=261,
)


_AUDIO_CLASS_RESULT = _descriptor.Descriptor(
  name='audio_class_result',
  full_name='audio_class_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='probability', full_name='audio_class_result.probability', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classes', full_name='audio_class_result.classes', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decision', full_name='audio_class_result.decision', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUDIO_CLASS_RESULT_AUDIO_CLASS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=261,
)


_AUDIO_ENERGY_RESULT = _descriptor.Descriptor(
  name='audio_energy_result',
  full_name='audio_energy_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_decibel_over_background', full_name='audio_energy_result.max_decibel_over_background', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_disturbances', full_name='audio_energy_result.num_disturbances', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=263,
  serialized_end=347,
)


_AUDIO_CLASSIFCATION_MESSAGE = _descriptor.Descriptor(
  name='audio_classifcation_message',
  full_name='audio_classifcation_message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='audio_classifcation_message.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unix_time', full_name='audio_classifcation_message.unix_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classifer_key', full_name='audio_classifcation_message.classifer_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energies', full_name='audio_classifcation_message.energies', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='classes', full_name='audio_classifcation_message.classes', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=350,
  serialized_end=518,
)

_AUDIO_CLASS_RESULT.fields_by_name['classes'].enum_type = _AUDIO_CLASS_RESULT_AUDIO_CLASS
_AUDIO_CLASS_RESULT.fields_by_name['decision'].enum_type = _AUDIO_CLASS_RESULT_AUDIO_CLASS
_AUDIO_CLASS_RESULT_AUDIO_CLASS.containing_type = _AUDIO_CLASS_RESULT;
_AUDIO_CLASSIFCATION_MESSAGE.fields_by_name['energies'].message_type = _AUDIO_ENERGY_RESULT
_AUDIO_CLASSIFCATION_MESSAGE.fields_by_name['classes'].message_type = _AUDIO_CLASS_RESULT
DESCRIPTOR.message_types_by_name['audio_class_result'] = _AUDIO_CLASS_RESULT
DESCRIPTOR.message_types_by_name['audio_energy_result'] = _AUDIO_ENERGY_RESULT
DESCRIPTOR.message_types_by_name['audio_classifcation_message'] = _AUDIO_CLASSIFCATION_MESSAGE

class audio_class_result(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUDIO_CLASS_RESULT

  # @@protoc_insertion_point(class_scope:audio_class_result)

class audio_energy_result(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUDIO_ENERGY_RESULT

  # @@protoc_insertion_point(class_scope:audio_energy_result)

class audio_classifcation_message(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUDIO_CLASSIFCATION_MESSAGE

  # @@protoc_insertion_point(class_scope:audio_classifcation_message)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\032com.hello.suripu.api.audioB\031AudioClassificationProtos')
# @@protoc_insertion_point(module_scope)
