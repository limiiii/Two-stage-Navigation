
import numpy as np
from scipy.spatial.transform import Rotation
def quaternion_to_euler(quat):
    r = Rotation.from_quat(quat)
    euler = r.as_euler('xyz', degrees=True)  # 按顺序返回欧拉角，单位为度数
    return euler

# 示例四元组
quat = [0.0, 0.0, 0.32740, 0.94489]
# 转换为欧拉角
euler_angles = quaternion_to_euler(quat)
print("euler_angles", euler_angles)

theta = (2 * np.arccos(0.94489)) * 180 / 3.1415926
print("theta:", theta)

