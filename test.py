import cv2
import pickle
import numpy as np
import os
import tempfile
import shutil

# Helper function: safe load pickle
def safe_load_pickle(filepath):
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, 'rb') as f:
            try:
                return pickle.load(f)
            except Exception:
                print(f"⚠ Corrupted file removed: {filepath}")
                os.remove(filepath)
    return None

# Helper function: safe save pickle
def safe_save_pickle(data, filepath):
    temp_fd, temp_path = tempfile.mkstemp()
    os.close(temp_fd)
    with open(temp_path, 'wb') as f:
        pickle.dump(data, f)
    shutil.move(temp_path, filepath)  # Replace atomically

# Setup
video = cv2.VideoCapture(0)
facesdetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_data = []
name = input("Enter your name: ")
i = 0

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facesdetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resize_img = cv2.resize(crop_img, (50, 50))

        # Take 10 samples, one every 10 frames
        if len(faces_data) < 10 and i % 10 == 0:
            faces_data.append(resize_img)

        cv2.putText(frame, str(len(faces_data)), (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)

    i += 1

    cv2.imshow("Camera Feed", frame)

    # Exit when 'q' pressed or 10 samples collected
    if cv2.waitKey(1) == ord('q') or len(faces_data) == 10:
        break

video.release()
cv2.destroyAllWindows()

# Save data
faces_data = np.asarray(faces_data).reshape(10, -1)

# Ensure folder exists
data_dir = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Save names
names_file = os.path.join(data_dir, 'names.pkl')
names = safe_load_pickle(names_file)
if names is None:
    names = []
names = names + [name] * 10
safe_save_pickle(names, names_file)

# Save faces
faces_file = os.path.join(data_dir, 'faces_data.pkl')
faces = safe_load_pickle(faces_file)
if faces is None:
    faces = np.empty((0, faces_data.shape[1]))
faces = np.append(faces, faces_data, axis=0)
safe_save_pickle(faces, faces_file)

print("✅ Data saved successfully!")
