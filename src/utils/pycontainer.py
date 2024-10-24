from enum import Enum


class TargetEnum(Enum):
    """
    需要扫描的类型
    """
    CLASS = 0
    FUNCTION = 1
    METHOD = 2
    FUNCTION_AND_METHOD = 3


class Container:
    """
    基于全局扫描装饰器，并自动注册容器中的模型，这里是一个简单的实现，暂不考虑排除某些模块下的内容
    """

    def __init__(self):
        pass

    def register(self, path, target: TargetEnum, detected_attributes: dict):
        """
        选择某个模块路径，然后递归的进行扫描该路径,
        需要指定扫描的目标，
        然后还需要指定装饰器装饰过的具有特定属性的标识
        detected_attributes = {
             "all_of": ["attribute1", "attribute2"],
             "any_of": ["attribute3", "attribute4"]
        }
        """
        pass
