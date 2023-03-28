import numpy as np
import pytesseract
import pandas as pd
import cv2
from pdf2image import convert_from_path
import os
from PIL import Image
from pytesseract import image_to_string
from module import extract_boxes, extract_checkboxes

images = convert_from_path('C:/Users/Taraneh/Desktop/pythonProject/ocr/pages/typeA1.pdf',
                           poppler_path='C:/poppler-0.68.0/bin')
path = "pages"

for i in range(len(images)):
    name = f'page' + str(i) + '.jpg'
    filename = os.path.join(path, name)  # Save pages as images in the pdf
    images[i].save(filename)




a = []
b = []
A = []
B = []

for root, dirs, files in os.walk(path):
    for filename in files:
        final = {}
        text_list = []
        pg_nmb = filename.split(".")

        if pg_nmb[1] == 'jpg':
            pg_nmb = pg_nmb[0]

            file_path = os.path.join(root, filename)
            checkboxes = extract_checkboxes(file_path)
            boxes = extract_boxes(file_path)
            results = pytesseract.image_to_data(file_path, output_type=pytesseract.Output.DICT,
                                                config='--psm 12 --oem 3 ')
            results_df = pd.DataFrame(results)
            for k, checkbox in enumerate(checkboxes):
                if checkbox[1] == 1:

                    text_list = []
                    b = []
                    # final = {}
                    for j in range(0, len(results_df)):
                        x, y, w, h = results_df["left"][j], results_df["top"][j], results_df["width"][j], \
                            results_df["height"][j]

                        if (k + 1) != len(checkboxes):
                            next_box = checkboxes[k + 1]
                            if checkbox[0][1] - 10 <= next_box[0][1] <= checkbox[0][1] + 10:
                                if (checkbox[0][1] <= y <= checkbox[0][1] + checkbox[0][2]) and (
                                        checkbox[0][0] + checkbox[0][2] <= x <= next_box[0][0]):
                                    text_list.append(results_df['text'][j])
                                    # print(text_list)
                            else:
                                if (checkbox[0][1] <= y <= checkbox[0][1] + checkbox[0][2]) and (
                                        checkbox[0][0] + checkbox[0][2] <= x):
                                    text_list.append(results_df['text'][j])
                                    # print(text_list)

                        if (k + 1) == len(checkboxes) and (checkbox[0][1] <= y <= checkbox[0][1] + checkbox[0][2]) and (
                                checkbox[0][0] + checkbox[0][2] <= x):
                            text_list.append(results_df['text'][j])
                            # print(text_list)
                    text_list = [" ".join(text_list)]
                    # print(text_list)
                    a = (k, text_list)
                    # A.append(a)
                    for ff, box in enumerate(boxes):
                        if (box[0] < checkbox[0][0] < box[0] + box[2]) and (
                                box[1] < checkbox[0][1] < box[1] + box[3]) and \
                                boxes[ff + 1][1] == box[1]:
                            param = boxes[ff + 1]
                            im = cv2.imread(file_path)
                            imm = im[param[1]:param[1] + param[3], param[0]:param[0] + param[2]]
                            im2 = Image.fromarray(imm.astype('uint8'))
                            st = image_to_string(im2)
                            b = (k, st)
                            # B.append(b)

                    if b!=[]:
                        print(f"\033[1m{b[1]}:{text_list}\033[0m")
                    else:
                        print(f"\033[1m{text_list}\033[0m")

                    print("-------------------------------------------------------------")

