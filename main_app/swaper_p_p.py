import numpy as np 
import glob
import os
import cv2 
import matplotlib.pyplot as plt
import insightface
from insightface.app import FaceAnalysis
# from insightface.data import get_image as ins_get_image


def run_it(inp_img, otp_img, folder_name):
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))

   
    input_face2 =  f"public\static\{inp_img}"
    input_face = f"public\static\{otp_img}"
    img = cv2.imread(input_face2)
    faces = app.get(img)
    fig, axs = plt.subplots(1,6, figsize=(12, 5))
    print(len(faces))
    print(axs)


    swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)
    

    per = cv2.imread(input_face)

    per_face = app.get(per)
    per_face = per_face[0]
    res = img.copy()
    for face in faces:
        res = swapper.get(res, face, per_face, paste_back=True)

    files = os.listdir(f'public\static\{folder_name}')
    for file in files:
        file_path = os.path.join(f'public\static\{folder_name}', file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    output_path = f'public\static\{folder_name}\op.png'  # Set your desired output path here

    

    # Save the modified image
    cv2.imwrite(output_path, res)
    # plt.show()


  
