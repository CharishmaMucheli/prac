import cv2
import numpy as np
import mediapipe as mp
from services.skin_tone import detect_skin_tone
from services.body_type import detect_body_type

mp_face = mp.solutions.face_mesh.FaceMesh(static_image_mode=True)

def analyze_face(file):
    image = np.frombuffer(file.file.read(), np.uint8)
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = mp_face.process(rgb)

    face_shape = "Oval"  # placeholder logic
    skin_tone = detect_skin_tone(img)
    body_type = detect_body_type(img)

    return {
        "face_shape": face_shape,
        "skin_tone": skin_tone,
        "body_type": body_type
    }
