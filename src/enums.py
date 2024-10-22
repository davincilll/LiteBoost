# 补充一些对部分配置的枚举
from enum import Enum


class SchedulerConcurrentModeEnum(Enum):
    THREAD = 'thread'
    ASYNCIO = 'asyncio'
    SINGLE = 'single'
    GEVENT = 'gevent'
    GEVENT_EVENTLET = 'gevent_eventlet'


class FuncTypeEnum(Enum):
    COMMON_FUNCTION = 'COMMON_FUNCTION'
    INSTANCE_METHOD = 'INSTANCE_METHOD'
    CLASS_METHOD = 'CLASS_METHOD'
    # STATIC_METHOD = 'STATIC_METHOD' # 静态方法与COMMON方法是等同的