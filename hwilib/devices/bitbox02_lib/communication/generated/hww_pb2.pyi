"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from . import backup_commands_pb2
from . import bitbox02_system_pb2
from . import btc_pb2
import builtins
from . import cardano_pb2
from . import common_pb2
from . import eth_pb2
import google.protobuf.descriptor
import google.protobuf.message
from . import keystore_pb2
from . import mnemonic_pb2
from . import perform_attestation_pb2
from . import system_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Error(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: builtins.int
    message: typing.Text
    def __init__(self,
        *,
        code: builtins.int = ...,
        message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code",b"code","message",b"message"]) -> None: ...
global___Error = Error

class Success(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___Success = Success

class Request(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEVICE_NAME_FIELD_NUMBER: builtins.int
    DEVICE_LANGUAGE_FIELD_NUMBER: builtins.int
    DEVICE_INFO_FIELD_NUMBER: builtins.int
    SET_PASSWORD_FIELD_NUMBER: builtins.int
    CREATE_BACKUP_FIELD_NUMBER: builtins.int
    SHOW_MNEMONIC_FIELD_NUMBER: builtins.int
    BTC_PUB_FIELD_NUMBER: builtins.int
    BTC_SIGN_INIT_FIELD_NUMBER: builtins.int
    BTC_SIGN_INPUT_FIELD_NUMBER: builtins.int
    BTC_SIGN_OUTPUT_FIELD_NUMBER: builtins.int
    INSERT_REMOVE_SDCARD_FIELD_NUMBER: builtins.int
    CHECK_SDCARD_FIELD_NUMBER: builtins.int
    SET_MNEMONIC_PASSPHRASE_ENABLED_FIELD_NUMBER: builtins.int
    LIST_BACKUPS_FIELD_NUMBER: builtins.int
    RESTORE_BACKUP_FIELD_NUMBER: builtins.int
    PERFORM_ATTESTATION_FIELD_NUMBER: builtins.int
    REBOOT_FIELD_NUMBER: builtins.int
    CHECK_BACKUP_FIELD_NUMBER: builtins.int
    ETH_FIELD_NUMBER: builtins.int
    RESET_FIELD_NUMBER: builtins.int
    RESTORE_FROM_MNEMONIC_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    BTC_FIELD_NUMBER: builtins.int
    ELECTRUM_ENCRYPTION_KEY_FIELD_NUMBER: builtins.int
    CARDANO_FIELD_NUMBER: builtins.int
    @property
    def device_name(self) -> bitbox02_system_pb2.SetDeviceNameRequest:
        """removed: RandomNumberRequest random_number = 1;"""
        pass
    @property
    def device_language(self) -> bitbox02_system_pb2.SetDeviceLanguageRequest: ...
    @property
    def device_info(self) -> bitbox02_system_pb2.DeviceInfoRequest: ...
    @property
    def set_password(self) -> bitbox02_system_pb2.SetPasswordRequest: ...
    @property
    def create_backup(self) -> backup_commands_pb2.CreateBackupRequest: ...
    @property
    def show_mnemonic(self) -> mnemonic_pb2.ShowMnemonicRequest: ...
    @property
    def btc_pub(self) -> btc_pb2.BTCPubRequest: ...
    @property
    def btc_sign_init(self) -> btc_pb2.BTCSignInitRequest: ...
    @property
    def btc_sign_input(self) -> btc_pb2.BTCSignInputRequest: ...
    @property
    def btc_sign_output(self) -> btc_pb2.BTCSignOutputRequest: ...
    @property
    def insert_remove_sdcard(self) -> bitbox02_system_pb2.InsertRemoveSDCardRequest: ...
    @property
    def check_sdcard(self) -> bitbox02_system_pb2.CheckSDCardRequest: ...
    @property
    def set_mnemonic_passphrase_enabled(self) -> mnemonic_pb2.SetMnemonicPassphraseEnabledRequest: ...
    @property
    def list_backups(self) -> backup_commands_pb2.ListBackupsRequest: ...
    @property
    def restore_backup(self) -> backup_commands_pb2.RestoreBackupRequest: ...
    @property
    def perform_attestation(self) -> perform_attestation_pb2.PerformAttestationRequest: ...
    @property
    def reboot(self) -> system_pb2.RebootRequest: ...
    @property
    def check_backup(self) -> backup_commands_pb2.CheckBackupRequest: ...
    @property
    def eth(self) -> eth_pb2.ETHRequest: ...
    @property
    def reset(self) -> bitbox02_system_pb2.ResetRequest: ...
    @property
    def restore_from_mnemonic(self) -> mnemonic_pb2.RestoreFromMnemonicRequest: ...
    @property
    def fingerprint(self) -> common_pb2.RootFingerprintRequest:
        """removed: BitBoxBaseRequest bitboxbase = 23;"""
        pass
    @property
    def btc(self) -> btc_pb2.BTCRequest: ...
    @property
    def electrum_encryption_key(self) -> keystore_pb2.ElectrumEncryptionKeyRequest: ...
    @property
    def cardano(self) -> cardano_pb2.CardanoRequest: ...
    def __init__(self,
        *,
        device_name: typing.Optional[bitbox02_system_pb2.SetDeviceNameRequest] = ...,
        device_language: typing.Optional[bitbox02_system_pb2.SetDeviceLanguageRequest] = ...,
        device_info: typing.Optional[bitbox02_system_pb2.DeviceInfoRequest] = ...,
        set_password: typing.Optional[bitbox02_system_pb2.SetPasswordRequest] = ...,
        create_backup: typing.Optional[backup_commands_pb2.CreateBackupRequest] = ...,
        show_mnemonic: typing.Optional[mnemonic_pb2.ShowMnemonicRequest] = ...,
        btc_pub: typing.Optional[btc_pb2.BTCPubRequest] = ...,
        btc_sign_init: typing.Optional[btc_pb2.BTCSignInitRequest] = ...,
        btc_sign_input: typing.Optional[btc_pb2.BTCSignInputRequest] = ...,
        btc_sign_output: typing.Optional[btc_pb2.BTCSignOutputRequest] = ...,
        insert_remove_sdcard: typing.Optional[bitbox02_system_pb2.InsertRemoveSDCardRequest] = ...,
        check_sdcard: typing.Optional[bitbox02_system_pb2.CheckSDCardRequest] = ...,
        set_mnemonic_passphrase_enabled: typing.Optional[mnemonic_pb2.SetMnemonicPassphraseEnabledRequest] = ...,
        list_backups: typing.Optional[backup_commands_pb2.ListBackupsRequest] = ...,
        restore_backup: typing.Optional[backup_commands_pb2.RestoreBackupRequest] = ...,
        perform_attestation: typing.Optional[perform_attestation_pb2.PerformAttestationRequest] = ...,
        reboot: typing.Optional[system_pb2.RebootRequest] = ...,
        check_backup: typing.Optional[backup_commands_pb2.CheckBackupRequest] = ...,
        eth: typing.Optional[eth_pb2.ETHRequest] = ...,
        reset: typing.Optional[bitbox02_system_pb2.ResetRequest] = ...,
        restore_from_mnemonic: typing.Optional[mnemonic_pb2.RestoreFromMnemonicRequest] = ...,
        fingerprint: typing.Optional[common_pb2.RootFingerprintRequest] = ...,
        btc: typing.Optional[btc_pb2.BTCRequest] = ...,
        electrum_encryption_key: typing.Optional[keystore_pb2.ElectrumEncryptionKeyRequest] = ...,
        cardano: typing.Optional[cardano_pb2.CardanoRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["btc",b"btc","btc_pub",b"btc_pub","btc_sign_init",b"btc_sign_init","btc_sign_input",b"btc_sign_input","btc_sign_output",b"btc_sign_output","cardano",b"cardano","check_backup",b"check_backup","check_sdcard",b"check_sdcard","create_backup",b"create_backup","device_info",b"device_info","device_language",b"device_language","device_name",b"device_name","electrum_encryption_key",b"electrum_encryption_key","eth",b"eth","fingerprint",b"fingerprint","insert_remove_sdcard",b"insert_remove_sdcard","list_backups",b"list_backups","perform_attestation",b"perform_attestation","reboot",b"reboot","request",b"request","reset",b"reset","restore_backup",b"restore_backup","restore_from_mnemonic",b"restore_from_mnemonic","set_mnemonic_passphrase_enabled",b"set_mnemonic_passphrase_enabled","set_password",b"set_password","show_mnemonic",b"show_mnemonic"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["btc",b"btc","btc_pub",b"btc_pub","btc_sign_init",b"btc_sign_init","btc_sign_input",b"btc_sign_input","btc_sign_output",b"btc_sign_output","cardano",b"cardano","check_backup",b"check_backup","check_sdcard",b"check_sdcard","create_backup",b"create_backup","device_info",b"device_info","device_language",b"device_language","device_name",b"device_name","electrum_encryption_key",b"electrum_encryption_key","eth",b"eth","fingerprint",b"fingerprint","insert_remove_sdcard",b"insert_remove_sdcard","list_backups",b"list_backups","perform_attestation",b"perform_attestation","reboot",b"reboot","request",b"request","reset",b"reset","restore_backup",b"restore_backup","restore_from_mnemonic",b"restore_from_mnemonic","set_mnemonic_passphrase_enabled",b"set_mnemonic_passphrase_enabled","set_password",b"set_password","show_mnemonic",b"show_mnemonic"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["request",b"request"]) -> typing.Optional[typing_extensions.Literal["device_name","device_language","device_info","set_password","create_backup","show_mnemonic","btc_pub","btc_sign_init","btc_sign_input","btc_sign_output","insert_remove_sdcard","check_sdcard","set_mnemonic_passphrase_enabled","list_backups","restore_backup","perform_attestation","reboot","check_backup","eth","reset","restore_from_mnemonic","fingerprint","btc","electrum_encryption_key","cardano"]]: ...
global___Request = Request

class Response(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    DEVICE_INFO_FIELD_NUMBER: builtins.int
    PUB_FIELD_NUMBER: builtins.int
    BTC_SIGN_NEXT_FIELD_NUMBER: builtins.int
    LIST_BACKUPS_FIELD_NUMBER: builtins.int
    CHECK_BACKUP_FIELD_NUMBER: builtins.int
    PERFORM_ATTESTATION_FIELD_NUMBER: builtins.int
    CHECK_SDCARD_FIELD_NUMBER: builtins.int
    ETH_FIELD_NUMBER: builtins.int
    FINGERPRINT_FIELD_NUMBER: builtins.int
    BTC_FIELD_NUMBER: builtins.int
    ELECTRUM_ENCRYPTION_KEY_FIELD_NUMBER: builtins.int
    CARDANO_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> global___Success: ...
    @property
    def error(self) -> global___Error: ...
    @property
    def device_info(self) -> bitbox02_system_pb2.DeviceInfoResponse:
        """removed: RandomNumberResponse random_number = 3;"""
        pass
    @property
    def pub(self) -> common_pb2.PubResponse: ...
    @property
    def btc_sign_next(self) -> btc_pb2.BTCSignNextResponse: ...
    @property
    def list_backups(self) -> backup_commands_pb2.ListBackupsResponse: ...
    @property
    def check_backup(self) -> backup_commands_pb2.CheckBackupResponse: ...
    @property
    def perform_attestation(self) -> perform_attestation_pb2.PerformAttestationResponse: ...
    @property
    def check_sdcard(self) -> bitbox02_system_pb2.CheckSDCardResponse: ...
    @property
    def eth(self) -> eth_pb2.ETHResponse: ...
    @property
    def fingerprint(self) -> common_pb2.RootFingerprintResponse: ...
    @property
    def btc(self) -> btc_pb2.BTCResponse: ...
    @property
    def electrum_encryption_key(self) -> keystore_pb2.ElectrumEncryptionKeyResponse: ...
    @property
    def cardano(self) -> cardano_pb2.CardanoResponse: ...
    def __init__(self,
        *,
        success: typing.Optional[global___Success] = ...,
        error: typing.Optional[global___Error] = ...,
        device_info: typing.Optional[bitbox02_system_pb2.DeviceInfoResponse] = ...,
        pub: typing.Optional[common_pb2.PubResponse] = ...,
        btc_sign_next: typing.Optional[btc_pb2.BTCSignNextResponse] = ...,
        list_backups: typing.Optional[backup_commands_pb2.ListBackupsResponse] = ...,
        check_backup: typing.Optional[backup_commands_pb2.CheckBackupResponse] = ...,
        perform_attestation: typing.Optional[perform_attestation_pb2.PerformAttestationResponse] = ...,
        check_sdcard: typing.Optional[bitbox02_system_pb2.CheckSDCardResponse] = ...,
        eth: typing.Optional[eth_pb2.ETHResponse] = ...,
        fingerprint: typing.Optional[common_pb2.RootFingerprintResponse] = ...,
        btc: typing.Optional[btc_pb2.BTCResponse] = ...,
        electrum_encryption_key: typing.Optional[keystore_pb2.ElectrumEncryptionKeyResponse] = ...,
        cardano: typing.Optional[cardano_pb2.CardanoResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["btc",b"btc","btc_sign_next",b"btc_sign_next","cardano",b"cardano","check_backup",b"check_backup","check_sdcard",b"check_sdcard","device_info",b"device_info","electrum_encryption_key",b"electrum_encryption_key","error",b"error","eth",b"eth","fingerprint",b"fingerprint","list_backups",b"list_backups","perform_attestation",b"perform_attestation","pub",b"pub","response",b"response","success",b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["btc",b"btc","btc_sign_next",b"btc_sign_next","cardano",b"cardano","check_backup",b"check_backup","check_sdcard",b"check_sdcard","device_info",b"device_info","electrum_encryption_key",b"electrum_encryption_key","error",b"error","eth",b"eth","fingerprint",b"fingerprint","list_backups",b"list_backups","perform_attestation",b"perform_attestation","pub",b"pub","response",b"response","success",b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["success","error","device_info","pub","btc_sign_next","list_backups","check_backup","perform_attestation","check_sdcard","eth","fingerprint","btc","electrum_encryption_key","cardano"]]: ...
global___Response = Response
