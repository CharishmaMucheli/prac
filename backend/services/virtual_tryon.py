import cv2
import numpy as np

def try_on(user_img, cloth_img):
    user = cv2.imdecode(
        np.frombuffer(user_img.file.read(), np.uint8),
        cv2.IMREAD_COLOR
    )

    cloth = cv2.imdecode(
        np.frombuffer(cloth_img.file.read(), np.uint8),
        cv2.IMREAD_UNCHANGED
    )

    cloth = cv2.resize(cloth, (200, 300))
    user[100:400, 100:300] = cloth[:, :, :3]

    cv2.imwrite("output.jpg", user)

    return {"status": "Virtual try-on completed", "output": "output.jpg"}
