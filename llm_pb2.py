# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: llm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tllm.proto\x12\x03llm\"T\n\nLLMRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x08template\x18\x02 \x01(\x0e\x32\x13.llm.PromptTemplateH\x00\x88\x01\x01\x42\x0b\n\t_template\"\x1c\n\x08LLMReply\x12\x10\n\x08response\x18\x01 \x01(\t*\x1e\n\x0ePromptTemplate\x12\x0c\n\x08TERMINAL\x10\x00\x32\x30\n\x03LLM\x12)\n\x05query\x12\x0f.llm.LLMRequest\x1a\r.llm.LLMReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'llm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROMPTTEMPLATE._serialized_start=134
  _PROMPTTEMPLATE._serialized_end=164
  _LLMREQUEST._serialized_start=18
  _LLMREQUEST._serialized_end=102
  _LLMREPLY._serialized_start=104
  _LLMREPLY._serialized_end=132
  _LLM._serialized_start=166
  _LLM._serialized_end=214
# @@protoc_insertion_point(module_scope)
