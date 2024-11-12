"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ShowMnemonicRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ShowMnemonicRequest = ShowMnemonicRequest

class RestoreFromMnemonicRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIMESTAMP_FIELD_NUMBER: builtins.int
    TIMEZONE_OFFSET_FIELD_NUMBER: builtins.int
    timestamp: builtins.int
    timezone_offset: builtins.int
    def __init__(self,
        *,
        timestamp: builtins.int = ...,
        timezone_offset: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp","timezone_offset",b"timezone_offset"]) -> None: ...
global___RestoreFromMnemonicRequest = RestoreFromMnemonicRequest

class SetMnemonicPassphraseEnabledRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENABLED_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    def __init__(self,
        *,
        enabled: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enabled",b"enabled"]) -> None: ...
global___SetMnemonicPassphraseEnabledRequest = SetMnemonicPassphraseEnabledRequest
