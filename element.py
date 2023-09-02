__author__ = "X. Zhang, Westwood Robotics Corporation"
__email__ = "info@westwoodrobotics.io"
__copyright__ = "Copyright 2023 Westwood Robotics"
__date__ = "Sep. 01, 2023"

__version__ = "0.0.1"
__status__ = "beta"

class Element(object):
    """
    """

    def __init__(self, data):
        """
        """
        self.data = data

    def to_urdf(self):

        # Add link first
        urdf = ""
        urdf += "  <link\n"
        urdf += "    name=\"" + self.data["LINK NAME"]+"\">\n"
        urdf += "    <inertial>\n"
        urdf += "      <origin\n"
        urdf += "        xyz=\""+self.data["CENTER OF MASS X"]+" "+self.data["CENTER OF MASS Y"]+" "+self.data["CENTER OF MASS Z"]+"\"\n"
        urdf += "        rpy=\"0 0 0\" />\n"
        urdf += "      <mass\n"
        urdf += "        value=\""+self.data["MASS"]+"\" />\n"
        urdf += "      <inertia\n"
        urdf += "        ixx=\""+self.data["MOMENT IXX"]+"\"\n"
        urdf += "        ixy=\""+self.data["MOMENT IXY"]+"\"\n"
        urdf += "        ixz=\""+self.data["MOMENT IXZ"]+"\"\n"
        urdf += "        iyy=\""+self.data["MOMENT IYY"]+"\"\n"
        urdf += "        iyz=\""+self.data["MOMENT IYZ"]+"\"\n"
        urdf += "        izz=\""+self.data["MOMENT IZZ"]+"\" />\n"
        urdf += "    </inertial>\n"
        urdf += "    <visual>\n"
        urdf += "      <origin\n"
        urdf += "        xyz=\"0 0 0\"\n"
        urdf += "        rpy=\"0 0 0\" />\n"
        urdf += "      <geometry>\n"
        urdf += "        <mesh\n"
        urdf += "          filename=\""+self.data["MESH FILENAME"]+"\" />\n"
        urdf += "      </geometry>\n"
        urdf += "      <material\n"
        urdf += "        name=\"\">\n"
        urdf += "        <color\n"
        urdf += "          rgba=\""+self.data["COLOR RED"]+" "+self.data["COLOR GREEN"]+" "+self.data["COLOR BLUE"]+" "+self.data["COLOR ALPHA"]+"\" />\n"
        urdf += "      </material>\n"
        urdf += "    </visual>\n"
        urdf += "    <collision>\n"
        urdf += "      <origin\n"
        urdf += "        xyz=\""+self.data["COLLISION X"]+" "+self.data["COLLISION Y"]+" "+self.data["COLLISION Z"]+"\"\n"
        urdf += "        rpy=\""+self.data["COLLISION ROLL"]+" "+self.data["COLLISION PITCH"]+" "+self.data["COLLISION YAW"]+"\" />\n"
        urdf += "      <geometry>\n"
        urdf += "        <mesh\n"
        urdf += "          filename=\""+self.data["COLLISION MESH FILENAME"]+"\" />\n"
        urdf += "      </geometry>\n"
        urdf += "    </collision>\n"
        urdf += "  </link>\n"

        # Check if there is a joint, add a joint if necessary.
        if self.data["AXIS NAME"] != '':
            urdf += "  <joint\n"
            urdf += "    name=\""+self.data["JOINT NAME"]+"\"\n"
            urdf += "    type=\""+self.data["JOINT TYPE"]+"\">\n"
            urdf += "    <origin\n"
            urdf += "      xyz=\""+self.data["JOINT ORIGIN X"]+" "+self.data["JOINT ORIGIN Y"]+" "+self.data["JOINT ORIGIN Z"]+"\"\n"
            urdf += "      rpy=\""+self.data["JOINT ORIGIN ROLL"]+" "+self.data["JOINT ORIGIN PITCH"]+" "+self.data["JOINT ORIGIN YAW"]+"\" />\n"
            urdf += "    <parent\n"
            urdf += "      link=\""+self.data["PARENT"]+"\" />\n"
            urdf += "    <child\n"
            urdf += "      link=\""+self.data["LINK NAME"]+"\" />\n"
            urdf += "    <axis\n"
            urdf += "      xyz=\""+self.data["JOINT AXIS X"]+" "+self.data["JOINT AXIS Y"]+" "+self.data["JOINT AXIS Z"]+"\" />\n"
            urdf += "    <limit\n"
            urdf += "      lower=\""+self.data["LIMIT LOWER"]+"\"\n"
            urdf += "      upper=\""+self.data["LIMIT UPPER"]+"\"\n"
            urdf += "      effort=\""+self.data["LIMIT EFFORT"]+"\"\n"
            urdf += "      velocity=\""+self.data["LIMIT VELOCITY"]+"\" />\n"
            urdf += "  </joint>\n"

        return urdf
