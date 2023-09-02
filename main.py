__author__ = "X. Zhang, Westwood Robotics Corporation"
__email__ = "info@westwoodrobotics.io"
__copyright__ = "Copyright 2023 Westwood Robotics"
__date__ = "Sep. 01, 2023"

__version__ = "0.0.1"
__status__ = "beta"

from csv2urdf import CSV2URDF

robot_name = "BRUCE_V1.4_simplified"
csv_path = "files/"+robot_name+".csv"
urdf_path = "files/"+robot_name+".urdf"

CSV2URDF(robot_name, csv_path, urdf_path)