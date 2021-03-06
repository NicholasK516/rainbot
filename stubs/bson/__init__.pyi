# Stubs for bson (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import datetime
from typing import Any, BinaryIO, Iterator, List, Mapping, MutableMapping, Sequence

from bson.binary import Binary as Binary
from bson.code import Code as Code
from bson.codec_options import CodecOptions as CodecOptions
from bson.dbref import DBRef as DBRef
from bson.decimal128 import Decimal128 as Decimal128
from bson.errors import (InvalidBSON as InvalidBSON,
                         InvalidDocument as InvalidDocument,
                         InvalidStringData as InvalidStringData)
from bson.int64 import Int64 as Int64
from bson.max_key import MaxKey as MaxKey
from bson.min_key import MinKey as MinKey
from bson.objectid import ObjectId as ObjectId
from bson.regex import Regex as Regex
from bson.son import SON as SON
from bson.timestamp import Timestamp as Timestamp
from bson.tz_util import utc as utc

EPOCH_AWARE: datetime.datetime
EPOCH_NAIVE: datetime.datetime
BSONNUM: bytes
BSONSTR: bytes
BSONOBJ: bytes
BSONARR: bytes
BSONBIN: bytes
BSONUND: bytes
BSONOID: bytes
BSONBOO: bytes
BSONDAT: bytes
BSONNUL: bytes
BSONRGX: bytes
BSONREF: bytes
BSONCOD: bytes
BSONSYM: bytes
BSONCWS: bytes
BSONINT: bytes
BSONTIM: bytes
BSONLON: bytes
BSONDEC: bytes
BSONMIN: bytes
BSONMAX: bytes


def gen_list_name() -> Iterator[bytes]: ...


def decode_all(data: Sequence[bytes], codec_options: CodecOptions = ...) -> List[Mapping[Any, Any]]: ...


def decode_iter(data: Sequence[bytes], codec_options: CodecOptions = ...) -> Iterator[MutableMapping[Any, Any]]: ...


def decode_file_iter(file_obj: BinaryIO, codec_options: CodecOptions = ...) -> Iterator[MutableMapping[Any, Any]]: ...


def is_valid(bson: bytes) -> bool: ...


class BSON(bytes):
    @classmethod
    def encode(cls, document: Mapping[Any, Any], check_keys: bool = ..., codec_options: CodecOptions = ...) -> BSON: ...

    def decode(self, codec_options: CodecOptions = ...) -> MutableMapping[Any, Any]: ...  # type: ignore


def has_c() -> bool: ...
