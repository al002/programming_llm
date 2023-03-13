from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
TERMINAL: PromptTemplate

class LLMReply(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class LLMRequest(_message.Message):
    __slots__ = ["query", "template"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    query: str
    template: PromptTemplate
    def __init__(self, query: _Optional[str] = ..., template: _Optional[_Union[PromptTemplate, str]] = ...) -> None: ...

class PromptTemplate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
