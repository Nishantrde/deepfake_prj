import numpy as np 
import os
import cv2 
import matplotlib.pyplot as plt
import insightface
from insightface.app import FaceAnalysis


def run_iit(inp_img, folder_name):
    # Initialize FaceAnalysis instance
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))

    # Load the image
    input_image = f"public\static\{inp_img}"
    img = cv2.imread(input_image)

    # Detect faces in the image
    faces = app.get(img)

    # Ensure that at least two faces are detected for swapping
    if len(faces) < 2:
        print("At least two faces are needed for swapping.")
    else:
        # Extract the face regions
        face1 = faces[0]
        face2 = faces[1]
        swapped_image = img.copy()
        # Perform face swapping
        swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)
        swapped_image = swapper.get(swapped_image, face1, face2, paste_back=True)
        swapped_image = swapper.get(swapped_image, face2, face1, paste_back=True)
        files = os.listdir(f'public\static\{folder_name}')
        for file in files:
            file_path = os.path.join(f'public\static\{folder_name}', file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        output_path = f'public\static\{folder_name}\op.png'
        cv2.imwrite(output_path, swapped_image)
