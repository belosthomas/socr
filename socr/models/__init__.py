import torch

from .resSru import resSru
from .bigger_conv_lstm_network import BiggerConvLSTMNetwork
from .ocropy_line_network import OcropyLineNetwork
from .conv_lstm_network import ConvLSTMNetwork
from .x_height_labeling_model import XHeightLabelingModel
from .x_height_resnet_model import XHeightResnetModel
from .dhSegment import dhSegment


def get_model_by_name(name):
    return {
        "ConvLSTMNetwork": ConvLSTMNetwork,
        "BiggerConvLSTMNetwork": BiggerConvLSTMNetwork,
        "OcropyLineNetwork": OcropyLineNetwork,
        "XHeightLabelingModel": XHeightLabelingModel,
        "resSru": resSru,
        "XHeightResnetModel": XHeightResnetModel,
        "dhSegment": dhSegment
    }[name]


def get_optimizer_by_name(name):
    return {
        "SGD": torch.optim.SGD,
        "RMSProp": torch.optim.RMSprop,
        "Adam": torch.optim.Adam
    }[name]
