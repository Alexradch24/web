from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProdCatRequest(_message.Message):
    __slots__ = ["c"]
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class ProdCatReply(_message.Message):
    __slots__ = ["cat"]
    CAT_FIELD_NUMBER: _ClassVar[int]
    cat: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cat: _Optional[_Iterable[str]] = ...) -> None: ...

class ProdRequest(_message.Message):
    __slots__ = ["category"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: str
    def __init__(self, category: _Optional[str] = ...) -> None: ...

class ProdReply(_message.Message):
    __slots__ = ["category", "prod_price"]
    class Price(_message.Message):
        __slots__ = ["pr"]
        PR_FIELD_NUMBER: _ClassVar[int]
        pr: float
        def __init__(self, pr: _Optional[float] = ...) -> None: ...
    class ProdPriceEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ProdReply.Price
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ProdReply.Price, _Mapping]] = ...) -> None: ...
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PROD_PRICE_FIELD_NUMBER: _ClassVar[int]
    category: str
    prod_price: _containers.MessageMap[str, ProdReply.Price]
    def __init__(self, category: _Optional[str] = ..., prod_price: _Optional[_Mapping[str, ProdReply.Price]] = ...) -> None: ...
