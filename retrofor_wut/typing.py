"""retrofor_wut 类型提示支持。

此模块定义了部分 retrofor_wut 使用的类型。
"""

from typing import TYPE_CHECKING, TypeVar, Callable, NoReturn, Awaitable

from retrofor_wut.message import T_MS, T_Message, T_MessageSegment

if TYPE_CHECKING:
    from retrofor_wut.bot import Bot  # noqa
    from retrofor_wut.event import Event  # noqa
    from retrofor_wut.plugin import Plugin  # noqa
    from retrofor_wut.adapter import Adapter  # noqa
    from retrofor_wut.config import ConfigModel  # noqa

__all__ = [
    "T_State",
    "T_Event",
    "T_Plugin",
    "T_Adapter",
    "T_Config",
    "T_Message",
    "T_MessageSegment",
    "T_MS",
    "T_BotHook",
    "T_AdapterHook",
    "T_EventHook",
]

T_State = TypeVar("T_State")
T_Event = TypeVar("T_Event", bound="Event")
T_Plugin = TypeVar("T_Plugin", bound="Plugin")
T_Adapter = TypeVar("T_Adapter", bound="Adapter")
T_Config = TypeVar("T_Config", bound="ConfigModel")

T_BotHook = Callable[["Bot"], Awaitable[NoReturn]]
T_AdapterHook = Callable[[T_Adapter], Awaitable[NoReturn]]
T_EventHook = Callable[[T_Event], Awaitable[NoReturn]]
