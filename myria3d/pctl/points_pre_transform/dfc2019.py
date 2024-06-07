# function to turn points loaded via pdal into a pyg Data object, with additional channels
import numpy as np
from torch_geometric.data import Data

RETURN_NUMBER_NORMALIZATION_MAX_VALUE = 4.0


def dfc2019_pre_transform(points):
    """Turn pdal points into torch-geometric Data object.

    Args:
        las_filepath (str): path to the LAS file.

    Returns:
        Data: the point cloud formatted for later deep learning training.

    """
    # Positions and base features
    pos = np.asarray([points["X"], points["Y"], points["Z"]], dtype=np.float32).transpose()

    # normalization
    points["ReturnNumber"] = (points["ReturnNumber"]) / (RETURN_NUMBER_NORMALIZATION_MAX_VALUE)
    
    # todo
    x = np.array([
            points[name]
            for name in [
                "Intensity",
                "ReturnNumber",
            ]
        ]).transpose()
    x_features_names = [
        "Intensity",
        "ReturnNumber",
    ]
    y = points["Classification"]

    data = Data(pos=pos, x=x, y=y, x_features_names=x_features_names)

    return data
