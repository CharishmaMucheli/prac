import mediapipe as mp

print("Version:", mp.__version__)
print("Has solutions:", hasattr(mp, "solutions"))

mesh = mp.solutions.face_mesh.FaceMesh()
print("FaceMesh initialized")
